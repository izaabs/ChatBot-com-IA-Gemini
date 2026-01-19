# 🤖 ChatBot com IA (Gemini)

Este projeto é um chatbot interativo desenvolvido em **Python + Streamlit**, utilizando a API do **Google Gemini** para conversar de forma dinâmica.  
A aplicação exibe o histórico de mensagens, mantém memória durante a sessão e permite uma experiência completa de chat diretamente no navegador.

---

## 🚀 Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini API)**
- **Google GenerativeModel**
- **Session State para memória de conversa**

---

## 🛠️ Instalação das dependências

Instale as bibliotecas necessárias:

```bash
pip install streamlit google-generativeai
```

## ▶️ Executar o projeto

No terminal, execute:

```bash
streamlit run maingemini.py
```

A aplicação abrirá automaticamente no navegador.

## 🔑 Configuração da API Key

No código, você encontrará:

```python
chave_api = "SUA_CHAVE_AQUI"
```

➡️ Substitua "SUA_CHAVE_AQUI" pela sua chave real da API para que o projeto funcione corretamente.

## 🧠 Como o projeto funciona

- O usuário envia uma mensagem pelo campo de chat  
- A mensagem é exibida na tela  
- Ela é salva em `st.session_state`  
- O modelo Gemini recebe a conversa inteira (histórico)  
- A IA responde e a resposta também é salva e exibida  
- A conversa se mantém durante toda a sessão  

## 📝 Licença

Este projeto está sob a licença **MIT**.  
Você pode usar, modificar e distribuir o código livremente, desde que mantenha o aviso de direitos autorais.

Consulte o arquivo `LICENSE` para mais detalhes.


