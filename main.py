import keyboard as kb
import tkinter as tk
import json

with open("macros.json", "r") as f:
    macros = json.load(f)

active_macros = {}

for m in macros:
    active_macros[m] = False

def checked(m):
    active_macros[m] = not active_macros[m]
    print(active_macros[m])
    

app = tk.Tk()
app.title("Macros")

tk.Label(app, text="Active macros:").pack()
for m in macros:
    tk.Checkbutton(app, text=f"{m} = {macros[m]}", command=lambda: checked(m)).pack()

app.mainloop()