# Estruturação 
    # titulo
    # input do chat
    # a cada mensagem enviada:
        # mostrar a mensagem que o usuario enviou no chat
        # enviar essa mensagem para a IA responder
        # aparece na tela a resposta da IA

import streamlit as st
import google.generativeai as genai

# Passo 1: Configurações Iniciais
    # Título da página
st.write("### ChatBot com IA (Gemini)")

    # Configurar a chave de acesso da IA
    # OBS: Em projetos reais, nunca deixe a chave exposta assim no código
chave_api = "SUA_CHAVE_AQUI"
genai.configure(api_key=chave_api)
modelo = genai.GenerativeModel('gemini-2.5-flash')

# Passo 2: Configurar a memória (Session State)
    # Criar lista vazia se não existir e garante que o histórico não apague a cada interação
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Passo 3: Carregar histórico de mensagens
       # Mostra na tela tudo que já foi conversado antes
for mensagem in st.session_state["lista_mensagens"]:
    # O Streamlit precisa de "assistant", mas o Google usa "model"
    role = mensagem["role"]
    if role == "model":
        role = "assistant"
    
    # O Google guarda texto em lista, pegamos o primeiro item
    content = mensagem["parts"][0]
    st.chat_message(role).write(content)

# Passo 4: Capturar mensagem do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # Passo 5: Processar mensagem e gerar resposta
        # Mostrar mensagem do usuário na tela
    st.chat_message("user").write(mensagem_usuario)
        # Salvar mensagem no formato do Google (parts=[texto])
    st.session_state["lista_mensagens"].append({"role": "user", "parts": [mensagem_usuario]})

    # Passo 6: Buscar a resposta da IA
        # start_chat carrega o histórico anterior
    chat = modelo.start_chat(history=st.session_state["lista_mensagens"][:-1])
            # send_message envia a pergunta atual
    resposta_modelo = chat.send_message(mensagem_usuario)
    resposta_ia = resposta_modelo.text

    # Passo 7: Exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
        # Salvar resposta da IA no formato do Google
    st.session_state["lista_mensagens"].append({"role": "model", "parts": [resposta_ia]})