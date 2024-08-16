LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Показать стартовое окно бота',
    '/begin_quiz': 'Начать/продолжить разгадывать загадки',
    '/stat': 'Мои результаты викторины',
    '/help': 'Справка по работе бота'
}

LEXICON_RU: dict[str, str] = {
    '/start': 'Нажми кнопку «Регистрация», чтобы начать знакомство.',
    'ru_lang_button': 'Русский язык',
    'ba_lang_button': 'Башкирский язык',
    'rules': 'Давай начнем. Сейчас я расскажу тебе о том, как устроена игра.\n\n'
             'В игре 5 уровней, в каждом из которых ты познакомишься с одним из жанров башкирского фольклора: сказками, загадками, пословицами и поговорками, легендами, а также эпосом.\n\n'
             'В конце каждого раздела тебя ждет несколько простых заданий, которые помогут закрепить то, что ты узнаешь. Чтобы пройти на следующий уровень тебе нужно набрать в заданиях 25 баллов.\n\n'
             'Если не успеешь, потеряешь накопленные баллы и придется начинать сначала. Проходить уровни можно столько раз, сколько захочешь.\n\n'
             'Нажимай «Алга», чтобы начать.',
    'alga_button': 'Алга',
    'read_tale_button': 'Прочитать сказку',
    'next_tale_button': 'Идти дальше',
    'end_of_tales': 'Отлично! Теперь ты лучше знаешь башкирские сказки! Давай проверим, что ты запомнил.\n\n'
                    'Ответь на 5 вопросов викторины. За каждый правильный ответ ты получишь 5 баллов. Набери 25 баллов, чтобы перейти на следующий уровень. На первом уровне время на прохождение вопросов не ограничено.\n\n'
                    'Не страшно, если у тебя не получится сделать этого с первого раза, ты сможешь попробовать еще раз.\n\n'
                    'Готов? Тогда скорее нажимай на кнопку «Пройти викторину»',
    'begin_quiz_button': 'Пройти викторину',
    'quiz_win': 'Молодец! Ты справился с заданием и переходишь на следующий уровень!',
    'next_level_button': 'Перейти на следующий уровень',
    'quiz_lose': 'Ты очень старался! Но пока очков недостаточно. Попробуй пройти викторину еще раз. Или вернись к началу и прочитай сказки снова',
    'return_to_tales_button': 'Вернутся к началу уровня «Сказки»',
}
LEXICON_BA: dict[str, str] = {}

