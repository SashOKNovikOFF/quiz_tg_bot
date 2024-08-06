import os
import sys
from dataclasses import dataclass

RIDDLES_PATH = 'riddles/riddles.txt'

@dataclass
class Riddle:
    text: str
    diff_level: str
    variants: list[str]
    right_variant: int


riddles: list[Riddle] = []


# Функция, возвращающая список загадок с вариантами ответов и верным ответом
def prepare_riddles(path: str) -> None:
    f = open(path, 'r')
    counter = 0

    text = ""
    diff_level = ""
    variants = []
    right_variant = 0

    for line in f:
        line_num = counter % 7
        match line_num:
            case 0:
                diff_level = line
            case 1:
                text = line
            case 2 | 3 | 4 | 5:
                if line.startswith("+ "):
                    variants.append(line.split("+ ")[1])
                    right_variant = len(variants) - 1
                else:
                    variants.append(line)
            case 6:
                riddle = Riddle(
                    text=text,
                    diff_level=diff_level,
                    variants=variants.copy(),
                    right_variant=right_variant
                )
                riddles.append(riddle)
                variants.clear()
        counter += 1
    f.close()
    return riddles


# Вызов функции prepare_riddles для подготовки загадок из текстового файла
prepare_riddles(os.path.join(sys.path[0], os.path.normpath(RIDDLES_PATH)))