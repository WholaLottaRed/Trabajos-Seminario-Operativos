import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current_text = screen.get()
        current_text += text
        screen.set(current_text)

root = tk.Tk()
root.title("Calculadora")

# Pantalla
screen = tk.StringVar()
screen.set("")
entry = tk.Entry(root, textvar=screen, font="Helvetica 20")
entry.pack(fill=tk.BOTH, expand=True)

# Botones
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

button_frame = tk.Frame(root)
button_frame.pack()

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="Helvetica 15", width=5, height=2)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

root.mainloop()