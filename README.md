# 📦 Product Inventory Management

A simple product inventory management system built with FastAPI and Streamlit.

## ✨ Features

- Add, update, delete, and view products
- Product search by ID
- Inventory statistics
- Low-stock detection
- REST API with FastAPI
- Interactive frontend with Streamlit

## 🛠️ Technologies

- Python
- FastAPI
- Streamlit
- Requests
- Uvicorn

## 📁 Project Structure


product-inventory-management/
│
├── src/
│   ├── init.py
│   ├── app.py
│   ├── api_client.py
│   └── str_app.py
│
├── .gitignore
├── requirements.txt
└── README.md

🚀 Installation

git clone https://github.com/YOUR-USERNAME/product-inventory-management.git
cd product-inventory-management
pip install -r requirements.txt

▶️ Run the Project

Start the FastAPI backend:
uvicorn src.app:app --reload

API documentation:
http://127.0.0.1:8000/docs

In another terminal, start Streamlit:
streamlit run src/str_app.py


🔗 API Endpoints

Method
Endpoint
Description
GET
/products/
Get all products
GET
/products/{id}
Get a product
POST
/products/
Add a product
PUT
/products/{id}
Update a product
DELETE
/products/{id}
Delete a product

⚠️ Note
Product data is currently stored in memory and will reset when the FastAPI server restarts.

👩‍💻 Author

Sara Ayough

⭐ If you find this project useful, feel free to explore the repository.
