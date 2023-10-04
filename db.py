import sqlite3 as sql
from text import Text
class datab:
    con = sql.Connection
    cur = sql.Cursor

    def makeconnection():
        datab.con = sql.connect('files.db')
        datab.cur = datab.con.cursor()
        
        try: 
            datab.cur.execute("""CREATE TABLE "texts" ("title" TEXT, "text" TEXT)""") #Create table if it not exists
        except: pass

    def addtodb(title, text):
        exists = datab.cur.execute(f"SELECT title FROM texts WHERE title='{title}'"); exists = datab.cur.fetchone()
        
        if exists == None: pass
        else: return Text.failed_to_upload
        
        try:
            datab.cur.execute("SELECT title FROM texts")
            datab.cur.execute(f'INSERT INTO texts VALUES (?, ?)', (title, text))
            datab.con.commit()
            return Text.uploaded
        except:
            return Text.failed_to_upload
    
    def getfromdb(title):
        
        datab.cur.execute(f"SELECT text FROM texts WHERE title='{title}'")
        target = datab.cur.fetchone()
        
        if target is None:
            return Text.not_found
        return target[0]
    
    def getalltitles():
        
        datab.cur.execute(f"SELECT title FROM texts")
        target = datab.cur.fetchall()
        
        return target
    
    def deletefromdb(title):
        try:
            
            exists = datab.cur.execute(f"SELECT * FROM texts WHERE title='{title}'"); exists = datab.cur.fetchone()
            
            if exists != None:
                datab.cur.execute(f"DELETE FROM texts WHERE title='{title}'")
                datab.con.commit()
                return Text.deleted
            else:
                return Text.not_found
        
        except:
            return Text.crit_delete_error
