import tkinter as tk
window = tk.Tk()
label = tk.Label(
    text="jambo!",
    fg="white",
    bg="black",
    width=15,
    height=15
)

button = tk.Button(text="button1")


label.pack()
button.pack()
window.mainloop()

