from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def normalize_column_name(column_name: str) -> str:
    """Normalize a column name to lowercase snake_case."""
    return (
        str(column_name)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize all column names in a DataFrame."""
    df = df.copy()
    df.columns = [normalize_column_name(column) for column in df.columns]
    return df


def trim_text_values(df: pd.DataFrame) -> pd.DataFrame:
    """Trim extra spaces from text columns."""
    df = df.copy()

    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype(str).str.strip()
        df[column] = df[column].replace({"nan": pd.NA, "": pd.NA})

    return df


def validate_required_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> list[str]:
    """Return missing required columns after normalizing required names."""
    normalized_required = {normalize_column_name(column) for column in required_columns}
    existing_columns = set(df.columns)

    return sorted(normalized_required - existing_columns)


def clean_and_validate_csv(
    input_file: str | Path,
    output_file: str | Path,
    required_columns: Iterable[str] | None = None,
) -> dict:
    """Clean and validate a CSV file and export a cleaned CSV."""
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    raw_df = pd.read_csv(input_path)
    original_rows = len(raw_df)

    df = normalize_columns(raw_df)
    df = trim_text_values(df)
    df = df.dropna(how="all")

    rows_after_empty_drop = len(df)

    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()

    if required_columns:
        missing_required_columns = validate_required_columns(df, required_columns)
        if missing_required_columns:
            raise ValueError(
                "Missing required columns: " + ", ".join(missing_required_columns)
            )

    missing_values = {
        column: int(df[column].isna().sum())
        for column in df.columns
        if int(df[column].isna().sum()) > 0
    }

    df.to_csv(output_path, index=False)

    return {
        "input_file": str(input_path),
        "output_file": str(output_path),
        "original_rows": original_rows,
        "rows_after_empty_drop": rows_after_empty_drop,
        "duplicate_rows_removed": duplicate_count,
        "final_rows": len(df),
        "columns": list(df.columns),
        "missing_values": missing_values,
    }
