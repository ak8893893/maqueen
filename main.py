music.play(music.string_playable("E E F G G F E D C C D E E D D - E E F G G F E D C C D E D C C - D D E C D E F E C D E F E D C D -", 240),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 200)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 10)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 10)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)
basic.forever(on_forever)
