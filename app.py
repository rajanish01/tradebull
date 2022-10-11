from db import db_setup as db

cursor, con = db.setup()
db.create_tables(cursor, con)
