from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message, FSInputFile
from database.database import user_dict_template, users_db, \
    add_userinfo_in_db, update_username_in_db, \
    update_language_in_db, update_userinfo_in_db
from keyboards.keyboards import (create_quiz_keyboard,
                                 begin_quiz_keyboard,
                                 choose_language_kb,
                                 alga_button_kb,
                                 outer_url_kb,
                                 next_tale_kb,
                                 next_info_block_kb,
                                 next_level_button_kb,
                                 return_buttons_kb,
                                 return_to_the_beginning_kb)
from lexicon.lexicon import LEXICON, LEXICON_RU_LAMBDA, TALES, INFO_BLOCKS, END_OF_INFO
from services.file_handling import riddles
import logging
import random

# Инициализируем логгер
logger = logging.getLogger(__name__)

router = Router()


def create_new_user_db(message: Message):
    user_id = message.from_user.id
    if (user_id not in users_db) and not message.from_user.is_bot:
        users_db[user_id] = deepcopy(user_dict_template)
        add_userinfo_in_db(user_id, user_dict_template)


def is_riddle_last(current_riddle: int):
    return current_riddle >= 5


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    create_new_user_db(message)
    user = message.from_user
    user_id = user.id
    if users_db[user_id]['username'] == "":
        users_db[user_id]['username'] = user.first_name
        update_username_in_db(user_id, users_db[user_id])

    await message.answer(
        text=LEXICON_RU_LAMBDA['greeting'](user.first_name),
        reply_markup=choose_language_kb()
    )


# Этот хэндлер будет срабатывать на инлайн-кнопку "ru/ba_lang_button"
# и здороваться с пользователем, используя его имя
@router.callback_query((F.data == 'ru_lang_button') | (F.data == 'ba_lang_button'))
async def process_language_command(callback: CallbackQuery):
    user = callback.from_user
    user_id = user.id
    users_db[user_id]['lang'] = callback.data[:2]
    update_language_in_db(user_id, users_db[user_id])

    lang = users_db[user_id]['lang']
    if users_db[user_id]['current_level'] == 1:
        await callback.message.edit_text(
            text=LEXICON[lang]['rules'],
            reply_markup=alga_button_kb(lang)
        )
    elif users_db[user_id]['current_level'] >= 6:
        # TODO: выделить в отдельную функцию
        image = FSInputFile("images/ornament.jpg", 'rb')
        await callback.message.answer_photo(photo=image)
        await callback.message.answer(
            text=LEXICON[lang]['end_of_quiz'],
            reply_markup=return_to_the_beginning_kb(lang)
        )
        return
    else:
        await callback.message.edit_text(
            text=LEXICON[lang]['continue_quiz'],
            reply_markup=next_level_button_kb(lang)
        )


# Этот хэндлер будет срабатывать на инлайн-кнопку "alga_button"
#  или "next_tale_button" и перейти к прочтению сказки
@router.callback_query((F.data == 'alga_button') | (F.data == 'next_tale_button') | (F.data == 'return_to_tales_button') | (F.data == 'return_to_the_beginning_button'))
async def process_tales_command(callback: CallbackQuery):
    callback_user = callback.from_user
    user_id = callback_user.id
    user = users_db[user_id]
    lang = user['lang']
    curr_tale_num = user['tale_num']
    
    if callback.data == 'return_to_the_beginning_button':
        user['current_level'] = 1
        user['current_points'] = 0
        user['current_riddle'] = 0
        user['current_riddles_list'] = ""
        user['tale_num'] = 0
    
    if curr_tale_num == len(TALES[lang]):
        await callback.message.edit_text(
            text=TALES[lang][curr_tale_num - 1],
            reply_markup=outer_url_kb(lang, curr_tale_num - 1)
        )
        await callback.message.answer(
            text=LEXICON[lang]['end_of_tales'],
            reply_markup=begin_quiz_keyboard(lang)
        )
    else:
        if curr_tale_num != 0:
            await callback.message.edit_text(
                text=TALES[lang][curr_tale_num - 1],
                reply_markup=outer_url_kb(lang, curr_tale_num - 1)
            )
            
        user['tale_num'] += 1
        update_userinfo_in_db(user_id, user)
        
        next_tale_num = user['tale_num']
        await callback.message.answer(
            text=TALES[lang][next_tale_num - 1],
            reply_markup=next_tale_kb(lang, next_tale_num - 1)
        )


