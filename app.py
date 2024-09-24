import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 修改后的路径，使用其中一种方法
df = pd.read_csv(r'C:\Users\97854\Desktop\刘天翔\西南财经大学\大三上\机器学习\MISY331-Fall-2024-MIS\house_Assignment\housing\housing.csv')

st.title('California Housing Data (1990) by Joy Liu')

# 添加价格滑动条
price_slider = st.slider('Minimal Median House Value:', 200000, 500001, 200000)

# 添加侧边栏中的多选过滤器
location_type = st.sidebar.multiselect(
    'Choose the location type',
    df['ocean_proximity'].unique(),  # 位置选项
    df['ocean_proximity'].unique()  # 默认选项
)

# 添加侧边栏中的单选按钮过滤器
income_level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High')
)

# 根据收入等级过滤数据
if income_level == 'Low':
    df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    df = df[df['median_income'] >= 4.5]

# 根据位置类型过滤数据
df = df[df['ocean_proximity'].isin(location_type)]

# 根据价格过滤数据
df = df[df['median_house_value'] >= price_slider]

# 在地图上显示数据
st.map(df)

# 显示房价直方图
plt.style.use("seaborn-v0_8")
st.subheader('Distribution of Median House Value')
fig, ax = plt.subplots()
df['median_house_value'].hist(bins=30, ax=ax)  # 使用30个bins显示直方图
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
st.pyplot(fig)

# 显示数据表格
st.subheader('Filtered Data')
st.write(df)
