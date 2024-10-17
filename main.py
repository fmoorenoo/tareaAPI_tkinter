import requests
from dataclass_wizard import fromdict
from models.api_response import APIResponse
import interfaz

def main():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)

    interfaz.mostrarProducto(product_list, 0)


if __name__ == '__main__':
    main()



