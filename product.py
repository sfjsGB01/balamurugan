import requests
BASE_URL = 'https://fakestoreapi.com'

# product_response = requests.get(f"{BASE_URL}/products/2")
# print(product_response.json())

product_response = requests.get(f"{BASE_URL}/products")
print(product_response.json())

#for product in product_response.json():
#    print(f"{product['title']} costs ${product['price']}" )
