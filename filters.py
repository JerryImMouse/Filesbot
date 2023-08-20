import asyncio
from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

class IDFilter(BaseFilter):
    def __init__(self, id: Union[int, list]):
        self.id = id

    async def __call__(self, msg: Message) -> bool:
        if type(self.id) == list:
            for el in self.id:
                print(el)
                if msg.from_user.id == el:
                    return True
                else: pass
        else: 
            if msg.from_user.id == self.id:
                print(self.id)
                return True
            else: return False