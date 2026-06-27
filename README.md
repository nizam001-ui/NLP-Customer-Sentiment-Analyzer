<div align="center">

# 📊 E-Commerce Customer Sentiment Analyzer

### NLP-powered review intelligence, visualized in Power BI

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP%20Sentiment-yellow)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

## 📑 Table of Contents

* [Project Overview](#-project-overview)
* [Business Value](#-business-value)
* [Tech Stack](#%EF%B8%8F-tech-stack)
* [How It Works](#-how-it-works)
* [Dashboard Previews](#-dashboard-previews)
* [Repository Structure](#-repository-structure)
* [Getting Started](#-getting-started)
* [Author](#-author)

---

## 🚀 Project Overview

Understanding customer feedback at scale is impossible to do manually. At even a modest volume, reading every review line-by-line stops being realistic — yet that feedback contains exactly the signal a product or marketing team needs.

This project is an **end-to-end data pipeline** that:

1. Ingests raw, unstructured customer reviews
2. Applies **Natural Language Processing (NLP)** to score each review's sentiment polarity mathematically
3. Surfaces the result as an **interactive Power BI dashboard** stakeholders can filter and explore without touching a spreadsheet

The output isn't just "positive vs. negative" — it's a structured, queryable view of brand health that scales to however many reviews come in.

## 💡 Business Value

By converting unstructured text into structured sentiment scores, this pipeline lets marketing and product teams:

1. **Instantly isolate product pain points** — surface specific defects or complaints mentioned in 1-star reviews without reading them one by one.
2. **Track customer satisfaction trends over time** — spot whether sentiment is improving, declining, or spiking around specific events (launches, price changes, shipping issues).
3. **Cut manual review time to near zero** — replace hours of manual reading with a dashboard that filters thousands of reviews in seconds.

## ⚙️ Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| **Data Processing** | Python (Pandas) | Cleaning, structuring, and preparing raw review data |
| **Sentiment Engine** | TextBlob (NLP) | Calculating polarity scores and classifying sentiment |
| **Storage** | CSV | Lightweight, portable storage for raw and scored data |
| **Visualization** | Power BI (DAX) | Interactive dashboard and modeling layer |

## 🔍 How It Works

```
raw_reviews.csv
      │
      ▼
1_generate_data.py   →  loads / prepares the raw review dataset
      │
      ▼
2_nlp_analyzer.py    →  runs each review through TextBlob,
                         scores polarity, classifies as
                         Positive / Neutral / Negative
      │
      ▼
analyzed_reviews.csv  →  scored dataset, ready for BI
      │
      ▼
analyzed_reviews.pbix →  interactive Power BI dashboard
```

Each review is reduced to a single, comparable **polarity score**, which is what makes it possible to aggregate, filter, and trend sentiment across thousands of reviews at once instead of reading them individually.

## 📈 Dashboard Previews

*The dashboard lets stakeholders instantly filter between Positive, Neutral, and Negative reviews to isolate product pain points and track sentiment over time.*

![Dashboard View 1](images/1_dashboard_preview.png)
![Dashboard View 2](images/2_dashboard_preview.png)
![Dashboard View 3](images/3_dashboard_preview.png)

## 📂 Repository Structure

```text
NLP-Customer-Sentiment-Analyzer/
│
├── data/
│   ├── raw_reviews.csv              # Initial, unformatted review dataset
│   └── analyzed_reviews.csv         # Final dataset with NLP sentiment scores
│
├── scripts/
│   ├── 1_generate_data.py           # Data extraction / generation script
│   └── 2_nlp_analyzer.py            # TextBlob NLP processing engine
│
├── dashboard/
│   └── analyzed_reviews.pbix        # Interactive Power BI file
│
├── images/
│   ├── 1_dashboard_preview.png
│   ├── 2_dashboard_preview.png
│   └── 3_dashboard_preview.png
│
└── README.md
```

## ▶️ Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/NLP-Customer-Sentiment-Analyzer.git
cd NLP-Customer-Sentiment-Analyzer

# 2. Install dependencies
pip install pandas textblob

# 3. Run the pipeline
python scripts/1_generate_data.py
python scripts/2_nlp_analyzer.py

# 4. Open the dashboard
# Launch dashboard/analyzed_reviews.pbix in Power BI Desktop
```

## 👨‍💻 Author

**Nizam ud din** — *B.S. Computer Science, University of Turbat*

* Data Analyst & BI Developer
* Specializing in Python, SQL, and Power BI reporting

---

<div align="center">
<sub>If this project is useful to you, consider leaving a ⭐ on the repository.</sub>
</div>
