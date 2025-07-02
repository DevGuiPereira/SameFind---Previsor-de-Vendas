# 🔮🦈 SameFind - Previsor de Vendas

Projeto de Inteligência Artificial desenvolvido para prever o volume de vendas de uma empresa com base no mês e no investimento em marketing, de forma simples, visual e interativa.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é aplicar técnicas de **regressão linear** para estimar as vendas de uma empresa, considerando o mês do ano e o valor investido em marketing como variáveis preditoras. A solução conta com uma interface interativa construída com **Streamlit**, permitindo que o usuário insira valores e visualize as previsões de forma gráfica e intuitiva.

---

## 🛠 Tecnologias e Ferramentas Utilizadas

- **Python** — Linguagem principal do projeto  
- **Pandas** — Manipulação de dados  
- **Scikit-Learn** — Treinamento do modelo de regressão linear  
- **Joblib** — Salvamento do modelo treinado  
- **Streamlit** — Criação da interface interativa  
- **Plotly** — Gráficos interativos para visualização dos resultados  
- **Gradio** — [Listada no requirements, mas não utilizada diretamente no código atual]  

---

## ⚙️ Descrição do Funcionamento

O projeto é composto por duas partes principais:

1. **Treinamento do Modelo**  
   - Os dados históricos são carregados a partir do arquivo `dados.csv`.  
   - As variáveis utilizadas são:  
     - `mes` → Mês do ano (1 a 12)  
     - `investimento_marketing` → Valor investido em marketing (R$)  
     - `vendas` → Valor real das vendas (R$)  
   - Um modelo de regressão linear é treinado para prever as vendas com base nas variáveis.  
   - O modelo treinado é salvo no arquivo `modelo_vendas.pkl`.  

2. **Interface Interativa (Streamlit)**  
   - O usuário informa o mês e o investimento previsto.  
   - O modelo realiza a previsão de vendas.  
   - Um gráfico interativo compara as vendas reais (histórico) com as previsões.  
   - A interface exibe o valor previsto e o gráfico atualizado.  

---

## ▶️ Como Executar/Testar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python** instalado e o gerenciador de pacotes **pip**.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Instale as Dependencias:
   ```bash
   pip install -r requirements.txt

3. Execute no Sistema:
   ```bash
   streamlit run interface.py

⚠️ Importante: Certifique-se de que o arquivo dados.csv esteja na pasta do projeto. Para personalizar o visual, você pode adicionar sua logo com o nome logo.png.

---

👨‍💻 Autores
- Bruno Vinicius Rezende
- Carlos Junior
- Guilherme Reis Pereira
- Kawan Aureliano
