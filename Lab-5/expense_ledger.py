"""Expense ledger used to demonstrate static-analysis remediation.

This is a self-contained SAMPLE, not the Lab 5 instructor-assigned source.
"""

import hashlib
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def parse_amount(text):
    """Return a nonnegative two-decimal-place amount or ``None``."""
    try:
        amount = Decimal(str(text))
        if not amount.is_finite() or amount < 0:
            return None
        return amount.quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError, ValueError):
        return None


def add_expense(name, amount_text, records=None):
    """Add one item without sharing a mutable default history."""
    if records is None:
        records = []
    amount = parse_amount(amount_text)
    if amount is not None:
        records.append({"name": name, "amount": str(amount)})
    return records


def receipt_checksum(name):
    """Compute a SHA-256 digest for the receipt label."""
    return hashlib.sha256(name.encode("utf-8")).hexdigest()


def write_receipt(records, filename):
    """Save records as JSON without executing a shell command."""
    destination = Path(filename)
    destination.write_text(json.dumps(records, indent=2), encoding="utf-8")
    return str(destination)


def main():
    """Exercise the sample with deterministic, non-sensitive inputs."""
    entries = add_expense("Espresso", "25")
    filename = write_receipt(entries, "demo_receipt.json")
    print("Saved receipt:", filename)
    print("SHA-256:", receipt_checksum("Espresso"))


if __name__ == "__main__":
    main()
