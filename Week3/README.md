# Week 3 — Sales Analysis

This folder contains a Jupyter notebook and a sample dataset used for a simple sales analysis.

## Contents

-   `sales_analysis.ipynb` — Notebook that performs data loading, cleaning, exploratory analysis, simple visualizations, and summary metrics.
-   `sales_data.csv` — Example sales dataset used by the notebook.

## Purpose

The notebook demonstrates reading a CSV, performing basic data transformations, producing plots (e.g., time-series, category breakdowns), and summarizing sales performance.

## Dependencies

Typical libraries used (install into your environment if needed):

-   `pandas`
-   `numpy`
-   `matplotlib` or `seaborn`
-   `jupyter`

## Quick setup (Windows)

Create a virtual environment and install common data libraries:

```powershell
python -m venv .venv..venvScriptsActivate.ps1pip install --upgrade pippip install pandas numpy matplotlib seaborn jupyter
```

## Open the notebook

Launch Jupyter and open the notebook file:

```powershell
jupyter notebook Week3/sales_analysis.ipynb
```

## Tips

-   If the notebook throws an import error, install the missing package into the active environment.
-   Inspect the first cells of `sales_analysis.ipynb` for any project-specific notes or additional package lists.
-   To reuse the analysis with your own data, replace `sales_data.csv` with a file of the same schema or update the data-loading cell accordingly.

## License / Notes

This folder is part of a learning exercise — feel free to modify, extend, or use the analysis as a template for your own datasets.