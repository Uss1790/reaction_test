let counter = 0
let i = 0
let start = 0
let ende = 0
let Time_taken = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    counter = 3
    while (i <= counter + 1 - 1) {
        basic.showNumber(3 - i)
        basic.pause(100)
        i += 1
    }
    basic.clearScreen()
    basic.pause((Math.random() * 3 + 2) * 1000)
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
    start = control.millis()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (start != 0) {
        ende = control.millis()
        Time_taken = (ende - start) / 1000
        basic.clearScreen()
        basic.pause(500)
        for (let index = 0; index < 3; index++) {
            basic.showNumber(Time_taken)
        }
        start = 0
    }
    
})
basic.forever(function on_forever() {
    
})
