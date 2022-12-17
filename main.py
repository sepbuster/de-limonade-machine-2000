def on_button_pressed_a():
    global smaak3
    smaak3 = "tropical"
    smaakkeuze(smaak3)
    betaling(smaak3)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global smaak3
    smaak3 = "framboos"
    smaakkeuze(smaak3)
    betaling(smaak3)
input.on_button_pressed(Button.B, on_button_pressed_b)

def betaling(smaak: str):
    OLED.clear()
    OLED.write_string_new_line("gooi er een euro in")
    while True:
        if pins.digital_read_pin(DigitalPin.P0) == 0:
            break
    OLED.clear()
    OLED.write_string_new_line("u heeft betaald")
    OLED.write_string_new_line("")
    OLED.write_string_new_line("plaats een bekertje")
def smaakkeuze(smaak2: str):
    OLED.clear()
    OLED.write_string_new_line("U koos voor " + smaak2)
    basic.pause(3000)
smaak3 = ""
OLED.init(128, 64)
OLED.write_string_new_line("kies een limo smaak")
OLED.write_string_new_line("")
OLED.write_string_new_line("a=tropical")
OLED.write_string_new_line("")
OLED.write_string_new_line("b=framboos")