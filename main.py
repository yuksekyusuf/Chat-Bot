import openai
from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

chat_log = []

@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    chat_log.append({'role': 'user', 'content': user_input})
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        message = chat_log,
        temperature = 0.6
    )
    bot_response = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_response})
    return bot_response