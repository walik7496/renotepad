import tkinter as tk
from tkinter import scrolledtext, filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("ReNotepad")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(expand=True, fill='both')

        # Menu
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # File
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

        # Help
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def about(self):
        about_text = "This Notepad is written in Python."
        tk.messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()