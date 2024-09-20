import os
import openai
from dotenv import load_dotenv

# Завантаження змінних середовища з файлу .env
load_dotenv()

# Отримання API ключа з .env файлу
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(prompt):
    try:
        # Використання методу 'create' для запиту до API ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while communicating with the OpenAI API."











