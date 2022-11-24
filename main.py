counter = 0
i = 0
start = 0
ende = 0
Time_taken = 0

def on_button_pressed_a():
    global counter, i, start
    counter = 3
    while i <= counter + 1 - 1:
        basic.show_number(3 - i)
        basic.pause(100)
        i += 1
    basic.clear_screen()
    basic.pause((Math.random() * 3 + 2)*1000)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    start = control.millis()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global ende, Time_taken, start
    if start != 0:
        ende = control.millis()
        Time_taken = (ende - start) / 1000
        basic.clear_screen()
        basic.pause(500)
        for index in range(3):
            basic.show_number(Time_taken)
        start = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
