import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(layout="wide", page_title="RE100 시장 세그먼트")

# 데이터 설정
segments = ['중기업 제조업', '중기업 서비스업', '소기업 제조업', 
            '소기업 서비스업', '대기업 협력사', '공공기관', '기타']
sizes = [35, 25, 15, 10, 8, 5, 2]
colors = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d', '#ffc658']
explode = (0.1, 0.05, 0, 0, 0, 0, 0)  # 주요 세그먼트 강조

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 8))
plt.clf()  # Clear the current figure

# 파이 차트 생성
wedges, texts, autotexts = plt.pie(sizes,
                                  explode=explode,
                                  labels=segments,
                                  colors=colors,
                                  autopct='%1.1f%%',
                                  shadow=True,
                                  startangle=90,
                                  pctdistance=0.85)

# 중앙에 원 추가하여 도넛 차트 형태로 만들기
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# 텍스트 스타일 설정
plt.setp(autotexts, size=9, weight="bold")
plt.setp(texts, size=10)

# 제목 추가
plt.title("중소기업 맞춤형 RE100 로드맵 생성 AI\n목표 시장 세그먼트", 
          pad=20, 
          size=15, 
          weight='bold')

# 부가 설명 추가
plt.text(0, -1.3, "* 전체 목표 시장 규모: 약 10만개 기업 기준",
         ha='center',
         size=9,
         style='italic')

# 범례 추가
plt.legend(wedges, segments,
          title="시장 세그먼트",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.axis('equal')

# Streamlit에 그래프 표시
st.pyplot(fig)
