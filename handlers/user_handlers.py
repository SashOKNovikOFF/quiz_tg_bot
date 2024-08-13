from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from database.database import user_dict_template, users_db, \
    add_userinfo_in_db, update_userinfo_in_db
from keyboards.keyboards import (create_quiz_keyboard,
                                 begin_quiz_keyboard,
                                 return_quiz_keyboard)
from lexicon.lexicon import LEXICON
from services.file_handling import riddles
import logging

# Инициализируем логгер
logger = logging.getLogger(__name__)

router = Router()


def create_new_user_db(message: Message):
    user_id = message.from_user.id
    if (user_id not in users_db) and not message.from_user.is_bot:
        users_db[user_id] = deepcopy(user_dict_template)
        add_userinfo_in_db(user_id, user_dict_template)


def is_riddle_last(message: Message):
    current_riddle = users_db[message.from_user.id]['current_riddle']
    return current_riddle == len(riddles) - 1


def is_riddle_last(callback: CallbackQuery):
    current_riddle = users_db[callback.from_user.id]['current_riddle']
    return current_riddle == len(riddles) - 1


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    create_new_user_db(message)
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=begin_quiz_keyboard()
    )


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    create_new_user_db(message)
    await message.answer(LEXICON[message.text])


# Этот хэндлер будет срабатывать на команду "/begin_quiz"
# и отправлять пользователю текущую загадку с кнопками вариантов ответа
@router.message(Command(commands='begin_quiz'))
async def process_begin_quiz_command(message: Message):
    create_new_user_db(message)
    
    if is_riddle_last(message):
        await message.answer(text=LEXICON['end'])
    else:
        riddle = riddles[users_db[message.from_user.id]['current_riddle']]
        await message.answer(
            text=riddle.text,
            reply_markup=create_quiz_keyboard(riddle)
        )


# Этот хэндлер будет срабатывать на команду "/stat"
# и отправлять пользователю текущий статус по отгаданным загадкам
@router.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    create_new_user_db(message)
    
    user_data = users_db[message.from_user.id]
    current_points    = user_data['current_points']
    current_level     = user_data['current_level']
    total_riddles_num = user_data['total_riddles_num']
    
    text = f"""
    <b>Ваш текущий результат</b>:
    
    Текущий уровень - {current_level}
    Количество полученных баллов - {current_points}
    Количество полученных загадок - {total_riddles_num}
    """
    await message.answer(
        text=text,
        reply_markup=return_quiz_keyboard()
    )


# Этот хэндлер будет срабатывать на инлайн-кнопки "begin_quiz", "return_quiz"
# и отправлять пользователю текущую загадку с кнопками вариантов ответа
@router.callback_query((F.data == 'begin_quiz') | (F.data == 'return_quiz'))
async def process_return_quiz_command(callback: CallbackQuery):
    create_new_user_db(callback.message)
    
    if is_riddle_last(callback):
        logging.info("Успешно пройдены все загадки")
        await callback.message.answer(text=LEXICON['end'])
    else:
        logging.info("Ещё не всё отгадали")
        riddle = riddles[users_db[callback.from_user.id]['current_riddle']]
        await callback.message.answer(
            text=riddle.text,
            reply_markup=create_quiz_keyboard(riddle)
        )


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером варианта и сообщать нам о выигрыше/проигрыше
@router.callback_query(lambda x: x.data in {"0", "1", "2", "3"})
async def guess_right_riddle_answer(callback: CallbackQuery):
    current_riddle = riddles[users_db[callback.from_user.id]['current_riddle']]
    if int(callback.data) == current_riddle.right_variant:
        users_db[callback.from_user.id]['current_points'] += 1
        if not is_riddle_last(callback):
            users_db[callback.from_user.id]['current_riddle'] += 1
            users_db[callback.from_user.id]['total_riddles_num'] += 1

        await callback.message.answer('Ты угадал! Ты получил 1 балл.')
    else:
        if not is_riddle_last(callback):
            users_db[callback.from_user.id]['current_riddle'] += 1
            users_db[callback.from_user.id]['total_riddles_num'] += 1
        
        await callback.message.answer('Ты не угадал! :(')
    
    if is_riddle_last(callback):
        await callback.message.answer(text=LEXICON['end'])
    else:
        riddle = riddles[users_db[callback.from_user.id]['current_riddle']]
        await callback.message.answer(
            text=riddle.text,
            reply_markup=create_quiz_keyboard(riddle)
        )
    
    update_userinfo_in_db(callback.from_user.id, users_db[callback.from_user.id])