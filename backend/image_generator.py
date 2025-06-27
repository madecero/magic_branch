import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_images(story_chunks):
    images = []
    for chunk in story_chunks:
        image_prompt = f"Children's book illustration: {chunk[:200]}"
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            n=1,
            size="1024x1024",  # or "512x512"
            quality="standard"
        )
        
        image_url = response.data[0].url
        images.append(image_url)
    
    return images

