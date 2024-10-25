import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import platform
from matplotlib import font_manager, rc

# 운영체제별 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':  # Mac
    plt.rc('font', family='AppleGothic')
else:  # Linux
    plt.rc('font', family='NanumGothic')
    
# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 페이지 설정
st.set_page_config(layout="wide", page_title="RE100 ROI Simulation")

# 데이터 설정
years = np.arange(2024, 2031)
investment = np.array([5000, 3000, 2000, 1500, 1000, 800, 500])  # 연간 투자비용 (백만원)
savings = np.array([1000, 2500, 3500, 4000, 4500, 5000, 5500])   # 연간 절감액 (백만원)
cumulative_savings = np.cumsum(savings - investment)              # 누적 순이익

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

# 막대 그래프
width = 0.35
bar1 = ax.bar(years - width/2, investment, width, label='연간 투자비용', color='#FF9999')
bar2 = ax.bar(years + width/2, savings, width, label='연간 절감액', color='#66B2FF')

# 누적 순이익 선 그래프
line = ax.plot(years, cumulative_savings, 'g-', label='누적 순이익', linewidth=2, marker='o')

# 그래프 스타일링
ax.set_title('RE100 투자 대비 수익 시뮬레이션 (2024-2030)', fontsize=15, pad=20)
ax.set_xlabel('연도', fontsize=12)
ax.set_ylabel('금액 (백만원)', fontsize=12)
ax.legend(fontsize=10, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.7)

# 축 설정
ax.set_xticks(years)
ax.set_ylim(bottom=min(min(investment), min(savings), min(cumulative_savings)) * 1.1,
            top=max(max(investment), max(savings), max(cumulative_savings)) * 1.1)

# 값 레이블 추가
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom')

add_value_labels(bar1)
add_value_labels(bar2)

# 누적 순이익 값 표시
for i, v in enumerate(cumulative_savings):
    ax.text(years[i], v, f'{int(v):,}', ha='center', va='bottom')

# 손익분기점 표시
breakeven_year = None
for i, cum in enumerate(cumulative_savings):
    if cum >= 0 and breakeven_year is None:
        breakeven_year = years[i]
        ax.axvline(x=breakeven_year, color='red', linestyle='--', alpha=0.5)
        ax.text(breakeven_year, plt.ylim()[1], f'손익분기점\n({breakeven_year}년)',
                ha='center', va='bottom', color='red')

plt.tight_layout()

# Streamlit에 그래프 표시
st.pyplot(fig)

# requirements.txt 추가 필요:
# matplotlib==3.9.2
# numpy==2.1.2
# streamlit==1.39.0
# korean-fonts
