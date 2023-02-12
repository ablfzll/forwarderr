import sqlite3

def create_databese():
	conn = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS photo(id INTEGER PRIMARY KEY AUTOINCREMENT,photoid integer, type text)")
	cur.execute("CREATE TABLE IF NOT EXISTS video(id INTEGER PRIMARY KEY AUTOINCREMENT,videoid integer, type text)")
	return "create database successfully";