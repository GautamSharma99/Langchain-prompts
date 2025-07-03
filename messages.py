from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage    
import os

load_dotenv()
api_key = os.getenv('OPENAI_KEY')

model = ChatOpenAI(api_key=api_key,
                   model='gpt-4o-mini')

messages= [
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='tell me about langchain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)


