from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    
    #region Functions
    [InlineKeyboardButton(text="🔼Загрузить текст", callback_data="upload"), 
     InlineKeyboardButton(text="❌Удалить текст", callback_data="delete"), 
     InlineKeyboardButton(text="🔽Получить текст", callback_data="get")],
    #endregion
    
    #region Info
    [InlineKeyboardButton(text="🆑GitHub", url="https://github.com/JerryImMouse"), 
     InlineKeyboardButton(text="👨‍💻BotGuide", callback_data="guide"), 
     InlineKeyboardButton(text="ℹ️Info", callback_data="info")],
    #endregion
    
    #region Menu
    [InlineKeyboardButton(text="📃Список заголовков", callback_data="list")],
    [InlineKeyboardButton(text="📖Главное меню", callback_data="menu_show")]
    #endregion

]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])