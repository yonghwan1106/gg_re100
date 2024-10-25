import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(layout="wide", page_title="RE100 Market Segments")

# 기본 폰트 설정
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 데이터 설정 (영문으로 변경)
segments = ['Medium Manufacturing', 'Medium Service', 'Small Manufacturing', 
            'Small Service', 'Large Corp. Partners', 'Public Org.', 'Others']
sizes = [35, 25, 15, 10, 8, 5, 2]
colors = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d', '#ffc658']
explode = (0.1, 0.05, 0, 0, 0, 0, 0)

# 기존 플롯 초기화
plt.clf()

# 새로운 figure 생성
fig, ax = plt.subplots(figsize=(12, 8))

# 파이 차트 생성
wedges, texts, autotexts = ax.pie(sizes,
                                 explode=explode,
                                 labels=segments,
                                 colors=colors,
                                 autopct='%1.1f%%',
                                 shadow=True,
                                 startangle=90,
                                 pctdistance=0.85)

# 중앙에 원 추가하여 도넛 차트 형태로 만들기
centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(centre_circle)

# 텍스트 스타일 설정
plt.setp(autotexts, size=9, weight="bold")
plt.setp(texts, size=10)

# 제목 추가
ax.set_title("RE100 Roadmap Generation AI\nTarget Market Segments", 
             pad=20, 
             size=15, 
             weight='bold')

# 부가 설명 추가
ax.text(0, -1.3, "* Total target market size: Based on 100,000 companies",
        ha='center',
        size=9,
        style='italic')

# 범례 추가
ax.legend(wedges, segments,
         title="Market Segments",
         loc="center left",
         bbox_to_anchor=(1, 0, 0.5, 1))

# 레이아웃 조정
plt.tight_layout()

# Streamlit에 그래프 표시
st.pyplot(fig)

# 한글 텍스트를 Streamlit의 텍스트 요소로 추가
st.markdown("""
### 시장 세그먼트 설명:
- 중기업 제조업 (Medium Manufacturing): 35%
- 중기업 서비스업 (Medium Service): 25%
- 소기업 제조업 (Small Manufacturing): 15%
- 소기업 서비스업 (Small Service): 10%
- 대기업 협력사 (Large Corp. Partners): 8%
- 공공기관 (Public Org.): 5%
- 기타 (Others): 2%
""")
