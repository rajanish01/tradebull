import threading

import rel
import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")

    def ticker():
        ws.send('{"action":"subscribe","args":["Ticker"]}')
        print("Ticker Started :::")

    try:
        T = threading.Thread(target=ticker)
        T.start()
    except:
        print("Ticker Thread Failed To Start !")


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://openapi-ws.bitmart.com/api?protocol=1.1",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection

    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
