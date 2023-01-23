### EDA ###
import numpy as np
import pandas as pd

### 파일 불러오기, 데이터프레임 생성 및 출력###
data = pd.read_csv('C:/Users/chlru/Downloads/archive/HR-Employee.csv')
df = pd.DataFrame(data)

print(df.head())

### 결측치, 이상치 검토 ###
# 결측치 검토 #
print(df.isnull().sum())

# 이상치 검토 #
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1





### 유의미한 시각화 5개 이상 ###

### 수치형 변수 간 상관관계 파악 ###

### 파생변수 생성 ###
