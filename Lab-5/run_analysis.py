"""Run genuine Pylint, Bandit and Flake8 against before and after revisions."""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def analyze(source, phase):
    results = {}
    for tool in ("pylint", "bandit", "flake8"):
        command = [sys.executable, "-m", tool]
        if tool == "bandit":
            command += ["-r"]
        command.append(str(source))
        try:
            result = subprocess.run(command, capture_output=True, text=True,
                                    check=False, cwd=HERE)
        except FileNotFoundError as error:
            raise SystemExit(f"Tool not installed: {error}") from error
        target = HERE / "reports" / phase / f"{tool}_report.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(result.stdout + result.stderr +
                          f"\n[Exit status: {result.returncode}]\n",
                          encoding="utf-8")
        print(phase, tool, result.returncode, "->", target)
        results[tool] = result
    return results


def main():
    analyze(HERE / "original_sample.py", "before")
    after = analyze(HERE / "expense_ledger.py", "after")
    text = after["pylint"].stdout
    match = re.search(r"rated at ([0-9.]+)/10", text)
    if not match or float(match.group(1)) <= 9.5:
        raise SystemExit("Pylint score must be above 9.5; check reports.")
    if after["bandit"].returncode or after["flake8"].returncode:
        raise SystemExit("Post-fix security/style findings remain; check reports.")
    print("Verified: final Pylint score", match.group(1),
          "/10 and zero post-fix Bandit/Flake8 findings.")


if __name__ == "__main__":
    main()
