from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_KEY')
model = ChatOpenAI(model='gpt-4o-mini',
                   api_key=api_key)

chat_history = [
    SystemMessage(content='you are a helpful assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)


print(chat_history) 