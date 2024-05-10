import tkinter as tk

def on_click(btn_text):
    if btn_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

def get_button_color(text):
    if text == '=':
        return '#99ff99'  # Зеленый цвет для равно
    elif text in ['+', '-', '*', '/']:
        return '#ff9999'  # Красный цвет для операций
    return '#d1d1e0'  # Серый цвет для остальных кнопок

root = tk.Tk()
root.title("Красочный калькулятор")
root.configure(bg='#f0f0f0')  # устанавливаем цвет фона

entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for text in buttons:
    btn_color = get_button_color(text)
    btn = tk.Button(root, text=text, width=5, height=2, bg=btn_color, font=('Arial', 12, 'bold'), command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
