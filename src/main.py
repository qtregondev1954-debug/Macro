
import tkinter as tk
from tkinter import filedialog
import json, pyautogui, time, os

current_macro=None

def load_macro():
    global current_macro
    path=filedialog.askopenfilename(initialdir="saves",filetypes=[("Macro","*.json")])
    if path:
        with open(path,"r",encoding="utf-8") as f:
            current_macro=json.load(f)

def play():
    if not current_macro: return
    for a in current_macro["actions"]:
        if a["type"]=="key":
            for _ in range(a.get("repeat",1)):
                pyautogui.press(a["key"])
                time.sleep(a.get("interval",0.1))
        if a["type"]=="mouse":
            pyautogui.mouseDown(button=a["button"])
            time.sleep(a["hold"])
            pyautogui.mouseUp(button=a["button"])

root=tk.Tk()
root.title("Macro Engine")
tk.Button(root,text="Load Macro",command=load_macro).pack()
tk.Button(root,text="Start",command=play).pack()
root.mainloop()
