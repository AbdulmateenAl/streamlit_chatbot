from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3")

chain = prompt | model

# Define the context and the question
context = "LangChain is a framework for developing applications powered by language models. It is widely used for building custom chatbots, content generation tools, and knowledge management systems."
question = "How can LangChain be used to build a custom chatbot?"

response = chain.invoke({"context": context, "question": question})
print(response)
