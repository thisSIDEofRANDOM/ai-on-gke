import requests
import os

address = os.getenv('RAY_ADDRESS')
print(address)
address = address[:-5]
print(address)

prompt = "a cute cat is dancing on the grass."
input = "%20".join(prompt.split(" "))
resp = requests.get(f"{address}:8000/imagine?prompt={input}")
with open("output.png", 'wb') as f:
    f.write(resp.content)
