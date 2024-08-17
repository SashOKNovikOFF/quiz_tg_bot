from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU, LEXICON, TALES_URL, RETURN_BUTTON
from services.file_handling import Riddle


# Функция, генерирующая клавиатуру для вопроса викторины
def create_quiz_keyboard(riddle: Riddle) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(
        *[InlineKeyboardButton(
            text=riddle.variants[ind],
            callback_data=str(ind)
          ) for ind in range(0, len(riddle.variants))],
          width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def begin_quiz_keyboard(lang: str, answer="", url="") -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    if answer == "" and url == "":
        kb_builder.row(
            InlineKeyboardButton(
                text=LEXICON[lang]['begin_quiz_button'],
                callback_data='begin_quiz_button'
            )
        )
    else:
        kb_builder.row(
            *[InlineKeyboardButton(
                text=answer,
                url=url
            ),
            InlineKeyboardButton(
                text=LEXICON[lang]['begin_quiz_button'],
                callback_data='begin_quiz_button'
            )],
            width=1
        )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def choose_language_kb() -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEXICON_RU['ru_lang_button'],
            callback_data='ru_lang_button'
        ),
        InlineKeyboardButton(
            text=LEXICON_RU['ba_lang_button'],
            callback_data='ba_lang_button'
        )],
        width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def alga_button_kb(lang: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[lang]['alga_button'],
            callback_data='alga_button'
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def outer_url_kb(lang: str, tale_num: int) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[lang]['read_tale_button'],
            url=TALES_URL[lang][tale_num]
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def next_tale_kb(lang: str, tale_num: int) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEXICON[lang]['read_tale_button'],
            url=TALES_URL[lang][tale_num]
        ),
        InlineKeyboardButton(
            text=LEXICON[lang]['next_tale_button'],
            callback_data='next_tale_button'
        )],
        width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def next_info_block_kb(lang: str, answer="") -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    if answer == "":
        # Добавляем в билдер кнопку возврата в игру
        kb_builder.row(
            InlineKeyboardButton(
                text=LEXICON[lang]['next_tale_button'],
                callback_data='next_info_block_button'
            )
        )
    else:
        kb_builder.row(
            InlineKeyboardButton(
                text=answer,
                callback_data='next_info_block_button'
            )
        )

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def next_level_button_kb(lang: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON[lang]['next_level_button'],
            callback_data='next_level_button'
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def return_buttons_kb(lang: str, curr_level: int) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    if curr_level == 0:
        return_text = LEXICON[lang]['return_to_tales_button']
        return_str = 'return_to_tales_button'
    else:
        return_text = RETURN_BUTTON[lang][curr_level + 1]
        return_str = 'next_info_block_button'

    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEXICON[lang]['begin_quiz_button'],
            callback_data='begin_quiz_button'
        ),
        InlineKeyboardButton(
            text=return_text,
            callback_data=return_str
        )],
        width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()