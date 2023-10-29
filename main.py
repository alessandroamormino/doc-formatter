import os
import openai

# Leggo la API KEY di OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Definisco l'input
content = "E' nato prima l'uovo o la gallina?"

response = chat_completion = openai.ChatCompletion.create(
	model="gpt-3.5-turbo", 
	messages=[
		{"role": "user", "content": content}
	]
)

print(response['choices'][0]['message']['content'])