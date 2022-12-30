basic.forever(function () {
    if (input.temperature() >= 20) {
        basic.showString("" + (input.temperature()))
    } else {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.mysterious), SoundExpressionPlayMode.UntilDone)
        basic.showString("!!!!")
        basic.showString("" + (input.temperature()))
    }
    basic.pause(5000)
})
