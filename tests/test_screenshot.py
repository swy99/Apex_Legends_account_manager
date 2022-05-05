import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Lib import screenshot
import pynput
from pynput import keyboard

if __name__ == '__main__':
    def on_press(key):
        if key == keyboard.Key.f10:
            return False
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
    img = screenshot.screenshot()
    name = input()
    img.save("./screenshots/" + name + ".jpg", 'JPEG')