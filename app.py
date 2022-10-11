from db import db_setup as db
from clients import bitmart_client
from strategies import bb_15_min_strategy as bb15

cursor, con = db.setup()
db.create_tables(cursor, con)

# bitmart_client.start_socket()

bb15.start()