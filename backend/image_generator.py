import os
import replicate

replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

def generate_images(story_chunks):
    images = []

    for prompt in story_chunks:
        output = replicate_client.run(
            "stability-ai/sdxl:8ab9d5c018148290b95ca7d94c640121be51dfb4641779aa0951f20a22c1111c",  # SDXL Turbo version
            input={"prompt": prompt}
        )
        images.append(output[0])  # First URL in list

    return images

