# Spotify Churn Analysis

Analysis of churn across 8,000 Spotify users by subscription plan, device, country, age, and listening behaviour. The original analysis was built in Excel (pivot tables, slicers, and charts). This repo recreates that one-page Excel dashboard in Streamlit.

## What this answers

- What share of users stopped using Spotify, by subscription plan
- Which platform, country, and age range have the most churned users
- How listening time and songs played compare between churned and retained users

## Dashboard

A single page (`app.py`) with the same layout as the Excel `Dashboard` sheet:

| Area | Contents |
| --- | --- |
| Sidebar filters | Multi-select dropdowns for Gender, Country, Subscription type, Device type, Churn status (empty = all, like a cleared Excel slicer) |
| KPI cards | Total Users, Churn Rate, Average Listening Time, Average Songs Played Daily |
| Charts | - What are the listening habits of users?<br>- What platform has the most churned users?<br>- What % of users stopped using Spotify?<br>- What country has the highest churn?<br>- What age range has the highest churn? |

## Data

| Path | Role |
| --- | --- |
| `data/raw/spotify_churn_dashboard.xlsx` | Excel dashboard; the app reads the hidden `spotify_dataset` sheet |

Columns: `user_id`, `gender`, `age`, `country_short`, `country`, `subscription_type`, `listening_time`, `songs_played_per_day`, `skip_rate`, `device_type`, `ads_listened_per_week`, `offline_listening`, `is_churned`.

Derived fields created in `utils.py`:

- `status` (Churned / Not churned)
- `age_group` (5-year bands, 16-20 to 56-60, matching the Excel pivot grouping)

## Key Insights
1. On average, churned users have a comparatively lower daily listening time than that of the active users.
2. The Family subscription has the highest churn rate among all the subscription types, which makes it the most at-risk plan.
3. Out of all the countries, Germany has the most churned users.
4. Desktop users are more prone to churn, which could be because of poor user experience, or lack of some features which are available on other device types.

## Stack

- Python, pandas, openpyxl
- Streamlit and Plotly for the dashboard
- Excel for the original pivot-table dashboard

## Run locally

For Windows:

```
uv venv dataenv
uv pip install --python dataenv -r requirements.txt
dataenv\Scripts\python.exe -m streamlit run app.py
```

On macOS / Linux:
```
uv venv dataenv
uv pip install --python dataenv -r requirements.txt
dataenv/bin/python -m streamlit run app.py
```

Requirements: `streamlit`, `pandas`, `plotly`, `openpyxl`.

## Project layout

```
app.py                  # Streamlit dashboard (single page)
utils.py                # Cached loader, CSS inject
style.css               # Metric, and chart styling
data/raw/               # Source Excel workbook
```

## Author

[Yasha Shah](https://github.com/yasha-shah/) · [LinkedIn](https://linkedin.com/in/shah-yasha)
