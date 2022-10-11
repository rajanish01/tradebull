from indicators.taapi_client import taapi_client as tapapi


def response():
    strategy_config = {
            "exchange": "binance",
            "symbol": "BTC/USDT",
            "interval": "15m",
            "indicators": [
                {
                    "id": "bbands",
                    "indicator": "bbands2"
                }
            ]
    }
    try:
        return tapapi.loan_indicator(strategy_config)
    except:
        raise Exception("Strategy Request Failed To Respond !")

print(response())
