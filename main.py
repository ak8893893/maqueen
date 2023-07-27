def on_forever():
    music.play(music.string_playable("E E F G G F E D C C D E E D D - E E F G G F E D C C D E D C C - D D E C D E F E C D E F E D C D -", 240),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("- - - - - - - - ", 112),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
