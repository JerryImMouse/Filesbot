import sqlite3 as sql
import text
class datab:
    con = sql.Connection
    cur = sql.Cursor

    title = None
    text = None

    def makeconnection():
        datab.con = sql.connect('files.db')
        datab.cur = datab.con.cursor()

    def addtodb():
        exists = datab.cur.execute(f"SELECT title FROM texts WHERE title='{datab.title}'"); exists = datab.cur.fetchone()
        if exists == None: pass
        else: return text.failed_to_upload
        try:
            datab.cur.execute("SELECT title FROM texts")
            datab.cur.execute(f'INSERT INTO texts VALUES (?, ?)', (datab.title, datab.text))
            datab.con.commit()
            return text.uploaded
        except:
            return text.failed_to_upload
    def getfromdb():
        datab.cur.execute(f"SELECT text FROM texts WHERE title='{datab.title}'")
        target = datab.cur.fetchone()
        if target is None:
            return text.not_found
        return target[0]
    
    def getalltitles():
        datab.cur.execute(f"SELECT title FROM texts")
        target = datab.cur.fetchall()
        return target
    
    def deletefromdb():
        try:
            exists = datab.cur.execute(f"SELECT * FROM texts WHERE title='{datab.title}'"); exists = datab.cur.fetchone()
            if exists != None:
                datab.cur.execute(f"DELETE FROM texts WHERE title='{datab.title}'")
                datab.con.commit()
                return "Успешно удалено"
            else:
                return "Во время удаления произошла ошибка. Скорее всего такого заголовка не существует."
        except:
            return "Во время удаления произошла ошибка.\n\nНапишите в Discord моему разработчику - jerryimmouse"
