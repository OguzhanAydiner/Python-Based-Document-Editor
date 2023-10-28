import tkinter as tk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        root.title("Simple Text Editor")

        # Create text widget
        self.text = tk.Text(root, wrap='word', undo=True)
        self.text.pack(expand=1, fill='both')

        # Create font object
        self.text_font = font.Font(family='Arial', size=12)
        self.text.configure(font=self.text_font)

        # Create Menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # File Menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As", command=self.save_as)

        # Options Menu
        self.options_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="Font Size", command=self.set_font_size)
        self.options_menu.add_command(label="Font Color", command=self.set_font_color)

        # Help Menu
        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        with open(filepath, 'r') as file:
            text = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, text)

    def save_as(self):
        filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, 'w') as file:
            text = self.text.get(1.0, tk.END)
            file.write(text)

    def set_font_size(self):
        size = tk.simpledialog.askinteger("Font Size", "Enter font size:")
        if size:
            self.text_font.configure(size=size)

    def set_font_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text.configure(fg=color)

    def show_about(self):
        tk.messagebox.showinfo("About", "Simple Text Editor\nCreated with Python and Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()