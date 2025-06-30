import os
from dotenv import load_dotenv
import torch

load_dotenv()
from diffusers import DiffusionPipeline

HF_TOKEN = os.getenv("HF_TOKEN")

pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/sdxl-turbo",
    use_auth_token=HF_TOKEN,
    torch_dtype=torch.float32
)
pipe.to("cuda" if pipe.device.type == "cuda" else "cpu")

def generate_images(story_chunks):
    images = []
    for chunk in story_chunks:
        image_prompt = f"Children's book illustration: {chunk[:200]}"
        result = pipe(image_prompt, num_inference_steps=4, guidance_scale=0.0)
        image = result.images[0]
        # Save image to a file and return the path, or encode as base64 if needed
        image_path = f"/tmp/{hash(chunk)}.png"
        image.save(image_path)
        images.append(image_path)
    return images