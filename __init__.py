from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura o modelo
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Cria o template do prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a PCD (Person with a Disability). Answer all questions about accessibility in a helpful and empathetic way."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Cria a chain (cadeia) combinando prompt + modelo
chain = prompt | model

# Lista para guardar a conversa
conversa = []

print("=== CHATBOT PCD ===")
print("Você pode fazer 3 perguntas. Digite 'sair' para parar antes.\n")

# Loop para 3 perguntas
for pergunta_num in range(1, 4):
    # Pede a pergunta do usuário
    print("==========================================")
    user_input = input(f"Pergunta {pergunta_num}/3: ")
    print("==========================================")

    # Se o usuário digitar 'sair', para o programa
    if user_input.lower() == 'sair':
        print("Tchau! ♿")
        break

    # Envia para o modelo usando o template
    response = chain.invoke({
        "input": user_input,
        "chat_history": conversa
    })

    # Adiciona as mensagens na conversa
    conversa.append(HumanMessage(content=user_input))
    conversa.append(AIMessage(content=response.content))

    # Mostra a resposta
    print(f"♿ PCD Bot: {response.content}\n")

    # Se foi a 3ª pergunta, avisa que acabou
    if pergunta_num == 3:
        print("=== FIM DO CHAT (3 perguntas respondidas) ===")

print("Programa finalizado! ♿")