TALES_RU: list[str] = [
    'Вперед! Отправляемся в путь навстречу к сказке!\n\n'
    'Все башкирские сказки можно разделить на 3 группы.\n\n'
    'Первая группа — это волшебные сказки или сказки, в которых происходят чудеса. Герои отправляются в приключение, встречают магического помощника, сражаются с чудищем и, конечно, обязательно побеждают его, чтобы встретить красавицу и стать обладателем чудесных предметов. \n\n'
    'Прочитай сказку «Киизбай и царские дочери», а когда вернешься обратно, нажми кнопку «Идти дальше».',

    'Следующая группа сказок — это сказки о животных.\n\n'
    'В них все звери умеют разговаривать, живут в домах и вообще очень похожи на человека. Они тоже попадают в забавные ситуации, спорят с другими животными, иногда хитрят, проказничают, а иногда сами становятся жертвами своих проделок.\n\n'
    'Прочитай сказку о животных «Лиса-сирота», а когда вернешься обратно, нажми кнопку «Идти дальше».',

    'Наконец, третья группа сказок — бытовые сказки. В них обычно нет чудес, персонажи — это обычные люди, как ты и я. С ними происходят разные истории, в которых им необходимо проявить смекалку, ловкость или проворство. Часто это забавные и смешные сказки, в которых высмеиваются плохие человеческие качества — жадность, глупость, скупость — и восхваляются хорошие — доброта, отзывчивость, смелость.\n\n'
    'Прочитай бытовую сказку «Ленивая девочка», а когда вернешься обратно, нажми кнопку «Идти дальше».',

    'Ты умница! Теперь, когда ты знаешь, какие сказки бывают, пора познакомиться с их персонажами, которые чаще всего встречаются в разных историях.\n\n'
    '<b>Храбрый Егет</b>\n\n'
    'Это главный герой многих башкирских сказок. Он сильный, смелый, умный, проворный и иногда немного по-доброму хитрый. Воплощает самые положительные качества человека. Обязательно уважает родителей, почитает старших и заботиться о младших.\n\n'
    'История начинается, когда егет оставляет отчий дом и отправляется в путь. На пути ему встречаются помощники, который подсказывают верную дорогу, дарят таинственные, но потом обязательно пригождающиеся подарки.\n\n'
    'В сказке егет не всегда побеждает каждого врага, который ему встретится. Одержать верх над злом ему помогают верные друзья, смекалка и доброта.\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.\n\n',

    '<b>Мудрая Красавица</b>\n\n'
    'Женские персонажи в башкирских сказках не просто красавицы, но и умницы. Они сообразительные, трудолюбивые, верные и инициативные. Умеют дать полезный совет или поддержать главного героя, но при необходимости, могут даже войско за собой повести.\n\n'
    'Например, в сказке «Незнай», младшая дочь царя сам ведет войско на битву с двенадцатиглавым дэвом — злым духом, который хочет взять ее в жены.\n\n'
    'А в сказке «Золотые руки», красавица проявляет мудрость, выбрав себе в мужья не самого сильного воина или богатого купца, а…\n\n'
    '… хочешь узнать дальше, тогда скорее нажимай на кнопку «Прочитать сказку». А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.',

    '<b>Хумай</b>\n\n'
    'Это сверхъестественной прекрасная птицей из башкирского фольклора. Ее считают символом счастья и удачи.\n\n'
    'Согласно легендам, Хумай очень красиво поет, и ее появление предвещает начало светлого периода в жизни человека, приход удачи и благополучия. Она становится для главного героя сказки надежным помощником, помогает ценным советом, иногда дарит волшебные подарки.\n\n'
    'Наверное, ты уже встречал похожих птиц в мифологии других народов. Например, бессмертный Феникс из древнегреческой мифологии, который старея, превращается в пепел, но затем снова возрождается из него большой и сильной птицей.\n\n'
    'В славянской мифологии встречается Жар-птица, способная принести счастье тому, кто её поймает. А у древнего народа персов есть истории о Симурге — могучей и мудрой птице, олицетворяющая доброту и ценность знаний.\n\n'
    'Все эти птицы объединяют не только удивительные свойства, но и роль проводников в волшебный мир.\n\n'
    'Хумай встречается во многих сказок, но есть у нее и своя собственная.\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.',

    '<b>Толпар</b>\n\n'
    'Крылатый конь и верный помощник главного героя. Умеет не только летать, но и разговаривать человеческим языком. Благодаря своим огромным чудесным крыльям Толпар может стремительно перемещаться на огромные расстояния. Даже путешествовать между мирами.\n\n'
    'Кроме того, волшебный конь — надежный помощник богатырей в битве, ведь он может метать молнии.\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.',

    '<b>Мяскэй</b>\n\n'
    'Все персонажи, с которыми мы знакомились до этого, были добрыми. Но есть в башкирских сказках и злые герои. Одна из них — старуха Мяскэй — ведьма и оборотень.\n\n'
    'По своим качествам она немного похожа на Бабу-ягу. Но если старуха из русских сказок чаще только пугает героя, а на самом деле может даже помочь, то мяскай до конца вредничает добрым персонажам и даже может быть для них опасной.\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.\n\n',

    '<b>Дэв</b>\n\n'
    'Еще один отрицательный персонаж, который часто встречается в башкирских сказках. Его представляли в виде огромного волосатого и очень неприятного существа.\n\n'
    'У дэва может быть несколько голов: три, девять или двенадцать. Чем больше голов, тем он сильнее. При этом умнее от этого он не становится и часто батыры побеждают противников дэвов не столько силой (ведь чудовища очень сильные), а смекалкой. Или с помощью волшебных помощников и мудрой красавицы.\n\n'
    'Яркий пример такой победы — в сказке «Девушка, егет и дэв».\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше», чтобы познакомиться со следующим персонажем.',

    '<b>Лиса</b>\n\n'
    'В сказках многих народов мира Лиса занимает особое место. Хитренькая и умненькая она обманывает других обитателей леса, получается все, что захочет. Но порой сама же оказывается жертвой своих проделок.\n\n'
    'Хотя в некоторых сказках она проявляет себе, как доброе существо и даже помогает главным героям. Например, в сказке «Биранхылу — дочь бире» лиса выдает себя за дочь царя демонов, чтобы настоящая девушка смогла остаться женой егета.\n\n'
    'Нажми кнопку «Прочитать сказку», чтобы перейти на сайт со сказкой. А когда вернешься обратно, нажми кнопку «Идти дальше».'
]
TALES_BA: list[str] = []

