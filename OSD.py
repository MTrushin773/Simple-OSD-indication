import tkinter as tk
import ctypes
from ctypes import wintypes, byref, Structure
import winsound
import time
import threading

try:
    import psutil
    psutil_ok = True
except:
    psutil_ok = False

VK_CAPITAL = 0x14
VK_NUMLOCK = 0x90

class POWER_STATUS(Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

def key_state(vk):
    s = ctypes.windll.user32.GetKeyState(vk)
    return (s & 0x0001) != 0

def lang_id():
    h = ctypes.windll.user32.GetForegroundWindow()
    t = ctypes.windll.user32.GetWindowThreadProcessId(h, None)
    l = ctypes.windll.user32.GetKeyboardLayout(t)
    return l & 0xFFFF

def power_status():
    s = POWER_STATUS()
    if ctypes.windll.kernel32.GetSystemPowerStatus(byref(s)):
        return s.ACLineStatus
    return None

def cpu_temp():
    if not psutil_ok:
        return None
    try:
        t = psutil.sensors_temperatures()
        for name, entries in t.items():
            if entries:
                return entries[0].current
        return None
    except:
        return None

langs = {
    0x0409: 'English (US)',
    0x0419: 'Russian',
    0x040C: 'French',
    0x0407: 'German',
}

def beep():
    def _b():
        try:
            winsound.Beep(800, 200)
            time.sleep(0.2)
            winsound.Beep(800, 200)
        except:
            pass
    threading.Thread(target=_b, daemon=True).start()

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.attributes('-topmost', True)

        self.win = None
        self.timer = None

        self.prev = {
            'caps': key_state(VK_CAPITAL),
            'num': key_state(VK_NUMLOCK),
            'lang': lang_id(),
            'power': power_status(),
        }

        self.alarm83 = False
        self.alarm91 = False
        self.last_temp = None

        self.check()

    def show(self, text, icon='', dur=2000):
        if self.win:
            self.win.destroy()
            self.win = None
        if self.timer:
            self.root.after_cancel(self.timer)
            self.timer = None

        w = tk.Toplevel(self.root)
        w.overrideredirect(True)
        w.attributes('-topmost', True)
        w.attributes('-alpha', 0.92)
        w.configure(bg='#2c2c2c')

        txt = f"{icon} {text}" if icon else text
        lb = tk.Label(w, text=txt, font=('Segoe UI', 16),
                      fg='white', bg='#2c2c2c', padx=25, pady=12)
        lb.pack()

        w.update_idletasks()
        sw = w.winfo_screenwidth()
        sh = w.winfo_screenheight()
        x = (sw - w.winfo_reqwidth()) // 2
        y = (sh - w.winfo_reqheight()) // 2
        w.geometry(f'+{x}+{y}')

        w.deiconify()
        self.win = w
        self.timer = self.root.after(dur, self.hide)

    def hide(self):
        if self.win:
            self.win.destroy()
            self.win = None
        self.timer = None

    def check(self):
        c = key_state(VK_CAPITAL)
        if c != self.prev['caps']:
            self.prev['caps'] = c
            self.show('Caps Lock ON' if c else 'Caps Lock OFF', '⬆' if c else '⬇')

        n = key_state(VK_NUMLOCK)
        if n != self.prev['num']:
            self.prev['num'] = n
            self.show('Num Lock ON' if n else 'Num Lock OFF', '🔢')

        l = lang_id()
        if l != self.prev['lang']:
            self.prev['lang'] = l
            self.show(langs.get(l, f'Lang {l:04X}'), '🌐')

        p = power_status()
        if p is not None and p != self.prev['power']:
            self.prev['power'] = p
            if p == 1:
                self.show('Charger connected', '⚡')
            elif p == 0:
                self.show('Charger disconnected', '🔋')
            else:
                self.show('Power status unknown', '❓')

        if psutil_ok:
            t = cpu_temp()
            if t is not None:
                if t > 83.0:
                    if not self.alarm83:
                        beep()
                        self.alarm83 = True
                    if t >= 91.0 and not self.alarm91:
                        beep()
                        self.alarm91 = True
                else:
                    if t < 80.0:
                        self.alarm83 = False
                        self.alarm91 = False

        self.root.after(150, self.check)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()