import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(layout="wide")

data6 = pd.read_csv('data6.csv')

byYR_crime = data6.groupby(['PRD_DE', 'C1_NM', 'RGN'])['DT'].apply(lambda x: x.sum()).unstack().sum(1)
byYR_crime_top = byYR_crime.unstack().T.sort_values(2021, ascending=False).dropna().iloc[:20]
barrank_data = byYR_crime_top.stack().rename('검거건수').reset_index()
barrank_data.rename(columns={'PRD_DE': '년', 'C1_NM': '범죄'}, inplace=True)

fig_bar = px.histogram(
    barrank_data, x="범죄", y="검거건수", color="범죄",
    animation_frame="년", range_y=[7000, 500000],
    color_discrete_sequence=px.colors.qualitative.Plotly_r
)
fig_bar.update_yaxes(showgrid=False)
fig_bar.update_xaxes(categoryorder='total descending')
fig_bar.update_traces(hovertemplate=None)
fig_bar.update_layout(template='plotly_white')
fig_bar.update_layout(yaxis_title='검거건수', xaxis_title='')
fig_bar.update_layout(
    autosize=False,
    width=1200,
    height=700,
)
fig_bar['layout']['sliders'][0]['pad']=dict(t=100)
# fig_bar.show()



rgn_crime_cnt = data6.copy()
pop_ = data6[['RGN', 'PRD_DE', '남', '여', '인구']].drop_duplicates().reset_index(drop=True)
rgn_crime_cnt = rgn_crime_cnt.groupby(['RGN', 'ITM_NM', 'UNIT_NM', 'PRD_DE'])['DT'].sum().reset_index()
rgn_crime_cnt = rgn_crime_cnt.merge(pop_, on=['PRD_DE', 'RGN'], how='left')
rgn_crime_cnt.rename(columns={'PRD_DE': '년', 'C1_NM': '범죄', 'RGN': '지역', 'DT': '검거건수'}, inplace=True)
rgn_crime_cnt['1만명당 검거건수'] = rgn_crime_cnt['검거건수'] / (rgn_crime_cnt['인구'] / 10000)

fig = px.scatter(rgn_crime_cnt, x="인구", y="1만명당 검거건수",
                 size="검거건수", color="지역",
                 log_x=False, log_y=True, size_max=60,
                 range_y=[300, 2500], range_x=[100000, 15000000],
                 animation_frame="년",
                 color_discrete_sequence=px.colors.qualitative.Plotly_r)

# fig.update_yaxes(showgrid=False)
# fig.update_traces(hovertemplate=None)
fig.update_layout(template='plotly_white')
fig.update_layout(yaxis_title='1만명당 검거수', xaxis_title='인구')
fig.update_layout(
    autosize=False,
    width=1200,
    height=700,
)
fig['layout']['sliders'][0]['pad']=dict(t=50)
# fig.show()

st.title("연도별 최고 발생 범죄 현황")
st.plotly_chart(fig_bar)

st.title("연도별 지역 인구밀도 대비 범죄 발생률")
st.plotly_chart(fig)
