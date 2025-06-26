import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(data):
    name = data.get("name", "the child")
    age = data.get("age", 4)
    interests = ", ".join(data.get("interests", []))
    length = data.get("length", 5)

    system_prompt = (
        "You are a friendly storybook AI that creates short, vivid, age-appropriate stories for children. "
        "Generate exactly {length} story pages. Each page should be a clear and complete paragraph. "
        "Avoid headings like 'Page 1'. Do not leave any page empty. Each paragraph should be fun, simple, and imaginative."
        "The main character of the story is a child named {name} who is {age} years old and enjoys {interests}."
        "The child should get a sense that magic is real from the story."
    ).format(length=length, name=name, age=age, interests=interests)

    user_prompt = (
        f"Write a children's story for a {age}-year-old named {name} who enjoys {interests}. "
        f"Make the story {length} pages long. Each page should be a warm, engaging paragraph."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
    )

    full_story = response.choices[0].message.content or ""

    # Clean and split the story into non-empty paragraphs
    story_pages = [para.strip() for para in full_story.split("\n\n") if para.strip()]

    # Ensure the result has exactly the requested number of pages
    return story_pages[:length]
