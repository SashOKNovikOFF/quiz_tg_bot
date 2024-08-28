import os
import sys
from dataclasses import dataclass

RIDDLES_RU_PATH = [
    'riddles/riddles_1.txt',
    'riddles/riddles_2.txt',
    'riddles/riddles_3.txt',
    'riddles/riddles_4.txt',
    'riddles/riddles_5.txt',
]

RIDDLES_BA_PATH = [
    'riddles/riddles_6.txt',
    'riddles/riddles_7.txt',
    'riddles/riddles_8.txt',
    'riddles/riddles_9.txt',
    'riddles/riddles_10.txt',
]

@dataclass
class Riddle:
    text: str
    variants: list[str]
    right_variant: int


riddles: dict[str, list[list[Riddle]]] = {
    "ru": [[], [], [], [], []],
    "ba": [[], [], [], [], []]
}


# Функция, возвращающая список загадок с вариантами ответов и верным ответом
def prepare_riddles(block_num: int, path: str, lang: str) -> None:
    f = open(path, 'r')
    counter = 0

    text = ""
    variants = []
    right_variant = 0

    for line in f:
        line_num = counter % 6
        match line_num:
            case 0:
                text = line
            case 1 | 2 | 3 | 4:
                if line.startswith("+ "):
                    variants.append(line.split("+ ")[1])
                    right_variant = len(variants) - 1
                else:
                    variants.append(line)
            case 5:
                riddle = Riddle(
                    text=text,
                    variants=variants.copy(),
                    right_variant=right_variant
                )
                riddles[lang][block_num].append(riddle)
                variants.clear()
        counter += 1
    f.close()
    return riddles


# Вызов функции prepare_riddles для подготовки загадок из текстового файла
for ind in range(0, len(RIDDLES_RU_PATH)):
    path = os.path.join(sys.path[0], os.path.normpath(RIDDLES_RU_PATH[ind]))
    prepare_riddles(ind, path, "ru")
for ind in range(0, len(RIDDLES_BA_PATH)):
    path = os.path.join(sys.path[0], os.path.normpath(RIDDLES_BA_PATH[ind]))
    prepare_riddles(ind, path, "ba")

# TODO: не хватает поддержки экранированных символов в .txt-файлах
riddles["ru"][1][0].text = 'Бер Ҡарт килə ҡағынып,\nАуа-түнə абынып,\nАҡ сəкмəнен ябынып.\n\nИдет дедушка отряхивается,\nЧуть не падает, спотыкается,\nБелой шубою накрывается.'
riddles["ru"][1][1].text = 'Донъя биҙәр йәм бит ул,\nҺүнмәй торған шәм бит ул.\nАлыҫ булһа ла үҙе,\nБалҡып нурлана йөҙө».\n\nОно украшение мира,\nСвечка, которую нельзя потушить,\nХотя и далеко оно,\nЛицо светится ярко.'
riddles["ru"][1][2].text = 'Тарағы бар – сәсен тарамай,\nУрағы бар – иген ура алмай.\n\nУ него есть гребень — не расчесывается,\nЕсть серп — не может жать хлеб.'
riddles["ru"][1][3].text = 'Батша түгелмен — тажым бар,\nКешеләргә бирер наҙым бар.\n\nХоть я не королева - но есть корона,\nЕсть нежность, которую дарю людям.'
riddles["ru"][1][4].text = 'Тирмəм эсе аҡ булғанда,\nТышы ҡара булалыр,\nТирмə эсе ҡарайғанда,\nТышы аҡтан булалыр.\n\nКогда в юрте светлеет\nНа улице темно;\nКогда в юрте темнеет,\nТо на улице светло.'
riddles["ru"][1][5].text = 'Аяғым юҡ — атлайым,\nТау аҡтарып ташлайым.\nКүмер, тимер тейәйем,\nҺис арыным, тимәйем.\n\nНет ног — могу ходить,\nМогу горы свернуть.\nГружу уголь и железо,\nНикогда не устаю.'
riddles["ru"][1][6].text = 'Самая сложная загадка этого уровня!\n\nИргә ҡанат,\nСолтанға һанат,\nЙәй арымай,\nҠыш ҡарышмай.\n\nДля мужчины крыло,\nДля царя визирь,\nЛетом не устает,\nЗимой не противится.'

riddles["ba"][1][0].text = 'Бер Ҡарт килə ҡағынып,\nАуа-түнə абынып,\nАҡ сəкмəнен ябынып.'
riddles["ba"][1][1].text = 'Донъя биҙәр йәм бит ул,\nҺүнмәй торған шәм бит ул.\nАлыҫ булһа ла үҙе,\nБалҡып нурлана йөҙө».'
riddles["ba"][1][2].text = 'Тарағы бар – сәсен тарамай,\nУрағы бар – иген ура алмай.'
riddles["ba"][1][3].text = 'Батша түгелмен — тажым бар,\nКешеләргә бирер наҙым бар.'
riddles["ba"][1][4].text = 'Тирмəм эсе аҡ булғанда,\nТышы ҡара булалыр,\nТирмə эсе ҡарайғанда,\nТышы аҡтан булалыр.'
riddles["ba"][1][5].text = 'Аяғым юҡ — атлайым,\nТау аҡтарып ташлайым.\nКүмер, тимер тейәйем,\nҺис арыным, тимәйем.'
riddles["ba"][1][6].text = 'Иргә ҡанат,\nСолтанға һанат,\nЙәй арымай,\nҠыш ҡарышмай.'