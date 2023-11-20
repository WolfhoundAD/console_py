import tkinter as tk

def greet():
    name = name_entry.get()
    age = age_entry.get()

    try:
        age = int(age)
        greeting_label.config(text=f"Привет, {name}! Вам {age} года(лет).")
    except ValueError:
        greeting_label.config(text="Ошибка: введите числовое значение для возраста.")

root = tk.Tk()
root.title("Приветствие")

# Создание метки для имени
name_label = tk.Label(root, text="Введите ваше имя:")
name_label.pack()

# Поле для ввода имени
name_entry = tk.Entry(root)
name_entry.pack()

# Создание метки для возраста
age_label = tk.Label(root, text="Введите ваш возраст:")
age_label.pack()

# Поле для ввода возраста
age_entry = tk.Entry(root)
age_entry.pack()

# Кнопка для отправки данных
submit_button = tk.Button(root, text="Поприветствовать", command=greet)
submit_button.pack()

# Метка для отображения приветствия
greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()
