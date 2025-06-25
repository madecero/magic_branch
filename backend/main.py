from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from story_generator import generate_story
from image_generator import generate_images

from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    story_chunks = generate_story(data)
    images = generate_images(story_chunks)
    return {"pages": [{"text": s, "image": i} for s, i in zip(story_chunks, images)]}
