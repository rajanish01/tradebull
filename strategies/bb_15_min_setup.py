from indicators.taapi_client import taapi_client as taapi


def response(symbol):
    strategy_config = {
        "exchange": "binance",
        "symbol": symbol,
        "interval": "15m",
        "indicators": [
            {
                "id": "bbands",
                "indicator": "bbands2"
            }
        ]
    }
    try:
        return taapi.loan_indicator(strategy_config)
    except Exception:
        raise Exception("Strategy Request Failed To Respond !")
