
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple menu for demo
menu = {
    "pizza": 250,
    "burger": 150,
    "pasta": 200,
    "cold drink": 50
}

orders = []  # store user orders temporarily
@app.route('/')
def index():
    # ensure templates/index.html exists (templates/index.html)
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204
@app.route('/chat', methods=['POST'])
def chat():
    # accept JSON or form data safely
    data = request.get_json(silent=True) or request.form or {}
    user_msg = ""
    if isinstance(data, dict):
        user_msg = (data.get('message') or "").strip().lower()
    else:
        user_msg = (data or "").strip().lower()

    if not user_msg:
        return jsonify({"error": "No message provided. Send JSON {\"message\":\"...\"} or form field 'message'."}), 400

    response = ""

    # Greet
    if "hello" in user_msg or "hi" in user_msg:
        response = "Hi! 👋 Welcome to FoodieHub! Here's our menu: Pizza ₹250, Burger ₹150, Pasta ₹200, Cold Drink ₹50. What would you like to order?"

    # Check for menu items
    elif any(item in user_msg for item in menu.keys()):
        item = next((food for food in menu if food in user_msg), None)
        if item:
            orders.append(item)
            response = f"Added {item} to your order. Would you like to add more or confirm?"
        else:
            response = "Sorry, couldn't identify the item. Try 'pizza' or 'burger'."

    elif "confirm" in user_msg:
        total = sum(menu[item] for item in orders) if orders else 0
        response = f"Your order: {', '.join(orders) if orders else 'nothing'}. Total ₹{total}. Please share your name and address."

    elif "address" in user_msg:
        response = "✅ Order confirmed! It'll reach you soon. Thank you for ordering with FoodieHub 🍔"
        orders.clear()

    else:
        response = "Sorry, I didn't understand that. You can say 'I want a pizza' or 'confirm order'."

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)