from langchain_community.llms import Ollama
llm = Ollama(model="llama3")
llm.invoke("Tell me a joke")