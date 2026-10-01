import plotly.express as px
import streamlit as st
from plotly.subplots import make_subplots
from utils import (
    load_data, load_css, sidebar_filters, status_counts,
    STATUS_COLORS, STATUS_ORDER, BLUES, LEGEND_BOTTOM,
)

st.set_page_config(page_title='Spotify Churn Dashboard', layout='wide', initial_sidebar_state='expanded')

load_css()
full = load_data()

st.title('Spotify Churn Analysis Dashboard')

df = sidebar_filters(full)
if df.empty:
    st.warning('No users match the selected filters.')
    st.stop()

total_users = len(df)
churned = df[df['status'] == 'Churned']
churn_rate = len(churned) / total_users * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Users', f'{total_users:,}')
col2.metric('Churn Rate', f'{churn_rate:.1f}%')
col3.metric('Average Listening Time', f'{df["listening_time"].mean():,.2f} mins')
col4.metric('Average Songs Played Daily', f'{df["songs_played_per_day"].mean():,.0f}')

# What are the listening habits of users?
habits = df.groupby('status', as_index=False).agg(
    listening_time=('listening_time', 'mean'),
    songs_played_per_day=('songs_played_per_day', 'mean'),
)
habits_chart = make_subplots(rows=1, cols=2, horizontal_spacing=0.2)
for i, metric in enumerate(['listening_time', 'songs_played_per_day'], start=1):
    for status in STATUS_ORDER:
        row = habits[habits['status'] == status]
        habits_chart.add_bar(
            x=row['status'],
            y=row[metric],
            name=status,
            marker_color=STATUS_COLORS[status],
            showlegend=False,
            texttemplate='%{y:.1f}',
            textposition='outside',
            cliponaxis=False,
            hovertemplate=
            '<b>%{x}</b><br>'
            '%{y:,.2f}<br>'
            '<extra></extra>',
            row=1,
            col=i,
        )
habits_chart.update_layout(
    title={
        'text': 'What are the listening<br>habits of users?',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
habits_chart.update_layout(height=450, barcornerradius=4)
habits_chart.update_yaxes(title='Avg listening time (mins)', row=1, col=1)
habits_chart.update_yaxes(title='Avg songs per day', row=1, col=2)

# What platform has the most churned users?
device = churned.groupby('device_type', as_index=False).agg(users=('user_id', 'count')).sort_values('users', ascending=False)
device_chart = px.pie(device, names='device_type', values='users', hole=0.45, color_discrete_sequence=BLUES)
device_chart.update_layout(
    title={
        'text': 'What platform has the<br>most churned users?',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
device_chart.update_layout(height=450, showlegend=False)
device_chart.update_traces(
    textinfo='label+percent',
    textfont={'size': 14},
    insidetextfont={'color': ['#FAFAFA', '#1B1B1B', '#1B1B1B']},
    marker={'line': {'color': '#1b1b1b', 'width': 2}},
    sort=False,
    hovertemplate=
    '<b>%{label}</b><br>'
    'Churned users: %{value:,}<br>'
    'Share: %{percent:.1%}<br>'
    '<extra></extra>'
)

# What % of users stopped using Spotify?
plan = status_counts(df, 'subscription_type')
plan_chart = px.bar(
    plan, x='share', y='subscription_type', color='status', orientation='h', barmode='group',
    custom_data=['users'], color_discrete_map=STATUS_COLORS, category_orders={'status': STATUS_ORDER},
)
plan_chart.update_xaxes(title='', range=[0, 100], ticksuffix='%')
plan_chart.update_yaxes(title='')
plan_chart.update_layout(
    title={
        'text': 'What % of users stopped<br>using Spotify?',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
plan_chart.update_layout(height=450, barcornerradius=4, legend=LEGEND_BOTTOM)
plan_chart.update_traces(
    texttemplate='%{x:.0f}%',
    textposition='outside',
    cliponaxis=False,
    hovertemplate=
    '<b>%{y}</b> · %{fullData.name}<br>'
    '%{x:.1f}% of users (%{customdata[0]:,})<br>'
    '<extra></extra>'
)

# What country has the highest churn?
country = status_counts(df, 'country')
country_order = (
    country[country['status'] == 'Churned'].sort_values('users')['country'].tolist()
    or sorted(country['country'].unique())
)
country_chart = px.bar(
    country, x='users', y='country', color='status', orientation='h', barmode='group',
    custom_data=['share'], color_discrete_map=STATUS_COLORS,
    category_orders={'status': STATUS_ORDER, 'country': country_order[::-1]},
)
country_chart.update_xaxes(title='')
country_chart.update_yaxes(title='')
country_chart.update_layout(
    title={
        'text': 'What country has the<br>highest churn?',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
country_chart.update_layout(height=500, barcornerradius=4, legend=LEGEND_BOTTOM)
country_chart.update_traces(
    hovertemplate=
    '<b>%{y}</b> · %{fullData.name}<br>'
    'Users: %{x:,}<br>'
    '%{customdata[0]:.1f}% of country<br>'
    '<extra></extra>'
)

# What age range has the highest churn?
age = status_counts(df, 'age_group')
age_chart = px.bar(
    age, x='age_group', y='users', color='status', barmode='group',
    custom_data=['share'], color_discrete_map=STATUS_COLORS, category_orders={'status': STATUS_ORDER},
)
age_chart.update_xaxes(title='', type='category')
age_chart.update_yaxes(title='Users')
age_chart.update_layout(
    title={
        'text': 'What age range has the highest churn?',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
age_chart.update_layout(height=500, barcornerradius=4, legend=LEGEND_BOTTOM)
age_chart.update_traces(
    texttemplate='%{y:,}',
    textposition='outside',
    cliponaxis=False,
    hovertemplate=
    '<b>Age %{x}</b> · %{fullData.name}<br>'
    'Users: %{y:,}<br>'
    '%{customdata[0]:.1f}% of age range<br>'
    '<extra></extra>'
)

chart1, chart2, chart3 = st.columns(3)
chart1.plotly_chart(habits_chart, width='stretch')
chart2.plotly_chart(device_chart, width='stretch')
chart3.plotly_chart(plan_chart, width='stretch')

chart4, chart5 = st.columns([1, 2])
chart4.plotly_chart(country_chart, width='stretch')
chart5.plotly_chart(age_chart, width='stretch')

st.caption(
    f'Source: spotify_churn_dashboard.xlsx · {len(full):,} users · '
    '[GitHub](https://github.com/yasha-shah/) · [LinkedIn](https://linkedin.com/in/shah-yasha)'
)
