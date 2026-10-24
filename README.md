[![CI](https://github.com/Ibrahim-56/financial-dashboard/actions/workflows/tests.yml/badge.svg)](https://github.com/Ibrahim-56/financial-dashboard/actions/workflows/tests.yml)

# Financial Performance Dashboard

An interactive Streamlit dashboard that summarizes monthly revenue, expenses, and profit using a synthetic dataset.

## Features

- KPI totals for revenue, expenses, and profit
- Monthly revenue trend
- Monthly expense trend
- Monthly profit chart

## Technology

- Python
- Streamlit
- Pandas
- Plotly

## Run locally

Requires Python 3.10 or later.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

The app expects `financial_dashboard_data.csv` in the repository root.

## Tests and CI

Run the dataset checks locally:

```bash
pytest -v
```

GitHub Actions checks Python syntax and validates the dataset schema, numeric values, and profit calculations. These checks do not replace a manual review of the dashboard in a browser.

## Data note

The included financial dataset is synthetic and intended for demonstration; it is not a real company's financial data.
