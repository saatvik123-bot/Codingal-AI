import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

MODELS = [
    "stabilityai/stable-diffusion-3-medium-diffusers",
    "ByteDance/SDXL-Lightning",
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-xl-base-1.0",
]

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Accept": "image/png"
}


def generate_image_from_text(prompt):
    """Generate an image using Hugging Face inference with fallback models."""
    payload = {"inputs": prompt}
    last_err = None

    for model in MODELS:
        url = f"https://router.huggingface.co/hf-inference/models/{model}"

        for _ in range(3):  # retry loop
            try:
                r = requests.post(url, headers=HEADERS, json=payload, timeout=120)
                ct = (r.headers.get("content-type") or "").lower()

                # Model loading wait
                if r.status_code == 503 and "application/json" in ct:
                    try:
                        wait_s = int(r.json().get("estimated_time", 5))
                    except Exception:
                        wait_s = 5
                    time.sleep(wait_s + 1)
                    continue

                # Success → return image
                if r.status_code == 200 and "application/json" not in ct:
                    try:
                        return Image.open(BytesIO(r.content)).convert("RGB")
                    except Exception as e:
                        last_err = f"Decode error: {e}"
                        break

                # Error response
                try:
                    body = r.json() if "application/json" in ct else r.text
                except Exception:
                    body = r.text

                last_err = f"Request failed ({r.status_code}): {body}"
                break

            except Exception as e:
                last_err = str(e)

    raise Exception(last_err or "Unknown error")


def daylight_effect(image):
    image = ImageEnhance.Brightness(image).enhance(1.3)
    image = ImageEnhance.Contrast(image).enhance(1.1)
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    return image


def night_mood_effect(image):
    image = ImageEnhance.Brightness(image).enhance(0.9)
    image = ImageEnhance.Contrast(image).enhance(1.4)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    return image


def main():
    print("Welcome to the AI Image Stylist Project!")
    prompt = input("Enter your image description:\n").strip()

    try:
        print("Generating your base image...\n")
        base_image = generate_image_from_text(prompt)

        print("Applying Daylight Edition style...")
        daylight_img = daylight_effect(base_image)
        daylight_img.show()
        daylight_img.save(f"{prompt.replace(' ', '_')}_daylight.png")
        print("Daylight Edition Saved.\n")

        print("Applying Night Mood style...")
        night_img = night_mood_effect(base_image)
        night_img.show()
        night_img.save(f"{prompt.replace(' ', '_')}_night.png")
        print("Night Mood Saved.\n")

    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()