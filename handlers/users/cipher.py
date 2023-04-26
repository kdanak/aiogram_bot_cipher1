from loader import dp
from aiogram import types
import string


@dp.message_handler()
async def cipher(message: types.Message):
    shift = 2
    result = ''
    alphabet = string.ascii_lowercase + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    result += message.text.translate(table)
    await message.answer(result)