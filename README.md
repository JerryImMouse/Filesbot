
# Project Title

Telegram bot written on aiogram 3 library. It allows to store texts in it using sqlite3 database. Active development will improve its abilities.


![Logo](https://i.imgur.com/fYg3TBi.png)


## Installation

To install this bot you can use simple pip command

```bash
  touch files.db
  pip install -r requirements.txt
  python3 main.py
```
After all you had to create a config.py file in a root folder with other .py files.
    
## Environment Variables

To run this bot, you had to create one on BotFather on Telegram and get a token  

Then you had to place your API token to config.py file

`BOT_TOKEN`

Bot also have an ID filter to prevent database from trashing, you also need to add IDS variable into config.py file and pass some list with ids to it.

`IDS = [integerID], [anotherID]`

## Localization

All localization files stores in [text.py](https://github.com/JerryImMouse/Filesbot/blob/master/text.py)

You can just simply rewrite them all on willing language
## Roadmap

- Add the possibility to upload .pdf, .docx documents

- Make source code more organized and move all source files to **/src** folder

- W.I.P


## Screenshot

![Bot Screenshot](https://i.imgur.com/P6AGYzc.png)


## License

[MIT License](https://choosealicense.com/licenses/mit/)  
Copyright (c) 2023 JerryTheMouse  



