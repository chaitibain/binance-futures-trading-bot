import logging

class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):
        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(
            f"MARKET ORDER: {response}"
        )

        return response

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):
        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(
            f"LIMIT ORDER: {response}"
        )

        return response
