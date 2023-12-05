import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(layout="wide")

data6 = pd.read_csv('data6.csv')
incl = ['절도','불법사용','침입절도','불법사용','침입절도','장물','사기','컴퓨터등사용사기','부당이득','편의시설부정이용','전기통신금융사기피해금환급에관한특별법','보험사기방지특별법','횡령','배임','배임수재','배임증재','손괴','손괴치상','손괴치사','살인(기수)','살인(미수, 예비, 음모, 방조)','강도','강도상해','강도치상','강도강간/강제추행','강도살인','강도치사','일반방화','방화치상','방화치사','강간','강제추행','간음','강간등(강간,준강간,간음,강제추행,준강제추행)','강간등상해','강간등치상','강간등살인','강간등치사','특수강도강간등','카메라등 이용촬영','성적목적의 장소침입','통신매체 이용음란','공중밀집장소 추행','허위영상물편집·반포등','촬영물등이용협박·강요','폭행','폭행치상','폭행치사','상해','상해치사','협박','공갈','약취/유인','수수/은닉','부녀매매','국외이송','인신매매','약취와유인 상해,치상,살해,치사','체포','체포치상','체포치사','감금','감금치상','감금치사','폭력행위등(손괴,강요,주거침입등)','폭력행위등(단체등의구성, 활동)','통화','유가증권·인지·우표','문서','인장','직무유기','직권남용','수뢰','증뢰','도박','복표','공연음란','공연음란','과실치상','과실치사','업무상과실치상','업무상과실치사','실화','명예','권리행사방해','신용업무경매','주거침입','비밀침해','유기','유기치상','유기치사','교통방해','공무방해','공무방해치상','공무방해치사','도주와범인은닉','위증과증거인멸','무고','공안을해하는죄','내란의죄','음용수에관한죄','일수와수리에관한죄','기타','가정폭력범죄의 처벌등에 관한특례법','가축분뇨의 관리 및 이용에 관한법률','감염병의 예방 및 관리에 관한법률','개발제한구역의 지정 및 관리에 관한 특별조치법','개인정보보호법','건강기능식품에 관한법률','건설기계관리법','건설산업기본법','건축법','게임산업진흥에 관한법률','결혼중개업의 관리에 관한법률','경범죄처벌법','고용보험법','공유수면관리 및 매립에 관한법률','공유재산 및 물품관리법','공인중개사법','공중위생관리법','공직선거법','관세법','교통사고처리특례법','국가기술자격법','국가보안법','국민체육진흥법','국토의계획 및 이용에 관한법률','근로기준법','근로자 퇴직급여 보장법','낚시관리 및 육성법','노동조합 및 노동관계 조정법','농수산물유통 및 가격안정에 관한법률','농수산물의 원산지표시에 관한법률','농지법','대기환경보전법','대부업등의 등록 및 금융이용자보호에 관한법률','도로교통법','도로교통법(무면허운전)','도로교통법(사고후미조치)','도로교통법(음주운전)','도로교통법(음주측정거부)','도로법','도시및주거환경정비법','독점규제 및 공정거래에 관한법률','디자인보호법','마약류관리에 관한법률(대마)','마약류관리에 관한법률(마약)','마약류관리에 관한법률(향정)','물환경보전법','배타적경제수역에서의 외국인어업등에 관한 주권적권리의 행사에 관한법률','범죄수익 은닉의 규제 및 처벌등에 관한법률','변호사법','병역법','보조금관리에 관한법률','부동산실권리자 명의등기에 관한법률','부정경쟁방지 및 영업비밀 보호에 관한법률','부정수표단속법','사행행위 등 규제 및 처벌특례법','산림자원의 조성 및 관리에 관한법률','산업안전보건법','산지관리법','상표법','석유 및 석유대체연료사업법','선박안전법','선박직원법','성매매알선등 행위의 처벌에 관한법률','수도법','수산업법','수산자원관리법','스토킹범죄의처벌등에관한법률','식품위생법','신용정보의 이용 및 보호에 관한법률','아동·청소년의 성보호에 관한법률(성매수등)','아동·청소년의 성보호에 관한법률(음란물등)','아동·청소년의성보호에관한법률(성착취물등)','아동복지법','액화석유가스의 안전관리 및 사업법','약사법','여객자동차운수사업법','여신전문금융업법','영유아보육법','예비군법','옥외광고물등의 관리와 옥외광고산업진흥에 관한법률','외국환거래법','위험물안전관리법','유사수신행위의 규제에 관한법률','의료기기법','의료법','자동차관리법','자동차손해배상보장법','자본시장과 금융투자업에 관한법률','저작권법','전자금융거래법','전파법','정보통신망이용촉진 및 정보보호 등에 관한법률','조세범처벌법','주민등록법','주차장법','주택법','직업안정법','집회 및 시위에 관한법률','청소년보호법','총포·도검·화약류등의 안전관리에 관한법률','최저임금법','축산물위생관리법','출입국관리법','통신비밀보호법','특가법(도주차량)','특허법','폐기물관리법','풍속영업의 규제에 관한법률','하천법','학교보건법','학원의설립운영 및 과외교습에 관한법률','화물자동차 운수사업법','화재로 인한 재해보상과 보험가입에 관한법률','화재예방·소방시설설치유지 및 안전관리에 관한법률','화학물질관리법','기타특별법']
data6 = data6.loc[data6['C1_NM'].isin(incl)]

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
                 range_y=[100, 2500], range_x=[100000, 15000000],
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
st.plotly_chart(fig_bar, use_container_width=True)

st.title("연도별 지역 인구밀도 대비 범죄 발생률")
st.plotly_chart(fig, use_container_width=True)

st.write("Repository [link](https://github.com/masterfulEJ/DAnalytics_Proj.git)")
