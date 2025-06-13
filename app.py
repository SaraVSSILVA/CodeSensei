# # Lógica de Programação:

# Importar as bibliotecas necessárias
# Criar mecanismos de integrar GPT com site (API)
# Criar a interface do úsuario
# Integrar o GPT com a interface do usuário.
# Testar a aplicação 

# Importa as bibliotecas necessárias
import google.generativeai as genai  # Biblioteca para a API do Gemini
import streamlit as st  # Biblioteca para criar a interface web

# Configura a chave de API do Gemini
genai.configure(api_key="SUA_CHAVE_GEMINI_AQUI")  # Substitua pela sua API Key

# Define o modelo correto da API Gemini
model = genai.GenerativeModel("gemini-1.5-pro")  # Ajustado para o modelo atualizado

# Função para gerar a resposta do professor virtual
def chat_professor(prompt):
    """
    Esta função recebe a pergunta do usuário, envia para o modelo Gemini e retorna a explicação gerada.
    """
    try:
        response = model.generate_content(prompt)  # Chama a API para obter a explicação
        return response.text  # Retorna o texto gerado pelo modelo
    except Exception as e:
        return f"❌ Erro ao obter resposta: {str(e)}"  # Retorna uma mensagem de erro se algo falhar

# Configuração inicial do Streamlit
st.set_page_config(page_title="CodeSensei", layout="wide")

# Exibe a logo no topo da interface
st.image("human.png", width=150)  # Substitua "logo.png" pelo nome do seu arquivo

# Estilização da interface com CSS para remover fundo branco
st.markdown(
    """
    <style>
        .big-title { font-size: 32px; font-weight: bold; text-align: center; color: #4CAF50; }
        .subtitle { font-size: 18px; text-align: center; color: #666; }
        .response-box { font-size: 16px; background-color: transparent; padding: 10px; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibição do título e descrição com estilos customizados
st.markdown('<p class="big-title">👨‍🏫 CodeSensei - Seu Professor de Lógica de Programação</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Faça perguntas e receba explicações detalhadas!</p>', unsafe_allow_html=True)

# Criação de colunas para organizar melhor os elementos
col1, col2 = st.columns([2, 1])  # Define proporção das colunas

# Caixa de entrada para perguntas do usuário
with col1:
    entrada = st.text_input("🔹 Digite sua pergunta sobre lógica de programação:")

# Sugestões rápidas de perguntas comuns
with col2:
    st.markdown("### 🎯 Sugestões de perguntas:")
    opcoes = ["O que é um algoritmo?", "Como funciona um loop?", "Qual a diferença entre variável e constante?"]
    sugestao = st.selectbox("Escolha uma sugestão:", opcoes)

# Garante que alguma pergunta será usada (manual ou sugerida)
pergunta_final = entrada if entrada else sugestao

# Processa a pergunta do usuário e exibe a resposta correta sem fundo branco
if pergunta_final:
    resposta = chat_professor(pergunta_final)  # Chama a função para obter resposta real
    st.markdown(
        f"""
        <div class="response-box">
            📘 {resposta}
        </div>
        """,
        unsafe_allow_html=True,
    )