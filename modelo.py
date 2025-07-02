import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib  # <- para salvar o modelo

def treinar_modelo():
    # Lê os dados do arquivo CSV
    df = pd.read_csv('dados.csv')

    # Separa as variáveis independentes e dependente
    X = df[['mes', 'investimento_marketing']]
    y = df['vendas']

    # Treina o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Salva o modelo treinado em um arquivo .pkl
    joblib.dump(modelo, 'modelo_vendas.pkl')

    return modelo

# Isso garante que o modelo seja treinado se você rodar o script diretamente
if __name__ == "__main__":
    treinar_modelo()
