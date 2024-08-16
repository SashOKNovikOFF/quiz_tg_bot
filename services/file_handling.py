import os
import sys
from dataclasses import dataclass

RIDDLES_PATH = [
    'riddles/riddles_1.txt',
    'riddles/riddles_2.txt',
    'riddles/riddles_3.txt',
    'riddles/riddles_4.txt',
    'riddles/riddles_5.txt',
]

@dataclass
class Riddle:
    text: str
    variants: list[str]
    right_variant: int


riddles: list[list[Riddle]] = [
    [], [], [], [], []
]


# Функция, возвращающая список загадок с вариантами ответов и верным ответом
def prepare_riddles(block_num: int, path: str) -> None:
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
                riddles[block_num].append(riddle)
                variants.clear()
        counter += 1
    f.close()
    return riddles


# Вызов функции prepare_riddles для подготовки загадок из текстового файла
for ind in range(0, len(RIDDLES_PATH)):
    path = os.path.join(sys.path[0], os.path.normpath(RIDDLES_PATH[ind]))
    prepare_riddles(ind, path)