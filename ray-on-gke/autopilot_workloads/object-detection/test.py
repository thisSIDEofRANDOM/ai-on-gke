import requests
import numpy as np
import os

address = os.getenv('RAY_ADDRESS')
print(address)
address = address[:-5]

image_url = "https://ultralytics.com/images/zidane.jpg"
resp = requests.get(f"{address}:8000/detect?image_url={image_url}")

with open("output.jpeg", 'wb') as f:
    f.write(resp.content)
