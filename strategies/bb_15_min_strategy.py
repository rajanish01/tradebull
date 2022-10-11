import strategies.bb_15_min_setup as bb
from clients import bitmart_client as bc


def start():
    asset = "ETH"
    currency = "USDT"
    bband = bb.response(asset + "/" + currency).data[0].result
    asset_last_price = bc.get_asset_price(asset + "_" + currency).data.last_price

    if asset_last_price <= bband.valueLowerBand:
        # send buy trade signal
        pass
    if asset_last_price >= bband.valueUpperBand:
        # send sell trade signal
        pass
