from aiogram.methods import EditMessageText, EditMessageCaption, EditMessageReplyMarkup
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types, F, Router
from aiogram import flags
from states import Gen
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from filters import IDFilter
from db import datab
import logging
import kb, config
from additional import Additions
from text import Text as text

misc = Additions
datab.makeconnection()
router = Router()

#region StartMenu

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.delete()
    misc.msg_to_edit = await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
    logging.info(text.log_started.format(user_id=msg.from_user.id, username=msg.from_user.full_name))

@router.callback_query(F.data == "menu_show")
async def callback_menu(callback: types.CallbackQuery):
    misc.msg_to_edit = await callback.message.edit_text(text.menu, reply_markup=kb.menu)
    await callback.answer()

@router.callback_query(F.data == "cancel")
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(text.canceled, reply_markup=kb.menu)
    logging.info(text.log_canceled
                 .format(userid=callback.from_user.id, username=callback.from_user.full_name))


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
    misc.msg_to_edit = await callback.message.edit_text(text=f'{text.choose_title_get}\n\n{titstr}', reply_markup=kb.cancel)
    await callback.answer()

@router.message(Gen.choosingTitleToGet, F.text)
async def title_to_get_chosen(msg: Message, state: FSMContext):
    await state.clear()
    logging.info(text.log_got.format(
        title=datab.getfromdb(msg.text), userid=msg.from_user.id, username=msg.from_user.full_name))
    await misc.msg_to_edit.edit_text(text=datab.getfromdb(msg.text), reply_markup=kb.menu)
    await msg.delete()
#endregion
#region UploadText

@router.callback_query(IDFilter(config.IDS), F.data == "upload")
async def upload_text(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Gen.choosingTitle)
    misc.msg_to_edit = await callback.message.edit_text(
        text.choose_title_upload, reply_markup=kb.cancel)
    await callback.answer()

@router.message(Gen.choosingTitle, F.text)
async def text_typed(msg: Message, state: FSMContext):
    await state.clear()
    
    result = msg.text.split("~") # Split result string on "title" and "text"

    ans = datab.addtodb(title=result[0], text=result[1])

    await misc.msg_to_edit.edit_text(text=ans, reply_markup=kb.menu)
    await msg.delete()

    logging.info(text.log_upload
                 .format(title=result[0], userid=msg.from_user.id, username=msg.from_user.full_name))
#endregion
#region INFO
@router.callback_query(F.data == "info")
async def bot_info(callback: types.CallbackQuery):
    misc.msg_to_edit = await callback.message.edit_text(text.info.format(name=callback.from_user.full_name), reply_markup=kb.menu)
    await callback.answer()

@router.callback_query(F.data == "list")
async def show_list(callback: types.CallbackQuery):
    titles = datab.getalltitles()
    titstr = ""
    i = 1
    for title in titles:
        titstr = titstr + str(i) + ") " + title[0] + "\n"
        i = i + 1
    misc.msg_to_edit = await callback.message.edit_text(text.titles_list + "\n\n" + titstr, reply_markup=kb.menu)
    await callback.answer()

@router.callback_query(F.data == "guide")
async def guide(callback: types.CallbackQuery):
    misc.msg_to_edit = await callback.message.edit_text(text.guide, reply_markup=kb.menu) 
    await callback.answer()   

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
    misc.msg_to_edit = await callback.message.edit_text(
        text=f'{text.choose_title_get}\n\n{titstr}', reply_markup=kb.cancel)
    await callback.answer()

@router.message(Gen.choosingTitleToDelete, F.text)
async def delete_text(msg: Message, state: FSMContext):
    await state.clear()
    title = msg.text
    await misc.msg_to_edit.edit_text(text=datab.deletefromdb(title), reply_markup=kb.menu)
    await msg.delete()
    logging.info(text.log_deleted
                 .format(title=datab.title, userid=msg.from_user.id, username=msg.from_user.full_name))
#endregion
#region Misc

@router.message()
async def miscmsg(msg: Message):
    logging.info(text.unknown_message
                 .format(message=msg.text, userid=msg.from_user.id, username=msg.from_user.full_name))
    await msg.delete()


#endregion