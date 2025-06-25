import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(data):
    prompt = f"Write a children’s story for a {data['age']}-year-old about {', '.join(data['interests'])}. Include {data['length']} pages. Use simple, warm language appropriate for a child."
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly storybook AI that creates fun, age-appropriate stories for children."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )

    full_story = response.choices[0].message.content
    return full_story.split("\n\n")[:data["length"]]


