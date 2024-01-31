def on_forever():
    basic.show_string("" + str((input.magnetic_force(Dimension.STRENGTH))), 150)
basic.forever(on_forever)
