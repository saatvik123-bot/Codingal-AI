import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

MODELS = [
    "stabilityai/stable-diffusion-3-medium-diffusers",  # keep your original as primary
    "ByteDance/SDXL-Lightning",
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-xl-base-1.0",    
]

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Accept": "image/png"}

def generate_image_from_text(prompt):
    """Generates an image from a text prompt using HF router fallbacks."""
    payload, last_err = {"inputs": prompt}, None

    for model in MODELS:
        url = f"https://router.huggingface.co/hf-inference/models/{model}"
       

    for _ in range(3):
        r = requests.post(url, headers=HEADERS, json=payload, timeout=120)
        ct = (r.headers.get("content-type") or"").lower()

        if r.status_code == 503 and "application/json" in ct:
            try:
                wait_s = int(r.json().get("estimated_time", 5)) except Exception:
                wait_s = 5
                time.sleep(wait_s + 1)
                continue
        if r.status_code == 200 and "application/json" not in ct:
            try:
                return
        Image.open(BytesIO(r.content)).convert("RGB") except Exception:
        last_err = f"Request failed with status code 200: Could not decode image bytes: {e}"
        break


        try:
            body = r.json() if "application/json" in ct else r.text except Exception:
            body = r.text
            last_err = f"Requests failed with status code {r.status_code}: {body}"
            break

        rais Exception(last_err or "Request failed with status code 500: Unknown error")

    def daylight_effect(image):
        image = ImageEnhance.Brightness(image)