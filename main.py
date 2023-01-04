from playsound import playsound

SYMBOL_SOUND_DICT = {
    '.': '/Users/raahim/Desktop/Python/morsecode_player/short_beep.mp3',
    '-': '/Users/raahim/Desktop/Python/morsecode_player/long_beep.mp3',
}

morsecode = input('Enter morsecode: ')

for symbol in morsecode:
    try:
        playsound(SYMBOL_SOUND_DICT[symbol])
    except KeyError:
        None
