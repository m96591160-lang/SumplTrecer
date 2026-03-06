import tkinter as tk
from tkinter import messagebox
import winreg

def unlok():
    results = []
    
root = tk.Tk()

root.title("SumpleTvinker") #заголовок
root.geometry("700x300") #размер

btn = tk.Button(root, text="Unloc", command=unlok)

btn.pack(pady=20)

btn2 = tk.Button(root, text="Сканирование")
btn2.pack(pady=20)

btn3 = tk.Button(root, text="Диспетчир задач")
btn3.pack(pady=30)

root.mainloop()