from pathlib import Path
import sys
from pprint import pprint

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from csv_cleaner_validator import clean_and_validate_csv


def main() -> None:
    input_file = PROJECT_ROOT / "sample_data" / "messy_customers.csv"
    output_file = PROJECT_ROOT / "output" / "clean_customers.csv"

    required_columns = [
        "customer_id",
        "name",
        "email",
        "country",
        "signup_date",
    ]

    summary = clean_and_validate_csv(
        input_file=input_file,
        output_file=output_file,
        required_columns=required_columns,
    )

    print("CSV cleaned successfully.")
    print("Validation summary:")
    pprint(summary)


if __name__ == "__main__":
    main()
