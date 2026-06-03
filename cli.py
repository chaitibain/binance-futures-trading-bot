import os
import logging

from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_order
from bot.logging_config import setup_logger

# Load environment variables
load_dotenv()

# Setup logging
setup_logger()

# Get API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Create Binance client
client = BinanceClient(
    API_KEY,
    API_SECRET
).get_client()

# Create order manager
order_manager = OrderManager(client)

try:

    symbol = input(
        "Enter Symbol (e.g. BTCUSDT): "
    ).upper()

    side = input(
        "Enter Side (BUY/SELL): "
    ).upper()

    order_type = input(
        "Enter Order Type (MARKET/LIMIT): "
    ).upper()

    quantity = float(
        input("Enter Quantity: ")
    )

    price = None

    if order_type == "LIMIT":
        price = float(
            input("Enter Price: ")
        )

    # Validate inputs
    validate_order(
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    print("\n========== ORDER REQUEST ==========")

    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")

    if price is not None:
        print(f"Price: {price}")

    # Place order
    if order_type == "MARKET":

        response = (
            order_manager.place_market_order(
                symbol,
                side,
                quantity
            )
        )

    else:

        response = (
            order_manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )
        )

    print("\n========== ORDER RESPONSE ==========")

    print(
        f"Order ID: {response.get('orderId')}"
    )

    print(
        f"Status: {response.get('status')}"
    )

    print(
        f"Executed Qty: {response.get('executedQty')}"
    )

    print("\nOrder placed successfully.")

except Exception as e:

    logging.error(str(e))

    print(
        f"\nError occurred: {e}"
    )
