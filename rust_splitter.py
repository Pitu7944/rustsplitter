import pyautogui, keyboard, time, sys
pyautogui.FAILSAFE = True
global exit 
globals()['exit'] = True
def split_furnance(type, _):
    if type == 'Inventory':
        i = 1
        pyautogui.click(1000, 623, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
        i += 1
        pyautogui.click(827, 514, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
        i += 1
        pyautogui.moveTo(1198, 504, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
        i += 1
        pyautogui.drag(0, 100, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
        i += 1
        pyautogui.moveTo(1200, 500, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
        i += 1
        pyautogui.drag(-100, 100, duration = 0.17)
        print_percent_done(i,7, title="Splitting Inventory")
    if type == 'Furnance_Small':
        i = 1
        pyautogui.moveTo(1190, 620, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.drag(115,105, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.click(1300,720,duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.click(827, 514, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.moveTo(1200, 500, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.drag(300, 220, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.moveTo(1200, 500, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
        i += 1
        pyautogui.drag(200, 220, duration = 0.17)
        print_percent_done(i,9, title="Splitting Small Furnance")
    if type == 'exit':
        globals()['exit'] = False

keyboard.add_hotkey('f6', split_furnance, args=('Inventory', ''))
keyboard.add_hotkey('shift+f6', split_furnance, args=('Furnance_Small', ''))
keyboard.add_hotkey('shift+f5', split_furnance, args=('exit', ''))

def write_cui():
    print("\t+--------------------------------------------------+")
    print("\t| [F6] Split ore in Inventory                      |")
    print("\t| [Shift + F6] Split ore in Furnance               |")
    print("\t| [Shift + F5] Exit Program                        |")
    print("\t+--------------------------------------------------+")

def print_percent_done(index, total, bar_len=8, title='Please wait'):
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)
    done = round(percent_done/(100/bar_len))
    togo = bar_len-done
    done_str = '█'*int(done)
    togo_str = '░'*int(togo)
    print(f'\t  ⏳ {title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')
    if round(percent_done) == 100:
        print('\t  ✅')

write_cui()
while globals()['exit']:
    pass