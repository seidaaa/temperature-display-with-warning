def on_forever():
    if input.temperature() >= 20:
        basic.show_string("" + str((input.temperature())))
    else:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.mysterious),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_string("!!!!")
        basic.show_string("" + str((input.temperature())))
    basic.pause(5000)
basic.forever(on_forever)
