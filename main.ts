basic.forever(function on_forever() {
    music.play(music.stringPlayable("E E F G G F E D C C D E E D D - E E F G G F E D C C D E D C C - D D E C D E F E C D E F E D C D -", 240), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("- - - - - - - - ", 112), music.PlaybackMode.UntilDone)
})
