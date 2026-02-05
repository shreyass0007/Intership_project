# Week 4 — Sales Data Analysis ✅

## Overview

This week focuses on exploring and cleaning sales data, performing basic analysis, and producing visualizations and a cleaned dataset for downstream use. Work is captured in the Jupyter Notebook `analysis.ipynb`.

---

## Contents 🔍

- `analysis.ipynb` — main notebook containing data loading, cleaning, analysis, and visualizations
- `data/sales_data.csv` — raw input dataset used for analysis
- `output/cleaned_sales_data.csv` — cleaned dataset exported by the notebook

---

## Objectives 🎯

- Inspect the sales dataset and identify quality issues
- Clean and preprocess the data (missing values, types, anomalies)
- Perform exploratory analysis and create visualizations
- Export a cleaned CSV for future analysis or modeling

---

## How to run 🔧

1. Create and activate a Python virtual environment (Windows example):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install required packages (either with a project `requirements.txt` or manually):

```powershell
pip install pandas numpy matplotlib seaborn jupyter scikit-learn
# Or if you add a requirements file:
# pip install -r requirements.txt
```

3. Start Jupyter and open the notebook:

```powershell
jupyter notebook
# or
jupyter lab
```

4. Run the notebook cells sequentially. The cleaned CSV will be written to `output/cleaned_sales_data.csv`.

---

## Notebook structure (high level) 🧭

1. Data loading and initial inspection
2. Data cleaning and preprocessing
3. Exploratory data analysis (summary statistics and visualizations)
4. Exporting cleaned data
5. Notes and next steps

---

## Reproducibility & Notes 💡

- For consistent results, set random seeds where relevant (notebook includes notes if applicable).
- If large transformations are added, consider splitting heavy computation into scripts to avoid re-running all cells during development.

---

## Results & Outputs ✅

- A cleaned dataset: `output/cleaned_sales_data.csv`
- Visualizations and analysis written inline in `analysis.ipynb` (including charts and summarized findings)

---

## Contributing / Questions

If you find bugs, need clarifications, or want to extend the analysis, open an issue or submit a pull request. For quick questions, contact the project owner or your mentor.

---

**Notes:** If you'd like, I can also add a `requirements.txt` for this week with pinned package versions and/or a small script that runs the entire notebook headlessly (e.g., `papermill`) — tell me which you'd prefer. ✨
