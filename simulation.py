import matplotlib.pyplot as plt
import numpy as np

# 데이터 설정
years = np.arange(2024, 2031)
investment = np.array([5000, 3000, 2000, 1500, 1000, 800, 500])  # 연간 투자비용 (백만원)
savings = np.array([1000, 2500, 3500, 4000, 4500, 5000, 5500])   # 연간 절감액 (백만원)
cumulative_savings = np.cumsum(savings - investment)              # 누적 순이익

# 그래프 스타일 설정
plt.style.use('seaborn')
plt.figure(figsize=(12, 8))

# 막대 그래프 생성
width = 0.35
plt.bar(years - width/2, investment, width, label='연간 투자비용', color='#FF9999')
plt.bar(years + width/2, savings, width, label='연간 절감액', color='#66B2FF')

# 누적 순이익 선 그래프
plt.plot(years, cumulative_savings, 'g-', label='누적 순이익', linewidth=2, marker='o')

# 그래프 커스터마이징
plt.title('RE100 투자 대비 수익 시뮬레이션 (2024-2030)', fontsize=15, pad=20)
plt.xlabel('연도', fontsize=12)
plt.ylabel('금액 (백만원)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# 축 설정
plt.xticks(years)
plt.ylim(bottom=min(min(investment), min(savings), min(cumulative_savings)) * 1.1,
        top=max(max(investment), max(savings), max(cumulative_savings)) * 1.1)

# 값 레이블 추가
for i, (inv, sav, cum) in enumerate(zip(investment, savings, cumulative_savings)):
   plt.text(years[i] - width/2, inv, f'{inv:,}', ha='center', va='bottom')
   plt.text(years[i] + width/2, sav, f'{sav:,}', ha='center', va='bottom')
   plt.text(years[i], cum, f'{cum:,}', ha='center', va='bottom')

# 손익분기점 표시
breakeven_year = None
for i, cum in enumerate(cumulative_savings):
   if cum >= 0 and breakeven_year is None:
       breakeven_year = years[i]
       plt.axvline(x=breakeven_year, color='red', linestyle='--', alpha=0.5)
       plt.text(breakeven_year, plt.ylim()[1], f'손익분기점\n({breakeven_year}년)',
               ha='center', va='bottom', color='red')

# 부가 설명 추가
plt.figtext(0.02, 0.02, 
          '* 가정:\n'
          '- 초기 설비 투자 및 연간 운영 비용 포함\n'
          '- 전력 비용 상승률 및 탄소 배출권 가격 반영\n'
          '- 정부 지원금 및 세제 혜택 포함',
          fontsize=8, ha='left')

plt.tight_layout()
plt.show()
