### EDA ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### 파일 불러오기, 데이터프레임 생성 및 출력###
data = pd.read_csv('HR-Employee.csv')
df = pd.DataFrame(data)

### 데이터 확인 ###
print(df.head())
print(df.info())
print(df.describe())

### 결측치, 이상치 검토 ###

# 결측치 검토 #
print("결측치 검토\n", df.isnull().sum())

# 이상치 검토 #
def outlier(data, col):
    new_data = data[col]
    Q1 = np.quantile(data[col].values, 0.25)
    Q3 = np.quantile(data[col].values, 0.75)
    IQR = Q3 - Q1
    Low, High = Q1 - IQR*1.5, Q3 + IQR*1.5
     
    out_data = new_data[(new_data > High) | (new_data < Low)].index
    
    print("{}: {}".format(col, len(out_data)))

def detection(column_list):
    for col in df.columns:
        if df[col].dtypes != 'object':
            column_list.append(col)
            
    print("\n이상치 개수")
    for col in column_list:
        outlier(df, col)

num_col = []
detection(num_col)

## 이상치 데이터가 분포한 columns: MonthlyIncome, NumCompaniesWorked,
## PerformanceRating, StockOptionLevel, TotalWorkingYears,
## TrainingTimesLastYear, YearsAtCompany, YearsInCurrentRole,
## YearsSinceLastPromotion, YearsWithCurrManager

### 수치형 변수 간 상관관계 파악 ###
num_df = df[num_col]

plt.figure(figsize=(13,13))
sns.heatmap(num_df.corr(), annot=True, 
fmt = '.2f', linewidths=.1, cmap='Blues')
plt.show()

### 유의미한 시각화 5개 이상 ###
## 수치형 상관관계에서 관련성이 0.6 이상으로 높은 5개의 Years 데이터로 시각화 ##
Years = ['YearsAtCompany', 'YearsInCurrentRole', 
'YearsSinceLastPromotion', 'YearsWithCurrManager', 
'TotalWorkingYears']

Years_df = num_df[Years]

## Visualization 1.histogram ##
plt.figure(figsize=(10, 10))
plt.hist(Years_df)
plt.grid()
plt.show()

# 0~5 사이에 데이터가 높게 분포되어 있음, 분포된 데이터의 개수를 알기 쉬움 #

## Visualization 2.Kernel Density plot ##
Years_df.plot.kde()
plt.show()

# YearsSinceLastPromotion column에서의 분포가 Skew함, 히스토그램보다 시각적인 분포 확인이 뚜렷함 #

## Visualization 3.Box plot ##
plt.figure(figsize=(12, 12))
Years_df.boxplot()

# 각 column마다 이상치 값들이 여러 분포해 있음 , 평균, 중앙값, 이상치 등 확인이 쉬움 #
 
## Visualization 4.Scatter plot ##
# YearsAtCompany에 대한 선형관계 #
df.plot(x=Years[0], y=Years[1], kind='scatter')
plt.show()

df.plot(x=Years[0], y=Years[2], kind='scatter')
plt.show()

df.plot(x=Years[0], y=Years[3], kind='scatter')
plt.show()

df.plot(x=Years[0], y=Years[4], kind='scatter')
plt.show()

# 전체적으로 비례관계를 보임 #

## Visualization 5.histogram for Age ##
plt.figure(figsize=(10, 10))
plt.hist(df['Age'])
plt.grid()
plt.show()

# 직장인의 나이가 30 ~ 40대의 사람들이 주로 분포해 있음 #

### 파생변수 생성 ###
## 월 소득에서의 달러를 환율을 통해 한화로 변환 ##
## 세금 공제를 한 실 수령액을 나타내는 Column 생성 ##

# 환율: 1달러 = 1200원, 세금: 15% #
ExchangeRate = 1200
Tax = 0.15

df['RealMonthlyIncomeWon'] = df['MonthlyIncome'] * ExchangeRate * (1-Tax)
print("\n실수령액\n", df['RealMonthlyIncomeWon'])