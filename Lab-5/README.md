# SE Lab 5 - Static Code Analysis (ILLUSTRATIVE SAMPLE)

**Harika S | PES2UG24AM062 | Section 5A**

**IMPORTANT: This is not the instructor-assigned program.** The handout requires analysis of a Python file from an assigned GitHub repository, but the file/link has not been supplied. The expense-ledger source here is a standalone teaching sample.

The main branch history records one baseline commit followed by **three separate repair commits**: Pylint, Bandit and Flake8. The final version is in expense_ledger.py, and the initial code is also preserved in original_sample.py.

## Reproduce on Windows PowerShell
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python -m unittest -v
    python run_analysis.py

The script should create reports/before and reports/after, each containing pylint_report.txt, bandit_report.txt and flake8_report.txt. It verifies a final Pylint score > 9.5 and no post-fix Bandit or Flake8 findings.

**Verification caveat:** The static analyzers were not installed in the preparation environment and no valid analyzer outputs or Pylint score are claimed. Execute the commands on your computer, inspect the genuine reports, and run against the instructor-assigned script before submitting.
