import os
import replicate

replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

def generate_images(story_chunks):
    images = []

    for prompt in story_chunks:
        output = replicate_client.run(
            "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",  # SDXL
            input={"prompt": prompt}
        )
        images.append(output[0])  # First URL in list

    return images

