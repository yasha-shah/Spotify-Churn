import pandas as pd
import streamlit as st

LEGEND_BOTTOM = {'orientation': 'h', 'yanchor': 'top', 'y': -0.08, 'xanchor': 'center', 'x': 0.5, 'title': ''}
CHURN_COLOR = '#6BA0B8'
RETAINED_COLOR = '#2A5F8C'
STATUS_COLORS = {'Churned': CHURN_COLOR, 'Not churned': RETAINED_COLOR}
STATUS_ORDER = ['Churned', 'Not churned']
BLUES = ['#2A5F8C', '#6BA0B8', '#B7D0E2']

AGE_LABELS = ['16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60']

FILTERS = {
    'gender': 'Gender',
    'country': 'Country',
    'subscription_type': 'Subscription type',
    'device_type': 'Device type',
    'status': 'Churn status',
}


@st.cache_data
def load_data():
    df = pd.read_excel('data/raw/spotify_churn_dashboard.xlsx', sheet_name='spotify_dataset')
    df = df.drop(columns=['not_churned'])
    df['status'] = df['is_churned'].map({1: 'Churned', 0: 'Not churned'})
    df['age_group'] = pd.cut(df['age'], bins=range(15, 61, 5), labels=AGE_LABELS)
    return df


def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def sidebar_filters(df):
    st.sidebar.header('Filters')
    for field, label in FILTERS.items():
        options = STATUS_ORDER if field == 'status' else sorted(df[field].unique())
        chosen = st.sidebar.multiselect(label, options, placeholder='All', key=f'filter_{field}')
        # An empty filter means "no filter", like a cleared Excel slicer
        if chosen:
            df = df[df[field].isin(chosen)]
    return df


def status_counts(df, col):
    out = df.groupby([col, 'status'], as_index=False, observed=True).agg(users=('user_id', 'count'))
    totals = out.groupby(col, observed=True)['users'].transform('sum')
    out['share'] = out['users'] / totals * 100
    return out


