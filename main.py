import requests

from models.api_response import APIResponse
from dataclass_wizard import fromdict

response = requests.get("https://dummyjson.com/products")
product_list = response.text

if response.status_code == 200:
    print('Datos:', response.json())
else:
    print('Error')

for product in product_list.products:
    print(product.title)

