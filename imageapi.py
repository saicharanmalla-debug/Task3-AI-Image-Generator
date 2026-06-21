from dotenv import load_dotenv
import os
import requests
load_dotenv("task3.env")
apiurl = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
api_key = os.getenv("api_key")
headers= {
    "Authorization": f"Bearer {api_key}"
}

def gen_img(p):
  response = requests.post(
         apiurl,
         headers=headers,
         json={"inputs": p})

  return response
