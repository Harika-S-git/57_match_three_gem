"""Regression tests for the repaired sample."""
import json
import tempfile
import unittest
from pathlib import Path
from expense_ledger import add_expense, parse_amount, receipt_checksum, write_receipt


class ExpenseLedgerTests(unittest.TestCase):
    def test_amount_rejects_expressions_and_negatives(self):
        self.assertIsNone(parse_amount("__import__('os').system('echo bad')"))
        self.assertIsNone(parse_amount("-5"))
        self.assertIsNone(parse_amount("NaN"))
        self.assertEqual(str(parse_amount("12.50")), "12.50")

    def test_history_not_shared(self):
        first = add_expense("Latte", "40")
        second = add_expense("Tea", "20")
        self.assertEqual(len(first), 1)
        self.assertEqual(len(second), 1)

    def test_receipt_writes_safe_json(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / "receipt.json"
            write_receipt(add_expense("Espresso", "25"), dest)
            saved = json.loads(dest.read_text(encoding="utf-8"))
            self.assertEqual(saved[0]["amount"], "25.00")

    def test_sha256(self):
        self.assertEqual(len(receipt_checksum("Latte")), 64)


if __name__ == "__main__":
    unittest.main()
