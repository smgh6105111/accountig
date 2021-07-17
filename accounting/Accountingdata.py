import sqlite3

def dataentry():
	con=sqlite3.connect('a.db')
	cur=con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS a (id INTEGER PRIMARY KEY,enidaccount text,ennaccount text,enmaccount text)')
	con.commit()
	con.close()
	
	
def adddata(enidaccount,ennaccount,enmaccount):
	con=sqlite3.connect('a.db')
	cur=con.cursor()
	cur.execute('INSERT INTO a VALUES (NULL,?,?,?)',(enidaccount,ennaccount,enmaccount))
	con.commit()
	con.close()
	
	
def viewdata():
        con=sqlite3.connect('a.db')
        cur=con.cursor()
        cur.execute('SELECT * FROM a')
        rows=cur.fetchall()
        con.close()
        return rows
	
def deldata(id):
		con=sqlite3.connect('a.db')
		cur=con.cursor()
		cur.execute("DELETE FROM a WHERE id=?",(id,))
		con.commit()
		con.close()	
	
	
def update(id,enidaccount="",ennaccount="",enmaccount=""):
		con=sqlite3.connect('a.db')
		cur=con.cursor()
		cur.execute("UPDATE a SET enidaccount=?, ennaccount=?,enmaccount=? WHERE id=?",(enidaccount,ennaccount,enmaccount,id))
		con.commit()
		con.close()    
    
    
def search(enidaccount="",ennaccount="",enmaccount=""):
	con=sqlite3.connect('a.db')
	cur=con.cursor()
	cur.execute("SELECT * FROM a WHERE enidaccount=? or ennaccount=? or enmaccount=?",(enidaccount,ennaccount,enmaccount))
	rows=cur.fetchall()
	con.close()
	return rows
	
	
	
	
	
	
	
	
	
	
dataentry()