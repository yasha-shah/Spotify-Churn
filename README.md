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

| Column | Description |
| --- | --- |
| `user_id` | Unique identifier for each user |
| `gender` | User gender (Male / Female / Other) |
| `age` | User age |
| `country` | User country |
| `subscription_type` | Spotify plan (Free, Premium, Family, Student) |
| `listening_time` | Minutes spent listening per day |
| `songs_played_per_day` | Number of songs played daily |
| `skip_rate` | Share of songs skipped |
| `device_type` | Device used (Mobile, Desktop, Web) |
| `ads_listened_per_week` | Number of ads heard per week |
| `offline_listening` | Whether offline listening is enabled (0 / 1) |
| `is_churned` | Whether the user stopped using the platform (0 = Active, 1 = Churned) |

Derived fields created in `utils.py`:

- `status` (Churned / Not churned)
- `age_group` (5-year bands, 16-20 to 56-60, matching the Excel pivot grouping)

## Key Insights
1. **About 1 in 4 users churned:** 2,071 of 8,000 users (**25.9%**) stopped using the platform.
2. **Family is the most at-risk plan:** the Family subscription has the highest churn rate (**27.5%**), followed by Student (26.2%), Premium (25.1%), and Free (24.9%).
3. **Mobile users churn at the highest rate:** Mobile has a **26.9%** churn rate, ahead of Desktop (25.7%) and Web (25.0%). Desktop has the most churned users (715) only because it has the most users overall.
4. **Pakistan and Germany lead churn by country:** Pakistan has the highest churn rate (**27.5%**) and Germany the most churned users (277, a 27.3% rate). India has the lowest rate (24.3%).
5. **Users aged 26-35 churn the most:** the 31-35 (**27.7%**) and 26-30 (27.5%) age groups have the highest churn rates. The 16-20 and 36-40 groups have the lowest (24.4%).
6. **Listening behaviour does not separate churned users from active ones:** churned and active users have almost the same daily listening time (153.0 vs 154.4 mins), songs played per day (50.6 vs 50.0), and skip rate (30.5% vs 29.8%). Churn is likely driven by factors outside listening habits, such as pricing or plan features.
7. **Differences between segments are small:** churn rates vary by less than 3.5 percentage points across every plan, device, country, age group, and gender, which is expected in a synthetic dataset. Results should be treated as directional rather than conclusive.

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
