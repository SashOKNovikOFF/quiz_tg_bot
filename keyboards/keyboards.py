from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, LEXICON_RU, LEX, TALES_URL
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


def begin_quiz_keyboard(lang: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEX[lang]['begin_quiz_button'],
            callback_data='begin_quiz_button'
        )
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
            text=LEX[lang]['alga_button'],
            callback_data='alga_button'
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
            text=LEX[lang]['read_tale_button'],
            url=TALES_URL[lang][tale_num]
        ),
        InlineKeyboardButton(
            text=LEX[lang]['next_tale_button'],
            callback_data='next_tale_button'
        )],
        width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def next_level_button_kb(lang: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEX[lang]['next_level_button'],
            callback_data='next_level_button'
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def return_buttons_kb(lang: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEX[lang]['begin_quiz_button'],
            callback_data='begin_quiz_button'
        ),
        InlineKeyboardButton(
            text=LEX[lang]['return_to_tales_button'],
            callback_data='return_to_tales_button'
        )],
        width=1
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()