# Этот хэндлер будет срабатывать на инлайн-кнопку "next_level_button"
# и перейти к прочтению следующего блока информации
@router.callback_query((F.data == 'next_level_button') | (F.data == 'next_info_block_button'))
async def process_tales_command(callback: CallbackQuery):
    callback_user = callback.from_user
    user_id = callback_user.id
    user = users_db[user_id]
    lang = user['lang']
    
    curr_level_num = user['current_level']
    curr_tale_num = user['tale_num']
    curr_info_blocks = INFO_BLOCKS[lang][curr_level_num]
    
    if curr_tale_num == len(curr_info_blocks):
        await callback.message.edit_text(
            text=curr_info_blocks[curr_tale_num - 1],
        )

        # TODO: Особые случаи обработки с клавиатурами
        if curr_level_num == 3:
            kb = begin_quiz_keyboard(
                lang,
                answer="Узнать еще пословицы и поговорки",
                url="https://folkgame.tilda.ws/poslovicy"
            )
        elif curr_level_num == 4:
            kb = begin_quiz_keyboard(
                lang,
                answer="Слушать",
                url="https://bashmusic.net/ru/music/zolotoe-nasledie/view/playlist/id/380"
            )
        else:
            kb = begin_quiz_keyboard(lang)

        await callback.message.answer(
            text=END_OF_INFO[lang][curr_level_num],
            reply_markup=kb
        )
    else:
        if curr_tale_num != 0:
            await callback.message.edit_text(
                text=curr_info_blocks[curr_tale_num - 1],
            )

        user['tale_num'] += 1
        update_userinfo_in_db(user_id, user)

        next_tale_num = user['tale_num']
        
        # TODO: Особые случаи обработки с клавиатурами
        if curr_level_num == 2 and next_tale_num == 3:
            kb = next_info_block_kb(lang, answer="Проверить ответ")
        elif curr_level_num == 3 and next_tale_num == 2:
            kb = next_info_block_kb(lang, answer="Проверить ответ")
        elif curr_level_num == 5 and next_tale_num == 4:
            kb = next_info_block_kb(
                lang,
                answer="Посмотреть фильм",
                url="https://youtu.be/1SxHYuGMnCw"
            )
        else:
            kb = next_info_block_kb(lang)
        
        await callback.message.answer(
            text=curr_info_blocks[next_tale_num - 1],
            reply_markup=kb
        )


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    create_new_user_db(message)
    await message.answer("Нажмите /start для выбора языка и дальнейшей работы бота.")


# Этот хэндлер будет срабатывать на инлайн-кнопки "begin_quiz_button"
# и отправлять пользователю текущую загадку с кнопками вариантов ответа
@router.callback_query(F.data == 'begin_quiz_button')
async def process_return_quiz_command(callback: CallbackQuery):
    callback_user = callback.from_user
    user_id = callback_user.id
    user = users_db[user_id]
    lang = user['lang']
    curr_level = user['current_level'] - 1
    
    riddles_list = list(range(0, len(riddles[lang][curr_level])))
    random.shuffle(riddles_list)
    user['current_riddles_list'] = ""
    for riddle_num in range(0, 5):
        user['current_riddles_list'] += f"{riddles_list[riddle_num]}, "
    update_userinfo_in_db(user_id, user)
    
    riddle = riddles[lang][curr_level][riddles_list[0]]
    await callback.message.answer(
        text=riddle.text,
        reply_markup=create_quiz_keyboard(riddle)
    )


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером варианта и сообщать нам о выигрыше/проигрыше
@router.callback_query(lambda x: x.data in {"0", "1", "2", "3"})
async def guess_right_riddle_answer(callback: CallbackQuery):
    callback_user = callback.from_user
    user_id = callback_user.id
    user = users_db[user_id]
    lang = user['lang']
    curr_level = user['current_level'] - 1

    current_riddles_list = user['current_riddles_list'].split(', ')
    curr_riddle_num = int(current_riddles_list[user['current_riddle']])
    current_riddle = riddles[lang][curr_level][curr_riddle_num]

    right_answer_str = ""
    if int(callback.data) == current_riddle.right_variant:
        right_answer_str = "<i>Ты правильно ответил!</i>\n\n"
        user['current_points'] += 5
    
    if not is_riddle_last(user['current_riddle']):
        user['current_riddle'] += 1
    
    if is_riddle_last(user['current_riddle']):
        if user['current_points'] >= 25:
            user['current_level'] += 1
            if user['current_level'] >= 6:
                await callback.message.delete()
                image = FSInputFile("images/ornament.jpg", 'rb')
                await callback.message.answer_photo(photo=image)
                await callback.message.answer(
                    text=LEXICON[lang]['end_of_quiz'],
                    reply_markup=return_to_the_beginning_kb(lang)
                )
    
                update_userinfo_in_db(user_id, user)
                return
            else:
                await callback.message.edit_text(
                    text=right_answer_str + LEXICON[lang]['quiz_win'],
                    reply_markup=next_level_button_kb(lang)
                )
        else:
            await callback.message.edit_text(
                text=right_answer_str + LEXICON[lang]['quiz_lose'],
                reply_markup=return_buttons_kb(lang, curr_level)
            )
        
        user['current_points'] = 0
        user['current_riddle'] = 0
        user['current_riddles_list'] = ""
        user['tale_num'] = 0
    else:
        next_riddle_num = int(current_riddles_list[user['current_riddle']])
        riddle = riddles[lang][curr_level][next_riddle_num]
        await callback.message.edit_text(
            text=right_answer_str + riddle.text,
            reply_markup=create_quiz_keyboard(riddle)
        )
    
    update_userinfo_in_db(user_id, user)