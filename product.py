import requests,json
BASE_URL = 'https://fakestoreapi.com'

# product_response = requests.get(f"{BASE_URL}/products/2")
# print(product_response.json())

# product_response = requests.get(f"{BASE_URL}/products")
# print(product_response.json())

#for product in product_response.json():
#    print(f"{product['title']} costs ${product['price']}" )

# Get products with a limit with query params
# query_params = {"limit": 4}
# product_response = requests.get(f"{BASE_URL}/products", params=query_params)
# print(product_response.json())

#Categories
# product_response = requests.get(f"{BASE_URL}/products/categories")
# print(product_response.json())

#Newproduct

# new_product = {
#                     "title": 'Mobile',
#                     "price": 150000,
#                     "description": 'IPhone',
#                     "image": 'https://i.pravatar.cc',
#                     "category": 'electronic'
#                 }
# response = requests.post(f"{BASE_URL}/products", json=new_product)
# print(response.json())

# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.post(f"{BASE_URL}/products", data=json.dumps(new_product), headers=headers)
# print(response.json())


# update a product
update_prod = {
    "title": 'test product- x',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.put(f"{BASE_URL}/products/21", json=update_prod)
print(response.json())


# Delete a product

res = requests.delete(f"{BASE_URL}/products/11")
print(res.json())
