"""Sample expense-ledger module: mutable defaults and broad exception fixed."""
import os
import json
import hashlib
import subprocess


def parse_amount(text):
    """Parse a value; security fix is deliberately deferred to the Bandit stage."""
    try:
        return eval(text)
    except (SyntaxError, ValueError, TypeError, NameError):
        return None


def add_expense(name, amount_text, records=None):
    """Return entries, allocating fresh history when no records were supplied."""
    if records is None:
        records = []
    amount = parse_amount(amount_text)
    if amount is None:
        return records
    records.append({"name": name, "amount": amount})
    return records


def receipt_checksum(name):
    """Return a digest for receipt data (algorithm fixed in Bandit stage)."""
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def write_receipt(records, filename):
    """Write a receipt (shell invocation fixed in Bandit stage)."""
    text = json.dumps(records)
    subprocess.run("echo " + text + " > " + filename, shell=True, check=True)
    return filename


def main():
    """Demonstrate the parser and receipt generator."""
    entries=add_expense("Espresso", "25")
    path = write_receipt(entries, "demo_receipt.json")
    print("Saved receipt:", path, "checksum:", receipt_checksum("Espresso"))


if __name__ == "__main__":
    main()