TALES_URL_RU: list[str] = [
    'https://mirckazok.ru/bashkirskie-skazki/kiizbai-i-tcarskie-docheri/',
    'https://mirckazok.ru/bashkirskie-skazki/lisasirota/',
    'https://mirckazok.ru/italianskie-skazki/lenivaia-brucholina/', # поправить
    'https://mirckazok.ru/bashkirskie-skazki/khrabryi-malchik/',
    'https://mirckazok.ru/datskie-skazki/mudraia-koroleva-dagmar/', # поправить
    'https://mirckazok.ru/bashkirskie-skazki/khumaiptitca/',
    'https://mirckazok.ru/bashkirskie-skazki/starik-i-dev/', # поправить
    'https://mirckazok.ru/bashkirskie-skazki/starik-i-dev/', # поправить
    'https://mirckazok.ru/bashkirskie-skazki/starik-i-dev/',
    'https://mirckazok.ru/bashkirskie-skazki/lisa-v-medvezhei-berloge/' # поправить
]
TALES_URL_BA: list[str] = []

LEXICON_RU_LAMBDA: dict = {
    'greeting': lambda x: f'Приятно познакомиться, {x}.\n'
                f'Выбери язык, на котором мы будем общаться.',
}
LEXICON_BA_LAMBDA: dict = {}

INFO_BLOCKS_RU: dict[int, list[str]] = {
    2: [
        'Информация о пословицах и поговорках №1',
        'Информация о пословицах и поговорках №2',
    ],
    3: [
        'Информация о песнях №1',
        'Информация о песнях №2',
        'Информация о песнях №3',
    ],
    4: [
        'Информация о загадках №1',
        'Информация о загадках №2',
    ],
    5: [
        'Информация об эпосах №1',
        'Информация об эпосах №2',
        'Информация об эпосах №3',
        'Информация об эпосах №4'
    ]
}
INFO_BLOCKS_BA: dict[int, list[str]] = {}

END_OF_INFO_RU: dict[int, str] = {
    2: 'Информация о пословицах и поговорках №1',
    3: 'Информация о пословицах и поговорках №1',
    4: 'Информация о пословицах и поговорках №1',
    5: 'Информация о пословицах и поговорках №1',
}
END_OF_INFO_BA: dict[int, str] = {}

LEXICON: dict[str, dict[str, str]] = {
    'ru': LEXICON_RU,
    'ba': LEXICON_BA
}

LEX_LAMBDA: dict[str, dict[str, str]] = {
    'ru': LEXICON_RU_LAMBDA,
    'ba': LEXICON_BA_LAMBDA
}

TALES: dict[str, list[str]] = {
    'ru': TALES_RU,
    'ba': TALES_BA
}

TALES_URL: dict[str, list[str]] = {
    'ru': TALES_URL_RU,
    'ba': TALES_URL_BA
}

INFO_BLOCKS: dict[str, dict[int, list[str]]] = {
    'ru': INFO_BLOCKS_RU,
    'ba': INFO_BLOCKS_BA
}

END_OF_INFO: dict[str, dict[int, str]] = {
    'ru': END_OF_INFO_RU,
    'ba': END_OF_INFO_BA
}