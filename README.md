# Spotify Churn Analysis Dashboard
## Project Overview
This project is a data analysis of a simulated Spotify user dataset to analyse customer churn. It provides an interactive dashboard to understand various factors affecting user retention for the platform and will help in data-driven decision making.  

## Dataset
The [data](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis/data) is from a synthetically generated dataset sourced from Kaggle.  

### Key Columns:
|Column Name|Description|
|-----------|-----------|
|user_id|Unique identifier for each user|
|gender|User gender (Male/Female/Other)|
|age|User age|
|country|User country|
|subscription_type|Type of Spotify subscription (Free, Premium, Family, Student)|
|listening_time|Minutes spent listening per day|
|songs_played_per_day|Number of songs played daily|
|device_type|Device used (Mobile, Desktop, Web)|
|ads_listened_per_week|Number of ads heard per week|
|is_churned|If the user still uses the platform (0 = Active, 1 = Churned)|  

## Dashboard Overview
The dashboard shows a dynamic analysis of the data using various KPIs and visualizations, which can be further filtered using slicers.  


<img width="1579" height="808" alt="dashboard_screenshot" src="https://github.com/user-attachments/assets/4d935f5e-0474-4a0b-b87e-787ed9ee1e0f" />


### KPIs: 
Key Performance Indicators show **Total Users**, **Churn Rate**, **Average Listening Time**, and **Average Songs Played Daily** for a quick overview of the data.

### Slicers: 
Slicers can be used to further filter down the KPIs and visualizations to get a more in-depth analysis.  
Data can be filtered on the basis of:  
- **Gender**
- **Country**
- **Subscription Type**
- **Device Type**
- **Churn Status**

### Visualizations: 
1. Clustered Column Chart: A comparison of listening habits (Daily listening time and songs played daily) for users who churned versus those who stayed.
2. Pie Chart: A distribution of churned users for different device types.
3. Clustered Bar Chart: A breakdown of churn rate by subscription type.
4. Clustered Bar Chart: A breakdown of churn rate by country.
5. Clustered Column Chart: A distribution of churned users across different age groups.

![dashboard_gif](https://github.com/user-attachments/assets/2803029b-dffa-4c78-b33a-fd19e45aace0)

## Key Insights
1. On average, churned users have a comparatively lower daily listening time than that of the active users.
2. The Family subscription has the highest churn rate among all the subscription types, which makes it the most at-risk plan.
3. Out of all the countries, Germany has the most churned users.
4. Desktop users are more prone to churn, which could be because of poor user experience, or lack of some features which are available on other device types.

### Tools Used:  
Microsoft Excel: For data manipulation, pivot tables, and making the final dashboard.  

---
### Project Link:  
[Spotify-Churn-Analysis-Dashboard](https://github.com/yasha-shah/Spotify-Churn-Dashboard/blob/main/spotify_churn_dashboard.xlsx)
