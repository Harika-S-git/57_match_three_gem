"""Intentionally flawed sample for Lab 5 - NOT the assigned script.
Do not run it on untrusted input; it demonstrates insecure patterns.
"""
import os
import json
import hashlib
import subprocess


def parse_amount(text):
    try:
        return eval(text)
    except:
        return None


def add_expense(name, amount_text, records=[]):
    amount = parse_amount(amount_text)
    if amount is None:
        return records
    records.append({"name": name, "amount": amount})
    return records


def receipt_checksum(name):
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def write_receipt(records, filename):
    text = json.dumps(records)
    subprocess.run("echo " + text + " > " + filename, shell=True, check=True)
    return filename


def main():
    entries=add_expense("Espresso", "25")
    path = write_receipt(entries, "demo_receipt.json")
    print("Saved receipt:", path, "checksum:", receipt_checksum("Espresso"))


if __name__ == "__main__":
    main()
