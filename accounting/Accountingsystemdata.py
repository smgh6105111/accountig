import sqlite3

def dataentry():
    con=sqlite3.connect('a2.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS a2(id INTEGER PRIMARY KEY,enidaccount text,ennaccount text,enmaccount text, enpardakhty text, endaryafty text,entozihat text,enalbaghy text) ')
    con.commit()
    con.close()
    
def adddata(enidaccount,ennaccount,enmaccount,enpardakhty,endaryafty,entozihat,enalbaghy):
    con=sqlite3.connect('a2.db')
    cur=con.cursor()
    cur.execute('INSERT INTO a2 VALUES(NULL,?,?,?,?,?,?,?)',(enidaccount,ennaccount,enmaccount,enpardakhty,endaryafty,entozihat,enalbaghy))
    con.commit()
    con.close() 
    
        
def viewdata():
        con=sqlite3.connect('a2.db')
        cur=con.cursor()
        cur.execute('SELECT * FROM a2')
        rows=cur.fetchall()
        con.close()
        return rows
    
        
def deldata(id):
		con=sqlite3.connect('a2.db')
		cur=con.cursor()
		cur.execute("DELETE FROM a2 WHERE id=?",(id,))
		con.commit()
		con.close()
		
		    
def update(id,enidaccount="",ennaccount="",enmaccount="",enpardakhty="",endaryafty="",entozihat="",enalbaghy=""):
		con=sqlite3.connect('a2.db')
		cur=con.cursor()
		cur.execute("UPDATE a2 SET enidaccount=?,ennaccount=?,enmaccount=?,enpardakhty=?, endaryafty=?,entozihat=?,enalbaghy=? WHERE id=?",(enidaccount,ennaccount,enmaccount,enpardakhty,endaryafty,entozihat,enalbaghy,id))
		con.commit()
		con.close()    
    
    
def search(enidaccount="",ennaccount="",enmaccount="",enpardakhty="",endaryafty="",entozihat="",enalbaghy=""):
	con=sqlite3.connect('a2.db')
	cur=con.cursor()
	cur.execute("SELECT * FROM a2 WHERE enidaccount=?or ennaccount=?or enmaccount=?or enpardakhty=? or endaryafty=? or entozihat=? or enalbaghy=? ",(enidaccount,ennaccount,enmaccount,enpardakhty,endaryafty,entozihat,enalbaghy))
	rows=cur.fetchall()
	con.close()
	return rows
dataentry()