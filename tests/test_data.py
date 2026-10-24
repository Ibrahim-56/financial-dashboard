from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "financial_dashboard_data.csv"


def test_financial_dataset_has_expected_columns():
    data = pd.read_csv(DATA_PATH)
    assert {"Month", "Revenue", "Expenses", "Profit"}.issubset(data.columns)


def test_financial_values_are_numeric_and_non_negative():
    data = pd.read_csv(DATA_PATH)
    for column in ("Revenue", "Expenses", "Profit"):
        assert pd.api.types.is_numeric_dtype(data[column])
        assert (data[column] >= 0).all()


def test_profit_matches_revenue_minus_expenses():
    data = pd.read_csv(DATA_PATH)
    difference = (data["Revenue"] - data["Expenses"] - data["Profit"]).abs()
    assert (difference < 0.01).all()
