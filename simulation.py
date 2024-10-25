import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="RE100 ROI Simulation")

# Matplotlib 설정
plt.style.use('default')
plt.rc('font', family='DejaVu Sans')  # Streamlit Cloud에서 지원하는 기본 폰트 사용
plt.rc('axes', unicode_minus=False)    # 마이너스 기호 깨짐 방지

# 영문 레이블 정의 (한글 대체)
labels = {
    'title': 'RE100 Investment and Return Simulation (2024-2030)',
    'investment': 'Annual Investment',
    'savings': 'Annual Savings',
    'cumulative': 'Cumulative Profit',
    'year': 'Year',
    'amount': 'Amount (Million KRW)',
    'breakeven': 'Break-even Point'
}

# 데이터 설정
years = np.arange(2024, 2031)
investment = np.array([5000, 3000, 2000, 1500, 1000, 800, 500])
savings = np.array([1000, 2500, 3500, 4000, 4500, 5000, 5500])
cumulative_savings = np.cumsum(savings - investment)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 8))

# 막대 그래프
width = 0.35
bar1 = ax.bar(years - width/2, investment, width, label=labels['investment'], color='#FF9999')
bar2 = ax.bar(years + width/2, savings, width, label=labels['savings'], color='#66B2FF')

# 누적 순이익 선 그래프
line = ax.plot(years, cumulative_savings, 'g-', label=labels['cumulative'], linewidth=2, marker='o')

# 그래프 스타일링
ax.set_title(labels['title'], fontsize=15, pad=20)
ax.set_xlabel(labels['year'], fontsize=12)
ax.set_ylabel(labels['amount'], fontsize=12)
ax.legend(fontsize=10, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.7)

# 축 설정
ax.set_xticks(years)
ax.set_ylim(bottom=min(min(investment), min(savings), min(cumulative_savings)) * 1.1,
            top=max(max(investment), max(savings), max(cumulative_savings)) * 1.1)

# 값 레이블 추가
for i, v in enumerate(investment):
    ax.text(years[i] - width/2, v, f'{int(v):,}', ha='center', va='bottom')

for i, v in enumerate(savings):
    ax.text(years[i] + width/2, v, f'{int(v):,}', ha='center', va='bottom')

for i, v in enumerate(cumulative_savings):
    ax.text(years[i], v, f'{int(v):,}', ha='center', va='bottom')

# 손익분기점 표시
breakeven_year = None
for i, cum in enumerate(cumulative_savings):
    if cum >= 0 and breakeven_year is None:
        breakeven_year = years[i]
        ax.axvline(x=breakeven_year, color='red', linestyle='--', alpha=0.5)
        ax.text(breakeven_year, ax.get_ylim()[1], f'{labels["breakeven"]}\n({breakeven_year})',
                ha='center', va='bottom', color='red')

plt.tight_layout()

# Streamlit에 그래프 표시
st.pyplot(fig)

# 한글 설명은 Streamlit markdown으로 제공
st.markdown("""
### 투자 수익 분석
- **초기 투자비용**: 첫 해에 가장 큰 투자(50억원)가 필요하며, 점진적으로 감소
- **연간 절감액**: 시간이 지날수록 증가하여 최종적으로 연 55억원의 절감 효과
- **손익분기점**: {}년에 도달
- **7년차 누적 순이익**: {:,}백만원
""".format(breakeven_year, cumulative_savings[-1]))

# 주요 지표
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="총 투자비용", value=f"{investment.sum():,}백만원")
with col2:
    st.metric(label="총 절감액", value=f"{savings.sum():,}백만원")
with col3:
    st.metric(label="순이익", value=f"{cumulative_savings[-1]:,}백만원")
