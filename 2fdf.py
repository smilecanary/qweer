import tkinter as tk
from tkinter import messagebox

class AddCategoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Добавление категории")
        self.frame = tk.Frame(root, padx=15, pady=15)
        self.frame.pack()
        self.label_name = tk.Label(self.frame, text="Название категории:")
        self.label_name.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_name = tk.Entry(self.frame, width=40)
        self.entry_name.grid(row=0, column=1, pady=5)
        self.label_desc = tk.Label(self.frame, text="Описание:")
        self.label_desc.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_desc = tk.Entry(self.frame, width=40)
        self.entry_desc.grid(row=1, column=1, pady=5)
        self.add_button = tk.Button(self.frame, text="Добавить", command=self.add_category)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_category(self):
        name = self.entry_name.get()
        desc = self.entry_desc.get()
        try:
            new_category_id = add_category_to_db(name, desc)
            messagebox.showinfo("Успех", f"Категория '{name}' успешно добавлена!\nID: {new_category_id}")
            self.entry_name.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        except ValueError as ve:
            messagebox.showwarning("Внимание", str(ve))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении категории:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddCategoryApp(root)
    root.mainloop()