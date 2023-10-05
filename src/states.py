from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    choosingTitle = State()
    typingText = State()
    choosingTitleToGet = State()
    choosingTitleToDelete = State()