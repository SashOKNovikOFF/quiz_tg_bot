from aiogram import Router
from aiogram.types import Message

router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(
        text=f'Я не понимаю вашу команду {message.text}. \
                         Воспользуйтесь справочной командой /help для подробностей.',
    )