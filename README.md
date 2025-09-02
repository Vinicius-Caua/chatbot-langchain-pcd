# Chatbot PCD ♿

Breve projeto de chatbot com tema PCD (acessibilidade). Usa LangChain core + provedor Groq por padrão; tem prompt sistemático, histórico de mensagens e resumo final após 3 perguntas.

## Conteúdo do repositório

- [**init**.py](d:\Programacao\Backend\Python\chatBot__init__.py) — código principal (inicializa o modelo, roda loop de 3 perguntas, gera resumo).
- [.env.example](d:\Programacao\Backend\Python\chatBot.env.example) — variáveis de ambiente de exemplo.
- [.gitignore](d:\Programacao\Backend\Python\chatBot.gitignore) — arquivos ignorados pelo git.

## Visão geral técnica (foco IA)

- O projeto inicializa um cliente de modelo via [`init_chat_model`](d:\Programacao\Backend\Python\chatBot__init__.py).
- Conversas são representadas por objetos estruturados: [`HumanMessage`](d:\Programacao\Backend\Python\chatBot__init__.py) e [`AIMessage`](d:\Programacao\Backend\Python\chatBot__init__.py).
- O prompt é construído usando [`ChatPromptTemplate`](d:\Programacao\Backend\Python\chatBot__init__.py) com um `MessagesPlaceholder` para o histórico.  
  Fluxo: template (system + histórico + pergunta) → modelo → resposta.
- Há uma segunda chain (`summary_chain`) que recebe o histórico e pede ao modelo um resumo final das 3 perguntas/respostas.

## Requisitos

- Python 3.10+ recomendado
- Pacotes (exemplos):
  - groq
  - langchain
  - langchain-core
  - python-dotenv

Exemplo de instalação:

```bash
pip install groq langchain langchain-core python-dotenv
```

(Se for usar Ollama local, instale Ollama separadamente: https://ollama.com/download e `pip install ollama`.)

## Configuração (.env)

Crie um arquivo `.env` na raiz (baseie-se em [.env.example](d:\Programacao\Backend\Python\chatBot.env.example)):

```
LANGCHAIN_API_KEY= your_langchain_api_key_here
GROQ_API_KEY= your_groq_api_key_here
```

- O código chama `load_dotenv()` para carregar essas variáveis.
- As keys estão presentes nos sites correspondentes: [LangChain](https://smith.langchain.com/settings?_gl=1*rizbte*_gcl_au*MTQyMDYyNjk4Ni4xNzU2NDI0MTcx*_ga*MzgxMTc1MTc4LjE3NTY0MjQxNzE.*_ga_47WX3HKKY2*czE3NTY4NTUwNjgkbzQkZzEkdDE3NTY4NTUxMDQkajI0JGwwJGgw), [Groq](https://console.groq.com/keys).

## Como rodar (Windows)

1. Crie um ambiente virtual:

```powershell
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt  
```

2. Execute:

```powershell
.\env\Scripts\python.exe __init__.py
```

O script permite até 3 perguntas no loop e depois imprime o resumo final.

## Como o chatbot funciona (resumido)

1. Usuário digita pergunta (input).
2. Código monta o prompt: system message (regras) + histórico (HumanMessage / AIMessage) + pergunta atual.
3. Passa tudo ao modelo via `chain.invoke({...})`. O modelo responde com texto em `response.content`.
4. Histórico é atualizado com `HumanMessage(content=...)` e `AIMessage(content=...)`.
5. Após 3 perguntas, `summary_chain` recebe o mesmo histórico e pede um resumo em bullets; o resultado é impresso.

## Dicas e resolução de problemas

- Se não aparecer saída: verifique se você está imprimindo `response.content`.
- Erro de importação (pylance): confirme pacotes instalados no mesmo interpreter do projeto.
- Prompt multilinha: use triple-quoted string (`"""..."""`) para evitar quebras inesperadas.
- `chat_history` deve ser lista de objetos `HumanMessage`/`AIMessage`, NÃO strings.
