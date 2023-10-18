import streamlit as st
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = sns.load_dataset("tips")

st.write('### Задание 4: Нарисуйте гистограмму total_bill')

fig = px.histogram(tips, x='total_bill', nbins=50)
fig.update_xaxes(title='Cумма счета')
fig.update_yaxes(title='Частота')
fig.update_layout(title='Гистограмма total_bill', title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 5: Нарисуйте scatterplot, показывающий связь между total_bill and tip')
fig = px.scatter(tips, x='total_bill', y='tip')
fig.update_xaxes(title="Сумма счета (total_bill)")
fig.update_yaxes(title="Чаевые (tip)")
fig.update_traces(marker=dict(size=5))
fig.update_layout(title='Связь между total_bill и tip', title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 7. Нарисуйте 1 график, связывающий total_bill, tip, и size')
fig = px.scatter(tips, x='total_bill', y='tip', color='size')
fig.update_xaxes(title="Сумма счета (total_bill)")
fig.update_yaxes(title="Чаевые (tip)")
fig.update_layout(title='Связь между total_bill, tip и размером (size)', title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 8. Покажите связь между днем недели и размером счета')
fig = px.box(tips, x='day', y='total_bill', color='day', points=False)
fig.update_xaxes(title="День недели")
fig.update_yaxes(title="Сумма счета (total_bill)")
fig.update_layout(title="Связь между днем недели и размером счета", title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 9. Нарисуйте scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу')
fig = px.scatter(tips, x='tip', y='day', color='sex', color_discrete_map={'Male': 'blue', 'Female': 'red'})
fig.update_xaxes(title="Чаевые")
fig.update_yaxes(title="День недели")
fig.update_layout(title="Cвязь между полом, днем недели и размером оставленных чаевых", title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 10. Нарисуйте box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)')
fig = px.box(tips, x='day', y='total_bill', color='time',
             title="Связь между днем недели и суммой счета, разбитой по времени",
             labels={'day': 'День недели', 'total_bill': 'Сумма счета (total_bill)', 'time': 'Время'},
             color_discrete_sequence=['#FF5733', '#33FF56'])
fig.update_layout(title="Связь между днем недели и суммой счета, разбитой по времени", title_x=0.25)
st.plotly_chart(fig)

st.write('### Шаг 11. Нарисуйте 2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали.')
lunch_data = tips[tips['time'] == 'Lunch']
dinner_data = tips[tips['time'] == 'Dinner']
fig_lunch = go.Figure(data=[go.Histogram(x=lunch_data['tip'], nbinsx=30, name='Ланч')],
                      layout=go.Layout(title='Гистограмма чаевых на ланч', title_x=0.25,
                                       xaxis=dict(title='Чаевые'),
                                       yaxis=dict(title='Частота')))
fig_lunch.update_layout(width=400, height=400)
fig_dinner = go.Figure(data=[go.Histogram(x=dinner_data['tip'], nbinsx=20, name='Ужин')],
                       layout=go.Layout(title='Гистограмма чаевых на ужин', title_x=0.25,
                                        xaxis=dict(title='Чаевые'),
                                        yaxis=dict(title='Частота')))
fig_dinner.update_layout(width=400, height=400)
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_lunch)
with col2:
    st.plotly_chart(fig_dinner)

st.write('### Шаг 12. Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.')
fig_male = plt.figure(figsize=(5, 5))
sns.scatterplot(data=tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'Yes')], x='total_bill', y='tip', hue='smoker', legend=False)
sns.scatterplot(data=tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'No')], x='total_bill', y='tip', hue='smoker')
plt.xlabel('Сумма счета')
plt.ylabel('Сумма чаевых')
plt.title('Мужчины')
plt.tight_layout()
fig_female = plt.figure(figsize=(5, 5))
sns.scatterplot(data=tips[(tips['sex'] == 'Female') & (tips['smoker'] == 'Yes')], x='total_bill', y='tip', hue='smoker', legend=False)
sns.scatterplot(data=tips[(tips['sex'] == 'Female') & (tips['smoker'] == 'No')], x='total_bill', y='tip', hue='smoker')
plt.xlabel('Сумма счета')
plt.ylabel('Сумма чаевых')
plt.title('Женщины')
plt.tight_layout()
col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig_male)
with col2:
    st.pyplot(fig_female)


st.write('### Шаг 12. А теперь интерактивные')
fig_male = px.scatter(tips[(tips['sex'] == 'Male')], x='total_bill', y='tip', color='smoker',
                      labels={'total_bill': 'Сумма счета', 'tip': 'Сумма чаевых'})
fig_male.update_xaxes(title="Сумма счета (total_bill)")
fig_male.update_yaxes(title="Сумма чаевых (tip)")
fig_male.update_layout(title='Мужчины', title_x=0.35,width=400, height=400)

fig_female = px.scatter(tips[(tips['sex'] == 'Female')], x='total_bill', y='tip', color='smoker',
                      labels={'total_bill': 'Сумма счета', 'tip': 'Сумма чаевых'})
fig_female.update_xaxes(title="Сумма счета (total_bill)")
fig_female.update_yaxes(title="Сумма чаевых (tip)")
fig_female.update_layout(title='Женщины', title_x=0.35, width=400, height=400)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_male.update_layout(legend=dict(x=0, y=1)))
with col2:
     st.plotly_chart(fig_female.update_layout(legend=dict(x=0, y=1)))
