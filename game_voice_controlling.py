import speech_recognition as sr
import keyboard
import mouse
from unidecode import unidecode
from time import sleep

r = sr.Recognizer()


def aperta(tecla):
    keyboard.press(tecla)
    sleep(0.25)
    keyboard.release(tecla)


def up():
    mouse.move(0, -85, False)


def down():
    mouse.move(0, 85, False)


def left():
    mouse.move(-150, 0, False)


def right():
    mouse.move(150, 0, False)


while True:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.record(source2, 2.3)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2, language='pt-BR')
            MyText = unidecode(MyText.lower())

            print(MyText)

            if ('pular' in MyText) or ('jump' in MyText):
                aperta('space')

            if ('andar' in MyText) or ('walk' in MyText):
                anda = 'w'
                keyboard.press(anda)

            if ('correr' in MyText) or ('run' in MyText):
                corre = 'w + ctrl'
                keyboard.press(corre)

            if ('atras' in MyText) or ('back' in MyText):
                atras = 's'
                keyboard.press(atras)

            if ('direita' in MyText) or ('right' in MyText):
                direita = 'd'
                keyboard.press(direita)

            if ('esquerda' in MyText) or ('left' in MyText):
                esquerda = 'a'
                keyboard.press(esquerda)

            if ('agachar' in MyText) or ('crouch' in MyText):
                agachar = 'shift'
                keyboard.press(agachar)

            if ('atacar' in MyText) or ('attack' in MyText):
                ataque = 'left'
                mouse.click(ataque)

            if ('colocar' in MyText) or ('place' in MyText):
                coloca = 'right'
                mouse.click(coloca)

            if ('subir' in MyText) or ('go up' in MyText):
                coloca = 'right'
                aperta('space')
                mouse.click(coloca)

            if ('quebrar' in MyText) or ('break' in MyText):
                quebra = 'left'
                mouse.press(quebra)
                sleep(3.5)
                mouse.release(quebra)

            if ('soltar' in MyText) or ('drop' in MyText):
                aperta('q')

            if ('inventario' in MyText) or ('inventory' in MyText):
                aperta('e')

            if ('um' in MyText) or ('one' in MyText) or ('1' in MyText):
                aperta('1')

            if ('dois' in MyText) or ('two' in MyText) or ('2' in MyText):
                aperta('2')

            if ('tres' in MyText) or ('three' in MyText) or ('3' in MyText):
                aperta('3')

            if ('quatro' in MyText) or ('four' in MyText) or ('4' in MyText):
                aperta('4')

            if ('cinco' in MyText) or ('five' in MyText) or ('5' in MyText):
                aperta('5')

            if ('seis' in MyText) or ('six' in MyText) or ('6' in MyText):
                aperta('6')

            if ('sete' in MyText) or ('seven' in MyText) or ('7' in MyText):
                aperta('7')

            if ('oito' in MyText) or ('eight' in MyText) or ('8' in MyText):
                aperta('8')

            if ('nove' in MyText) or ('nine' in MyText) or ('9' in MyText):
                aperta('9')

            if ('parar' in MyText) or ('stop' in MyText) or ('three' in MyText):
                keyboard.release('w')
                keyboard.release('s')
                keyboard.release('d')
                keyboard.release('a')
                keyboard.release('shift')
                keyboard.release('ctrl')

            if ('cima' in MyText) or ('up' in MyText):
                up()

            if ('baixo' in MyText) or ('down' in MyText):
                down()

            if ('lado esquerdo' in MyText) or ('left side' in MyText):
                left()

            if ('lado direito' in MyText) or ('right side' in MyText):
                right()

            if ('centralizar' in MyText) or ('centralize' in MyText):
                mouse.move(683, 384)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
