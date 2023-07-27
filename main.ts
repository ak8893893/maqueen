music.play(music.stringPlayable("E E F G G F E D C C D E E D D - E E F G G F E D C C D E D C C - D D E C D E F E C D E F E D C D -", 240), music.PlaybackMode.LoopingInBackground)
basic.forever(function on_forever() {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 200)
    }
    
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 200)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 10)
    }
    
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 10)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 200)
    }
    
})
