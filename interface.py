import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from modelo import treinar_modelo
from PIL import Image

# Modelo treinado
modelo = treinar_modelo()

# Logo
st.set_page_config(page_title="SameFind Previsor de Vendas", page_icon="🦈", layout="centered")

# Apresentação
st.markdown("<h1 style='text-align: center; color: #00BFFF;'>🔮🦈 SameFind </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Previsor de Vendas Inteligente</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Preveja vendas com base no mês e investimento em marketing</p>", unsafe_allow_html=True)

# Exibe logo
try:
    logo = Image.open("logo.png")
    st.image("logo.png", use_container_width=True)

except:
    st.warning("Adicione sua logo como 'logo.png' na pasta do projeto.")

# Entradas do usuário
col1, col2 = st.columns(2)
with col1:
    mes = st.number_input("📆 Mês (1 a 12)", min_value=1, max_value=12, step=1)
with col2:
    investimento = st.number_input("💰 Investimento em Marketing (R$)", min_value=0.0, step=100.0)

if st.button("📈 Prever Vendas"):
    entrada = [[mes, investimento]]
    pred = modelo.predict(entrada)[0]

    # Dados reais + previsões
    df = pd.read_csv('dados.csv')
    X = df[['mes', 'investimento_marketing']]
    df['previsao'] = modelo.predict(X)

    nova_linha = pd.DataFrame({'mes': [mes], 'vendas': [None], 'previsao': [pred]})
    df_plot = pd.concat([df, nova_linha], ignore_index=True)

    # Gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_plot['mes'], y=df_plot['vendas'],
                             mode='lines+markers', name='Vendas Reais', line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=df_plot['mes'], y=df_plot['previsao'],
                             mode='lines+markers', name='Previsão', line=dict(color='orange', dash='dash')))
    fig.update_layout(title="📊 Vendas Reais vs Previsão",
                      xaxis_title="Mês",
                      yaxis_title="Vendas (R$)",
                      template="plotly_white")

    st.success(f"🧾 Previsão de vendas: R$ {pred:,.2f}")
    st.plotly_chart(fig, use_container_width=True)
