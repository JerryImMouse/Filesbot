from aiogram.types import Message
import text as t

class Additions:
    def log(text):
        try:
            print("LOG: " + text)
        except:
            print("ERR: Unable to log information.")

    msg_to_edit = Message