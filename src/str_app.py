import streamlit as st
import sys
import os


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


from api_client import (
    get_products,
    add_product,
    update_product,
    delete_product
)


st.set_page_config(
    page_title="Product Inventory",
    page_icon="📦",
    layout="wide"
)


st.title("📦 Product Inventory Management")
st.write(
    "Manage your products using FastAPI and Streamlit."
)


# ==========================================
# Get Products
# ==========================================

result = get_products()

if "products" in result:
    products = result["products"]
else:
    products = []


# ==========================================
# Dashboard
# ==========================================

total_products = len(products)

total_stock = sum(
    product["stock"]
    for product in products
)

low_stock = sum(
    1
    for product in products
    if product["stock"] <= 5
)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Products",
        total_products
    )

with col2:
    st.metric(
        "Total Stock",
        total_stock
    )

with col3:
    st.metric(
        "Low Stock Products",
        low_stock
    )


st.divider()


# ==========================================
# Add Product
# ==========================================

st.subheader("➕ Add New Product")


with st.form("add_product_form"):

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    name = st.text_input(
        "Product Name"
    )

    category = st.text_input(
        "Category"
    )

    price = st.number_input(
        "Price",
        min_value=0,
        step=1000
    )

    stock = st.number_input(
        "Stock",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button(
        "Add Product"
    )


    if submitted:

        if not name or not category:
            st.error(
                "Please enter product name and category."
            )

        else:

            new_product = {
                "id": int(product_id),
                "name": name,
                "category": category,
                "price": int(price),
                "stock": int(stock)
            }

            result = add_product(new_product)

            if "error" not in result:

                if result.get("message") == "Product ID already exists":

                    st.warning(
                        "A product with this ID already exists."
                    )

                else:

                    st.success(
                        "Product added successfully! 🎉"
                    )

                    st.rerun()

            else:

                st.error(
                    result["error"]
                )


st.divider()


# ==========================================
# Update Product
# ==========================================

st.subheader("✏️ Update Product")


if products:

    product_options = {
        f"{product['id']} - {product['name']}":
        product
        for product in products
    }


    selected_product_name = st.selectbox(
        "Select a product",
        list(product_options.keys())
    )


    selected_product = product_options[
        selected_product_name
    ]


    with st.form("update_product_form"):

        new_name = st.text_input(
            "Product Name",
            value=selected_product["name"]
        )

        new_category = st.text_input(
            "Category",
            value=selected_product["category"]
        )

        new_price = st.number_input(
            "Price",
            min_value=0,
            value=int(selected_product["price"]),
            step=1000
        )

        new_stock = st.number_input(
            "Stock",
            min_value=0,
            value=int(selected_product["stock"]),
            step=1
        )


        update_button = st.form_submit_button(
            "Update Product"
        )


        if update_button:
            updated_product = {
                "name": new_name,
                "category": new_category,
                "price": int(new_price),
                "stock": int(new_stock)
            }


            result = update_product(
                selected_product["id"],
                updated_product
            )


            if "error" not in result:

                st.success(
                    "Product updated successfully! ✅"
                )

                st.rerun()

            else:

                st.error(
                    result["error"]
                )


st.divider()


# ==========================================
# Product List
# ==========================================

st.subheader("📋 Product List")


if products:

    for product in products:

        col1, col2 = st.columns(
            [5, 1]
        )


        with col1:

            stock_status = (
                "⚠️ Low Stock"
                if product["stock"] <= 5
                else "✅ In Stock"
            )


            st.write(
                f"{product['name']}  \n"
                f"Category: {product['category']}  \n"
                f"Price: {product['price']:,} تومان  \n"
                f"Stock: {product['stock']} — "
                f"{stock_status}"
            )


        with col2:

            if st.button(
                "🗑️ Delete",
                key=f"delete_{product['id']}"
            ):

                result = delete_product(
                    product["id"]
                )


                if "error" not in result:

                    st.success(
                        "Product deleted successfully!"
                    )

                    st.rerun()

                else:

                    st.error(
                        result["error"]
                    )


        st.divider()


else:

    st.info(
        "No products available."
    )