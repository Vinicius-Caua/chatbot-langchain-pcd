from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura o tracing do LangSmith
os.environ["LANGSMITH_TRACING"] = "true"
model = init_chat_model("llama3-8b-8192", model_provider="groq")

response = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

print(response)