import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def plot_normal(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = stats.norm.pdf(x, mu, sigma)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
    st.plotly_chart(fig)

def plot_exponential(lambda_):
    x = np.linspace(0, 4/lambda_, 1000)
    y = stats.expon.pdf(x, scale=1/lambda_)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
    st.plotly_chart(fig)

def plot_poisson(lambda_):
    x = np.arange(0, 20)
    y = stats.poisson.pmf(x, lambda_)
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    st.plotly_chart(fig)

st.title("Визуализация распределений")

distribution = st.selectbox("Выберите распределение", ["Нормальное", "Экспоненциальное", "Пуассона"])

if distribution == "Нормальное":
    mu = st.slider("μ (среднее значение)", -10, 10, 0)
    sigma = st.slider("σ (стандартное отклонение)", 0.1, 10.0, 1.0)
    plot_normal(mu, sigma)

elif distribution == "Экспоненциальное":
    lambda_ = st.slider("λ (интенсивность)", 0.1, 10.0, 1.0)
    plot_exponential(lambda_)

elif distribution == "Пуассона":
    lambda_ = st.slider("λ (среднее число событий)", 0, 10, 1)
    plot_poisson(lambda_)

