import requests

BASE_URL = "http://127.0.0.1:8000"
session = requests.Session()
session.trust_env = False

def get_products():
    url = f"{BASE_URL}/products/"
    response = session.get(url)

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to get products"}

def get_product(product_id):
    url = f"{BASE_URL}/products/{product_id}"
    response = session.get(url)

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to get product"}

def add_product(product):
    url = f"{BASE_URL}/products/"
    response = session.post(url, json=product)

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to add product"}

def update_product(product_id, product):
    url = f"{BASE_URL}/products/{product_id}"
    response = session.put(url, json=product)

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to update product"}

def delete_product(product_id):
    url = f"{BASE_URL}/products/{product_id}"
    response = session.delete(url)

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to delete product"}

if __name__ == "__main__":
    result = get_products()
    print(result)