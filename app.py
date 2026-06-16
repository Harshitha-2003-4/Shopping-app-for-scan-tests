from flask import Flask, render_template, redirect, url_for, session, request, flash

app = Flask(__name__)
app.secret_key = "shopping_secret_key"

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 49.99, "image": "https://placehold.co/300x200?text=Headphones", "category": "Electronics"},
    {"id": 2, "name": "Running Shoes", "price": 79.99, "image": "https://placehold.co/300x200?text=Shoes", "category": "Fashion"},
    {"id": 3, "name": "Coffee Maker", "price": 34.99, "image": "https://placehold.co/300x200?text=Coffee+Maker", "category": "Kitchen"},
    {"id": 4, "name": "Yoga Mat", "price": 24.99, "image": "https://placehold.co/300x200?text=Yoga+Mat", "category": "Sports"},
    {"id": 5, "name": "Desk Lamp", "price": 19.99, "image": "https://placehold.co/300x200?text=Desk+Lamp", "category": "Home"},
    {"id": 6, "name": "Bluetooth Speaker", "price": 39.99, "image": "https://placehold.co/300x200?text=Speaker", "category": "Electronics"},
    {"id": 7, "name": "Backpack", "price": 44.99, "image": "https://placehold.co/300x200?text=Backpack", "category": "Fashion"},
    {"id": 8, "name": "Water Bottle", "price": 14.99, "image": "https://placehold.co/300x200?text=Water+Bottle", "category": "Sports"},
]


def get_cart():
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart


def get_cart_count():
    return sum(item["qty"] for item in get_cart().values())


def get_product_by_id(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


@app.context_processor
def inject_cart_count():
    return {"cart_count": get_cart_count()}


@app.route("/")
def index():
    category = request.args.get("category", "All")
    if category and category != "All":
        products = [p for p in PRODUCTS if p["category"] == category]
    else:
        products = PRODUCTS
    categories = ["All"] + sorted(set(p["category"] for p in PRODUCTS))
    return render_template("index.html", products=products, categories=categories, active_category=category)


@app.route("/cart")
def cart():
    cart = get_cart()
    items = []
    total = 0.0
    for pid, item in cart.items():
        subtotal = item["price"] * item["qty"]
        total += subtotal
        items.append({**item, "id": pid, "subtotal": subtotal})
    return render_template("cart.html", items=items, total=total)


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    product = get_product_by_id(product_id)
    if not product:
        flash("Product not found.", "danger")
        return redirect(url_for("index"))
    cart = get_cart()
    pid = str(product_id)
    if pid in cart:
        cart[pid]["qty"] += 1
    else:
        cart[pid] = {"name": product["name"], "price": product["price"], "qty": 1}
    save_cart(cart)
    flash(f'"{product["name"]}" added to cart!', "success")
    return redirect(request.referrer or url_for("index"))


@app.route("/remove/<int:product_id>")
def remove_from_cart(product_id):
    cart = get_cart()
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        save_cart(cart)
        flash("Item removed from cart.", "info")
    return redirect(url_for("cart"))


@app.route("/update/<int:product_id>", methods=["POST"])
def update_qty(product_id):
    qty = int(request.form.get("qty", 1))
    cart = get_cart()
    pid = str(product_id)
    if pid in cart:
        if qty < 1:
            del cart[pid]
            flash("Item removed from cart.", "info")
        else:
            cart[pid]["qty"] = qty
    save_cart(cart)
    return redirect(url_for("cart"))


@app.route("/clear")
def clear_cart():
    session.pop("cart", None)
    flash("Cart cleared.", "info")
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        session.pop("cart", None)
        return render_template("order_success.html")
    cart = get_cart()
    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("cart"))
    items = []
    total = 0.0
    for pid, item in cart.items():
        subtotal = item["price"] * item["qty"]
        total += subtotal
        items.append({**item, "id": pid, "subtotal": subtotal})
    return render_template("checkout.html", items=items, total=total)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
