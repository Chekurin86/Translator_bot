from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU, get_random_phrase
from services.services import translate
from aiogram import F, Router

# Инициализируем роутер уровня модуля
router = Router()

# Этот хендлер будет срабатывать на любые текстовые сообщения,
# кроме "/start" и "/help"
@router.message(F.text)
async def send_translate(message: Message):
    await message.answer(get_random_phrase())
    await message.answer(text=translate(message.text))

@router.message()
async def send_echo(message: Message):
    await message.answer(LEXICON_RU['error'])