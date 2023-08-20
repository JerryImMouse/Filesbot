from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types, F, Router
from aiogram import flags
from states import Gen
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from filters import IDFilter
import kb
from db import datab
import db
import text
import config

datab.makeconnection()
router = Router()

#region StartMenu

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(Command("menu"))
@router.message(F.text == "Меню")
@router.message(F.text == "Главное меню")
@router.message(F.text == "📖Главное меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == "menu_show")
async def callback_menu(callback: types.CallbackQuery):
    await callback.message.answer(text.menu, reply_markup=kb.menu)
    await callback.answer()

@router.message(Command("cancel"))
async def cancel(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text.menu, reply_markup=kb.menu)

#endregion
#region GetText
@router.callback_query(F.data == "get")
async def get_text(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.choosingTitleToGet)
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await callback.message.answer(text.choose_title_get + "\n\n" + titstr)
    await callback.answer()

@router.message(Gen.choosingTitleToGet, F.text)
async def title_to_get_chosen(msg: Message, state: FSMContext):
    await state.clear()
    datab.title = msg.text
    await msg.answer(datab.getfromdb())
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(Command("get"))
async def cmd_get_text(msg: Message, state: FSMContext):
    await state.set_state(Gen.choosingTitleToGet)
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await msg.answer(text.choose_title_get + "\n\n" + titstr)
#endregion
#region UploadText

@router.callback_query(IDFilter([config.IDS]), F.data == "upload")
async def upload_text(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.choosingTitle)
    await callback.message.answer(text.choose_title_upload)
    await callback.answer()

@router.message(Gen.choosingTitle, F.text)
async def title_chosen(msg: Message, state: FSMContext):
    await state.set_state(Gen.typingText)
    datab.title = msg.text
    await msg.answer(text.insert_text)

@router.message(Gen.typingText, F.text)
async def text_typed(msg: Message, state: FSMContext):
    await state.clear()
    datab.text = msg.text
    await msg.answer(datab.addtodb())
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(IDFilter(config.IDS), Command("upload"))
async def cmd_upload_text(msg: Message, state: FSMContext):
    await state.set_state(Gen.choosingTitle)
    await msg.answer(text.choose_title_upload)
#endregion
#region INFO
@router.callback_query(F.data == "info")
async def bot_info(callback: types.CallbackQuery):
    await callback.message.answer(text.info.format(name=callback.from_user.full_name), reply_markup=kb.menu)
    await callback.answer()

@router.callback_query(F.data == "list")
async def show_list(callback: types.CallbackQuery):
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await callback.message.answer(text.titles_list + "\n\n" + titstr, reply_markup=kb.menu)
    await callback.answer()

@router.message(Command("list"))
async def cmd_list(msg: Message):
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await msg.answer(text.titles_list + "\n\n" + titstr, reply_markup=kb.menu)

@router.callback_query(F.data == "guide")
async def guide(callback: types.CallbackQuery):
    await callback.message.answer(text.guide, reply_markup=kb.menu) 
    await callback.answer()   

@router.message(Command("github"))
async def cmd_github(msg: Message):
    await msg.answer("GitHub: https://github.com/JerryImMouse/Filesbot", reply_markup=kb.menu)

@router.message(Command("guide"))
async def cmd_guide(msg: Message):
    await msg.answer(text.guide, reply_markup=kb.menu)

@router.message(Command("info"))
async def cmd_info(msg: Message):
      await msg.answer(text.info.format(name=msg.from_user.full_name), reply_markup=kb.menu)
#endregion
#region DeleteText

@router.callback_query(IDFilter(config.IDS), F.data == "delete")
async def choose_delete(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.choosingTitleToDelete)
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await callback.message.answer(text.choose_title_get + "\n\n" + titstr)
    await callback.answer()

@router.message(Gen.choosingTitleToDelete, F.text)
async def delete_text(msg: Message, state: FSMContext):
    await state.clear()
    datab.title = msg.text
    await msg.answer(datab.deletefromdb(), reply_markup=kb.menu)

@router.message(Command("delete"))
async def cmd_delete(msg: Message, state: FSMContext):
    await state.set_state(Gen.choosingTitleToDelete)
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    await msg.answer(text.choose_title_get + "\n\n" + titstr)
#endregion