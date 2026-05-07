from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from csv_cleaner_validator.cleaner import clean_and_validate_csv, normalize_column_name


def test_normalize_column_name() -> None:
    assert normalize_column_name(" Customer ID ") == "customer_id"
    assert normalize_column_name("Signup-Date") == "signup_date"


def test_clean_and_validate_csv_creates_output(tmp_path: Path) -> None:
    input_file = tmp_path / "messy.csv"
    output_file = tmp_path / "clean.csv"

    input_file.write_text(
        " Customer ID , Name , Email\n"
        "1, John Smith , john@example.com\n"
        "1, John Smith , john@example.com\n"
        ",,\n",
        encoding="utf-8",
    )

    summary = clean_and_validate_csv(
        input_file=input_file,
        output_file=output_file,
        required_columns=["customer_id", "name", "email"],
    )

    assert output_file.exists()
    assert summary["duplicate_rows_removed"] == 1
    assert summary["final_rows"] == 1


def test_missing_required_columns_raise_error(tmp_path: Path) -> None:
    input_file = tmp_path / "missing.csv"
    output_file = tmp_path / "clean.csv"

    input_file.write_text(
        "name,email\n"
        "John,john@example.com\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        clean_and_validate_csv(
            input_file=input_file,
            output_file=output_file,
            required_columns=["customer_id", "name", "email"],
        )
