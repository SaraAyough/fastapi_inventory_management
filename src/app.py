from fastapi_offline import FastAPIOffline
from pydantic import BaseModel
from fastapi import Body

app = FastAPIOffline()


products = [{"id": 1, "name": "iPhone 15", "category": "Mobile", "price": 45000000, "stock": 8},
    {"id": 2, "name": "Galaxy S24", "category": "Mobile", "price": 38000000, "stock": 12},
    {"id": 3, "name": "MacBook Air M2", "category": "Laptop", "price": 65000000, "stock": 5}]

@app.get("/")
def home():
    return {"message": "Product Inventory API is running"}

@app.get("/products/")
def get_products():
    return {"products": products}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    return {"message": "Product not found"}

@app.post("/products/")
def add_product(product: dict = Body(...)):
    products.append(product)
    return {
        "message": "Product added successfully",
        "product": product}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully",
                "product": product}
    return {"message": "Product not found"}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: dict = Body(...)):
    for product in products:
        if product["id"] == product_id:
            product.update(updated_product)
            return {"message": "Product updated successfully", "product": product}
    return {"message": "Product not found"}