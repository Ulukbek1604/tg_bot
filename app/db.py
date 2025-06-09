import sqlite3

db =sqlite3.connect('tg_bot.db')
c =db.cursor()

def add_steam_key_into_db(game_name,st_key,count,price):
    try:
        c.execute('''INSERT INTO steam_keys (game_name, st_key, count,price) 
            VALUES (?, ?, ?, ?)''',(game_name,st_key,count,price) )
        db.commit()

    except sqlite3.OperationalError:
        print("Не получилось добавить запись")
def edit_steam_key_into_db(game_name,st_key,count,price):
    pass

def delete_steam_key_from_db(key_id):
    try:
        c.execute('''DELETE FROM steam_keys WHERE id=?''', (key_id,))
        db.commit()
    except:
        print("Удалить не пролучилось")
c.execute("""CREATE TABLE steam_keys(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name text,
    st_key text,
    price integer)
""")

db.close()

# c.execute('''DROP TABLE steam_keys''')
# db.commit()

# db.commit()

