# Binance Futures Testnet Trading Bot

## Overview

This project is a Python Command Line Interface (CLI) application that allows users to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

The application demonstrates:

* Python programming
* REST API integration
* Error handling
* Logging
* Input validation
* Modular project structure

## Features

* Place BUY orders
* Place SELL orders
* MARKET order support
* LIMIT order support
* Order validation
* Logging of API responses
* Exception handling

## Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── app.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Running the Application

```bash
python cli.py
```

## Example Market Order

```text
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): MARKET
Enter Quantity: 0.001
```

## Example Limit Order

```text
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): LIMIT
Enter Quantity: 0.001
Enter Price: 100000
```

## Logs

Application logs are stored in:

```text
logs/app.log
```

## Author

Developed as part of a Python Developer assessment project.

