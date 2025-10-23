# FoodieHub Restaurant Chatbot 🍕

A simple restaurant ordering chatbot built with Flask and JavaScript.

![FoodieHub Chatbot Demo](chatbot-demo.png)

## Features

- Interactive chat interface
- Menu display with prices
- Order management system
- Total bill calculation
- Order confirmation flow

## Tech Stack

- Backend: Python + Flask
- Frontend: HTML, CSS, JavaScript
- No database required (uses in-memory storage)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/jiyaydv/restraunt_chatbot.git
cd restraunt_chatbot
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the application:
```bash
python app.py
```

5. Open http://127.0.0.1:5000 in your browser

## How to Use

1. Start with "Hello" or "Hi"
2. Bot will show the menu
3. Order items by saying "I want a pizza" etc.
4. Say "confirm" to complete order
5. Provide delivery address
6. Get order confirmation

## Menu

- Pizza: ₹250
- Burger: ₹150
- Pasta: ₹200
- Cold Drink: ₹50

## Project Structure

```
restraunt_chatbot/
├── app.py              # Flask application
├── templates/
│   └── index.html      # Chat interface
├── static/
│   └── style.css       # Styling
└── README.md           # This file
```

## License

MIT License

## Author

JIYA YADAV