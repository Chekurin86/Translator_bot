import random

LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ бот-переводчик для перевода текста с английского на русский язык и наоборот.\n'
              'Если хотите более подробно изучить мою работу можете\n'
              'отправить команду /help',
    '/help': 'Я принимаю от вас текст на английском или русском языках и при помощи интернета\n'
            'перевожу вам его на другой язык. Т.е. если вы напишете слово на русском, \n'
             'я напишу вам перевод этого слова на ангийском языке, и наоборот.',
    'error': 'Извините, я могу переводить только текст...'
}

def get_random_phrase() -> str:
    return random.choice([
        'Сейчас я быстро найду перевод...',
        "Я знаю как это перевести, секундочку...",
        "Я быстро это переведу",
        "Я постараюсь это быстро перевести",
        "Мне уже попадался подобный текст, я его быстро переведу!",
        "Сейчас, один момент...",
        "Я занимаюсь переводом уже давно, так что быстро переведу ваш текст"
    ])





