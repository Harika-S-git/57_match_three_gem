# Lab 5 - Issue register & reflection (SAMPLE, NOT ASSIGNED SCRIPT)

Harika S | SRN PES2UG24AM062 | Section 5A

The following are findings by **source inspection** of original_sample.py, not claimed outputs from Pylint/Bandit/Flake8.

| Issue | Type | Line in baseline | Description | Fix approach |
|---|---|---|---|---|
| unsafe eval | Security | parse_amount | Executes Python text | Decimal parser |
| shell=True | Security | write_receipt | Command injection risk | Path.write_text |
| MD5 hash | Security | receipt_checksum | Weak hashing choice | SHA-256 |
| mutable list default | Correctness | add_expense | Shared records across calls | None and allocate |
| bare except | Correctness | parse_amount | Hides unexpected errors | Specific exceptions |
| unused os import | Style | imports | Unused dependency | Remove |
| missing spacing | Style | main | PEP8 E225 | Add whitespace |

## Repair plan
1. Pylint phase: mutable default and broad exception fixes.
2. Bandit phase: replace eval, shell invocation and MD5.
3. Flake8 phase: remove unused import, format and document code.

## Reflection
**Why all three?** Pylint focuses on Python practices, Bandit on security anti-patterns, Flake8 on style and unused code.

**Why fix security problems first?** Arbitrary evaluation and shell execution may execute attacker-controlled input, a more serious risk than formatting defects.

**What changed?** The example now parses decimal amounts, avoids executing commands, computes a SHA-256 digest and does not share mutable histories.

**Does clean static analysis guarantee correctness?** No; add tests, input validation review and dependency checks.

No explicit reflection-question list was included in the supplied handout. These are representative answers; replace with lecturer questions if separately provided.

## Evidence
Run the genuine tools with run_analysis.py. The current repository does not include fabricated before/after analyzer outputs.
