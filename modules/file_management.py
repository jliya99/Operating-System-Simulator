import tkinter as tk
from tkinter import messagebox
import os


# ==========================================
# DATA FOLDER
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FOLDER = os.path.join(
    BASE_DIR,
    "data"
)

os.makedirs(
    DATA_FOLDER,
    exist_ok=True
)


# ==========================================
# FILE MANAGEMENT CLASS
# ==========================================

class FileManagement:

    def __init__(self, parent):

        self.parent = parent

        self.window = tk.Toplevel(parent)
        self.window.title("File Management")
        self.window.geometry("900x750")
        self.window.configure(bg="#0f172a")

        self.create_interface()
        self.load_files()

    # ==========================================
    # INTERFACE
    # ==========================================

    def create_interface(self):

        tk.Label(
            self.window,
            text="FILE MANAGEMENT",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=25)

        # ==========================================
        # FILE NAME SECTION
        # ==========================================

        input_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=25,
            pady=20
        )

        input_frame.pack(
            padx=30,
            pady=15,
            fill="x"
        )

        tk.Label(
            input_frame,
            text="File Name",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.filename_entry = tk.Entry(
            input_frame,
            width=25,
            font=("Arial", 11)
        )

        self.filename_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        # ==========================================
        # CREATE BUTTON
        # ==========================================

        tk.Button(
            input_frame,
            text="Create File",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            width=15,
            command=self.create_file
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        # ==========================================
        # DELETE BUTTON
        # ==========================================

        tk.Button(
            input_frame,
            text="Delete File",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            width=15,
            command=self.delete_file
        ).grid(
            row=0,
            column=3,
            padx=10
        )

        # ==========================================
        # FILE LIST
        # ==========================================

        tk.Label(
            self.window,
            text="FILE LIST",
            font=("Arial", 17, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=10)

        list_frame = tk.Frame(
            self.window
        )

        list_frame.pack(
            padx=30,
            fill="x"
        )

        self.file_listbox = tk.Listbox(
            list_frame,
            height=5,
            font=("Arial", 12)
        )

        self.file_listbox.pack(
            fill="x"
        )

        # Select file event
        self.file_listbox.bind(
            "<<ListboxSelect>>",
            self.select_file
        )

        # ==========================================
        # FILE CONTENT
        # ==========================================

        tk.Label(
            self.window,
            text="FILE CONTENT",
            font=("Arial", 17, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=15)

        self.content_text = tk.Text(
            self.window,
            height=5,
            font=("Arial", 11)
        )

        self.content_text.pack(
            padx=30,
            fill="x"
        )

        # ==========================================
        # READ / WRITE BUTTONS
        # ==========================================

        button_frame = tk.Frame(
            self.window,
            bg="#0f172a"
        )

        button_frame.pack(
            pady=20
        )

        # Read Button

        tk.Button(
            button_frame,
            text="Read File",
            font=("Arial", 11, "bold"),
            bg="#16a34a",
            fg="white",
            width=18,
            command=self.read_file
        ).pack(
            side="left",
            padx=10
        )

        # Write Button

        tk.Button(
            button_frame,
            text="Write File",
            font=("Arial", 11, "bold"),
            bg="#7c3aed",
            fg="white",
            width=18,
            command=self.write_file
        ).pack(
            side="left",
            padx=10
        )

        # Refresh Button

        tk.Button(
            button_frame,
            text="Refresh",
            font=("Arial", 11, "bold"),
            bg="#475569",
            fg="white",
            width=18,
            command=self.load_files
        ).pack(
            side="left",
            padx=10
        )

    # ==========================================
    # LOAD EXISTING FILES
    # ==========================================

    def load_files(self):

        self.file_listbox.delete(
            0,
            tk.END
        )

        for filename in sorted(
            os.listdir(DATA_FOLDER)
        ):

            if filename.lower().endswith(".txt"):

                self.file_listbox.insert(
                    tk.END,
                    filename
                )

    # ==========================================
    # GET FILE NAME
    # ==========================================

    def get_filename(self):

        filename = self.filename_entry.get().strip()

        if not filename:

            messagebox.showwarning(
                "Missing File Name",
                "Please enter a file name."
            )

            return None

        # Prevent folder/path input

        if os.path.basename(filename) != filename:

            messagebox.showerror(
                "Invalid File Name",
                "Please enter only a file name."
            )

            return None

        # Automatically add .txt

        if not filename.lower().endswith(".txt"):

            filename += ".txt"

        return filename

    # ==========================================
    # CREATE FILE
    # ==========================================

    def create_file(self):

        filename = self.get_filename()

        if not filename:
            return

        file_path = os.path.join(
            DATA_FOLDER,
            filename
        )

        # Check existing file

        if os.path.exists(file_path):

            messagebox.showerror(
                "File Exists",
                "This file already exists."
            )

            return

        # Create actual file

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ):
                pass

            self.load_files()

            self.filename_entry.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Success",
                f"File '{filename}' created successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not create file.\n{e}"
            )

    # ==========================================
    # DELETE FILE
    # ==========================================

    def delete_file(self):

        selected = self.file_listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "No File Selected",
                "Please select a file first."
            )

            return

        filename = self.file_listbox.get(
            selected[0]
        )

        file_path = os.path.join(
            DATA_FOLDER,
            filename
        )

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{filename}'?"
        )

        if not confirm:
            return

        try:

            os.remove(file_path)

            self.load_files()

            self.content_text.delete(
                "1.0",
                tk.END
            )

            self.filename_entry.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Deleted",
                f"File '{filename}' deleted successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not delete file.\n{e}"
            )

    # ==========================================
    # WRITE FILE
    # ==========================================

    def write_file(self):

        selected = self.file_listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "No File Selected",
                "Please select a file first."
            )

            return

        filename = self.file_listbox.get(
            selected[0]
        )

        file_path = os.path.join(
            DATA_FOLDER,
            filename
        )

        content = self.content_text.get(
            "1.0",
            "end-1c"
        )

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)

            messagebox.showinfo(
                "Write Successful",
                f"Content written to '{filename}'."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not write file.\n{e}"
            )

    # ==========================================
    # READ FILE
    # ==========================================

    def read_file(self):

        selected = self.file_listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "No File Selected",
                "Please select a file first."
            )

            return

        filename = self.file_listbox.get(
            selected[0]
        )

        file_path = os.path.join(
            DATA_FOLDER,
            filename
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            self.content_text.delete(
                "1.0",
                tk.END
            )

            self.content_text.insert(
                "1.0",
                content
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Could not read file.\n{e}"
            )

    # ==========================================
    # SELECT FILE
    # ==========================================

    def select_file(self, event=None):

        selected = self.file_listbox.curselection()

        if not selected:
            return

        filename = self.file_listbox.get(
            selected[0]
        )

        self.filename_entry.delete(
            0,
            tk.END
        )

        self.filename_entry.insert(
            0,
            filename
        )