from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
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
          width=2
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def begin_quiz_keyboard() -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['begin_quiz'],
            callback_data='begin_quiz'
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def return_quiz_keyboard() -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер кнопку возврата в игру
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['return_quiz'],
            callback_data='return_quiz'
        )
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()