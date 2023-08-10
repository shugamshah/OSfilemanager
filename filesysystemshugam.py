import tkinter as tk
from tkinter import filedialog
import os

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shugam File System")
        self.root.configure(background='#333333', width=500, height=300)

        self.create_file_button = tk.Button(self.root, text="Create File", command=self.create_file, bg='#ffffff', fg='#000000')
        self.create_file_button.pack(padx=20, pady=10)

        self.list_hidden_files_button = tk.Button(self.root, text="List Hidden Files", command=self.list_hidden_files, bg='#ffffff', fg='#000000')
        self.list_hidden_files_button.pack(padx=20, pady=10)

        self.write_file_button = tk.Button(self.root, text="Write to File", command=self.write_file, bg='#ffffff', fg='#000000')
        self.write_file_button.pack(padx=20, pady=10)

        self.read_file_button = tk.Button(self.root, text="Read File", command=self.read_file, bg='#ffffff', fg='#000000')
        self.read_file_button.pack(padx=20, pady=10)

        self.delete_file_button = tk.Button(self.root, text="Delete File", command=self.delete_file, bg='#ffffff', fg='#000000')
        self.delete_file_button.pack(padx=20, pady=10)

        self.permission_button = tk.Button(self.root, text="Set Permissions", command=self.setpermissions, bg='#ffffff', fg='#000000')
        self.permission_button.pack(padx=20, pady=10)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit, bg='#ffffff', fg='#000000')
        self.exit_button.pack(padx=20, pady=10)

        
        


    def create_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w'):
                    tk.messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' created.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def list_hidden_files(self):
        files = os.listdir('.')
        hidden_files = [f for f in files if f.startswith('.')]
        tk.messagebox.showinfo("Hidden Files", hidden_files)

    def write_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            content = input("Enter the content: ")
            with open(file_path, 'w') as f:
                f.write(content)
            tk.messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' written.")

    def read_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                content = f.read()
            tk.messagebox.showinfo("File Content", content)

    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.remove(file_path)
            tk.messagebox.showinfo("Success", f"File '{os.path.basename(file_path)}' deleted.")
            

    def exit(self):
        self.root.destroy()

    def setpermissions(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            permissions = input("Enter the permissions (e.g. 777): ")
            try:
                os.chmod(file_path, int(permissions))
                tk.messagebox.showinfo("Success", f"Permissions for file '{os.path.basename(file_path)}' set to {permissions}.")
            except ValueError:
                tk.messagebox.showinfo("Error", f"Invalid permissions: {permissions}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()