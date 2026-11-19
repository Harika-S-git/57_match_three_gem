"""Sample expense-ledger module: Pylint and Bandit-related defects addressed."""
import os
import json
import hashlib
from decimal import Decimal, InvalidOperation
from pathlib import Path


def parse_amount(text):
    """Convert only ordinary decimal amounts; never evaluate Python input."""
    try:
        value = Decimal(str(text))
        if not value.is_finite() or value < 0:
            return None
        return value.quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError, ValueError):
        return None


def add_expense(name, amount_text, records=None):
    """Return entries, allocating fresh history when no records were supplied."""
    if records is None:
        records = []
    amount = parse_amount(amount_text)
    if amount is None:
        return records
    records.append({"name": name, "amount": str(amount)})
    return records


def receipt_checksum(name):
    """Use SHA-256 instead of MD5 for the digest."""
    return hashlib.sha256(name.encode("utf-8")).hexdigest()


def write_receipt(records, filename):
    """Write JSON without shell interpolation or command execution."""
    Path(filename).write_text(json.dumps(records, indent=2), encoding="utf-8")
    return filename


def main():
    """Demonstrate the parser and receipt generator."""
    entries=add_expense("Espresso", "25")
    path = write_receipt(entries, "demo_receipt.json")
    print("Saved receipt:", path, "checksum:", receipt_checksum("Espresso"))


if __name__ == "__main__":
    main()
