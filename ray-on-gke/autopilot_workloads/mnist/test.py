import requests
import numpy as np
import os

address = os.getenv('RAY_ADDRESS')
print(address)
resp = requests.get(
        address[:-5] + ":8000/", json={"array": np.random.randn(28 * 28).tolist()}
)
print(resp.json())
