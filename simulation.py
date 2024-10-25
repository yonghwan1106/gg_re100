import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(layout="wide", page_title="RE100 ROI 시뮬레이션")

# 데이터 설정
years = np.arange(2024, 2031)
investment = np.array([5000, 3000, 2000, 1500, 1000, 800, 500])  # 연간 투자비용 (백만원)
savings = np.array([1000, 2500, 3500, 4000, 4500, 5000, 5500])   # 연간 절감액 (백만원)
cumulative_savings = np.cumsum(savings - investment)              # 누적 순이익

# 새로운 figure 생성
fig, ax = plt.subplots(figsize=(12, 8))

# 막대 그래프 생성
width = 0.35
ax.bar(years - width/2, investment, width, label='연간 투자비용', color='#FF9999')
ax.bar(years + width/2, savings, width, label='연간 절감액', color='#66B2FF')

# 누적 순이익 선 그래프
ax.plot(years, cumulative_savings, 'g-', label='누적 순이익', linewidth=2, marker='o')

# 그래프 커스터마이징
ax.set_title('RE100 투자 대비 수익 시뮬레이션 (2024-2030)', fontsize=15, pad=20)
ax.set_xlabel('연도', fontsize=12)
ax.set_ylabel('금액 (백만원)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.7)

# 축 설정
ax.set_xticks(years)
ax.set_ylim(bottom=min(min(investment), min(savings), min(cumulative_savings)) * 1.1,
            top=max(max(investment), max(savings), max(cumulative_savings)) * 1.1)

# 값 레이블 추가
for i, (inv, sav, cum) in enumerate(zip(investment, savings, cumulative_savings)):
    ax.text(years[i] - width/2, inv, f'{inv:,}', ha='center', va='bottom')
    ax.text(years[i] + width/2, sav, f'{sav:,}', ha='center', va='bottom')
    ax.text(years[i], cum, f'{cum:,}', ha='center', va='bottom')

# 손익분기점 표시
breakeven_year = None
for i, cum in enumerate(cumulative_savings):
    if cum >= 0 and breakeven_year is None:
        breakeven_year = years[i]
        ax.axvline(x=breakeven_year, color='red', linestyle='--', alpha=0.5)
        ax.text(breakeven_year, ax.get_ylim()[1], f'손익분기점\n({breakeven_year}년)',
                ha='center', va='bottom', color='red')

# 부가 설명 추가
fig.text(0.02, 0.02, 
         '* 가정:\n'
         '- 초기 설비 투자 및 연간 운영 비용 포함\n'
         '- 전력 비용 상승률 및 탄소 배출권 가격 반영\n'
         '- 정부 지원금 및 세제 혜택 포함',
         fontsize=8, ha='left')

# 레이아웃 조정
plt.tight_layout()

# Streamlit에 그래프 표시
st.pyplot(fig)

# 추가 설명
st.markdown("""
### 투자 수익 분석
- **초기 투자비용**: 첫 해에 가장 큰 투자(50억원)가 필요하며, 점진적으로 감소
- **연간 절감액**: 시간이 지날수록 증가하여 최종적으로 연 55억원의 절감 효과
- **손익분기점**: {}년에 도달
- **7년차 누적 순이익**: {:,}백만원
""".format(breakeven_year, cumulative_savings[-1]))

# 주요 지표 표시
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="총 투자비용", value=f"{investment.sum():,}백만원")
with col2:
    st.metric(label="총 절감액", value=f"{savings.sum():,}백만원")
with col3:
    st.metric(label="순이익", value=f"{cumulative_savings[-1]:,}백만원")
