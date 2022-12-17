def on_button_pressed_a():
    global smaak3, betaald
    smaak3 = "tropical"
    smaakkeuze(smaak3)
    betaald = 0
    betaling(smaak3)
    controleer_bekertje()
    schenk_limonade()
    begin()
input.on_button_pressed(Button.A, on_button_pressed_a)

def begin():
    global betaald
    pins.digital_write_pin(DigitalPin.P0, 1)
    betaald = 0
    OLED.clear()
    OLED.write_string_new_line("kies een limo smaak")
    OLED.write_string_new_line("")
    OLED.write_string_new_line("a=tropical")
    OLED.write_string_new_line("")
    OLED.write_string_new_line("b=framboos")

def on_button_pressed_b():
    global smaak3, betaald
    smaak3 = "framboos"
    smaakkeuze(smaak3)
    betaald = 0
    betaling(smaak3)
    controleer_bekertje()
    schenk_limonade()
    begin()
input.on_button_pressed(Button.B, on_button_pressed_b)

def betaling(smaak: str):
    global betaald
    OLED.clear()
    OLED.write_string_new_line("gooi er een euro in")
    while True:
        if pins.digital_read_pin(DigitalPin.P0) == 0:
            betaald = 1
            break
    OLED.clear()
    OLED.write_string_new_line("u heeft betaald")
    basic.pause(3000)
def schenk_limonade():
    for index in range(101):
        OLED.draw_loading(index)
        basic.pause(30)
    basic.pause(1000)
    OLED.clear()
    OLED.write_string_new_line("drink smakelijk")
    basic.pause(5000)
def smaakkeuze(smaak2: str):
    OLED.clear()
    OLED.write_string_new_line("U koos voor " + smaak2)
    basic.pause(3000)
def controleer_bekertje():
    global afstand
    OLED.clear()
    OLED.write_string_new_line("plaats een bekertje")
    while True:
        afstand = sonar.ping(DigitalPin.P13, DigitalPin.P15, PingUnit.CENTIMETERS)
        if afstand < 4:
            OLED.clear()
            OLED.write_string_new_line("limonade wordt geschonken")
            basic.pause(2000)
            break
afstand = 0
betaald = 0
smaak3 = ""
OLED.init(128, 64)
OLED.clear()
OLED.write_string_new_line("kies een limo smaak")
OLED.write_string_new_line("")
OLED.write_string_new_line("a=tropical")
OLED.write_string_new_line("")
OLED.write_string_new_line("b=framboos")