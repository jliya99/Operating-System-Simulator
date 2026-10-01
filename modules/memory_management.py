import tkinter as tk
from tkinter import ttk, messagebox


class MemoryManagement:

    def __init__(self, parent):

        self.parent = parent
        self.page_table = []

        self.window = tk.Toplevel(parent)
        self.window.title("Memory Management")
        self.window.geometry("1000x750")
        self.window.configure(bg="#0f172a")

        self.create_interface()

    # ==========================================
    # MAIN INTERFACE
    # ==========================================
    def create_interface(self):

        tk.Label(
            self.window,
            text="MEMORY MANAGEMENT",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=15)

        # ==========================================
        # PAGING
        # ==========================================
        tk.Label(
            self.window,
            text="PAGING",
            font=("Arial", 17, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        input_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=20,
            pady=15
        )

        input_frame.pack(
            padx=30,
            pady=10,
            fill="x"
        )

        # Page
        tk.Label(
            input_frame,
            text="Page Number",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        self.page_entry = tk.Entry(
            input_frame,
            width=12
        )

        self.page_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        # Frame
        tk.Label(
            input_frame,
            text="Frame Number",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=2, padx=10)

        self.frame_entry = tk.Entry(
            input_frame,
            width=12
        )

        self.frame_entry.grid(
            row=0,
            column=3,
            padx=10
        )

        # Allocate
        tk.Button(
            input_frame,
            text="Allocate Page",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            width=16,
            command=self.allocate_page
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        # Clear
        tk.Button(
            input_frame,
            text="Clear Paging",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            width=16,
            command=self.clear_paging
        ).grid(
            row=0,
            column=5,
            padx=10
        )

        # ==========================================
        # PAGE TABLE
        # ==========================================
        tk.Label(
            self.window,
            text="PAGE TABLE",
            font=("Arial", 15, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=5)

        table_frame = tk.Frame(self.window)
        table_frame.pack(
            padx=30,
            fill="x"
        )

        columns = (
            "Page Number",
            "Frame Number",
            "Status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=5
        )

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=200,
                anchor="center"
            )

        self.tree.pack(
            fill="x"
        )

        # ==========================================
        # PAGE REPLACEMENT
        # ==========================================
        tk.Label(
            self.window,
            text="PAGE REPLACEMENT",
            font=("Arial", 17, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(20, 5))

        replacement_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=20,
            pady=15
        )

        replacement_frame.pack(
            padx=30,
            fill="x"
        )

        # Reference String
        tk.Label(
            replacement_frame,
            text="Reference String",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        self.reference_entry = tk.Entry(
            replacement_frame,
            width=35
        )

        self.reference_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        # Frames
        tk.Label(
            replacement_frame,
            text="Frames",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.frames_entry = tk.Entry(
            replacement_frame,
            width=8
        )

        self.frames_entry.grid(
            row=0,
            column=3,
            padx=10
        )

        # Algorithm
        tk.Label(
            replacement_frame,
            text="Algorithm",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=15
        )

        self.algorithm = ttk.Combobox(
            replacement_frame,
            values=["FIFO", "LRU"],
            state="readonly",
            width=15
        )

        self.algorithm.set("FIFO")

        self.algorithm.grid(
            row=1,
            column=1,
            padx=10,
            pady=15
        )

        # Run
        tk.Button(
            replacement_frame,
            text="RUN PAGE REPLACEMENT",
            font=("Arial", 11, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            command=self.run_replacement
        ).grid(
            row=1,
            column=2,
            columnspan=2,
            padx=10
        )

        # ==========================================
        # RESULT
        # ==========================================
        self.result_label = tk.Label(
            self.window,
            text="Page Faults: -    |    Page Hits: -",
            font=("Arial", 13, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        self.result_label.pack(pady=15)

        # Replacement result
        self.replacement_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 11, "bold"),
            bg="#0f172a",
            fg="white"
        )

        self.replacement_label.pack()

    # ==========================================
    # ALLOCATE PAGE
    # ==========================================
    def allocate_page(self):

        page = self.page_entry.get()
        frame = self.frame_entry.get()

        if not page or not frame:

            messagebox.showwarning(
                "Missing Information",
                "Please enter Page Number and Frame Number."
            )

            return

        try:

            page = int(page)
            frame = int(frame)

            if page < 0 or frame < 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Page and Frame must be positive numbers."
            )

            return

        # Duplicate page
        for item in self.page_table:

            if item["page"] == page:

                messagebox.showerror(
                    "Duplicate Page",
                    "This page is already allocated."
                )

                return

        # Duplicate frame
        for item in self.page_table:

            if item["frame"] == frame:

                messagebox.showerror(
                    "Frame Already Used",
                    "This frame is already assigned."
                )

                return

        self.page_table.append({
            "page": page,
            "frame": frame
        })

        self.tree.insert(
            "",
            "end",
            values=(
                page,
                frame,
                "Allocated"
            )
        )

        self.page_entry.delete(
            0,
            tk.END
        )

        self.frame_entry.delete(
            0,
            tk.END
        )

        messagebox.showinfo(
            "Success",
            f"Page {page} allocated to Frame {frame}."
        )

    # ==========================================
    # CLEAR PAGING
    # ==========================================
    def clear_paging(self):

        self.page_table.clear()

        for item in self.tree.get_children():

            self.tree.delete(item)

    # ==========================================
    # RUN PAGE REPLACEMENT
    # ==========================================
    def run_replacement(self):

        reference_text = self.reference_entry.get()
        frames_text = self.frames_entry.get()

        if not reference_text or not frames_text:

            messagebox.showwarning(
                "Missing Information",
                "Please enter Reference String and Frames."
            )

            return

        try:

            reference = [
                int(x)
                for x in reference_text.replace(",", " ").split()
            ]

            frames = int(frames_text)

            if frames <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Enter valid numbers."
            )

            return

        if not reference:

            messagebox.showerror(
                "Invalid Reference",
                "Reference String cannot be empty."
            )

            return

        algorithm = self.algorithm.get()

        if algorithm == "FIFO":

            faults, hits, sequence = self.fifo(
                reference,
                frames
            )

        else:

            faults, hits, sequence = self.lru(
                reference,
                frames
            )

        self.result_label.config(
            text=(
                f"Page Faults: {faults}"
                f"    |    "
                f"Page Hits: {hits}"
            )
        )

        self.replacement_label.config(
            text="Frame Sequence: " + "  →  ".join(sequence)
        )

    # ==========================================
    # FIFO
    # ==========================================
    def fifo(self, reference, frame_count):

        queue = []

        faults = 0
        hits = 0

        sequence = []

        for page in reference:

            if page in queue:

                hits += 1

            else:

                faults += 1

                if len(queue) < frame_count:

                    queue.append(page)

                else:

                    queue.pop(0)
                    queue.append(page)

            sequence.append(
                "[" + ", ".join(
                    str(x) for x in queue
                ) + "]"
            )

        return faults, hits, sequence

    # ==========================================
    # LRU
    # ==========================================
    def lru(self, reference, frame_count):

        frames = []

        faults = 0
        hits = 0

        sequence = []

        for page in reference:

            if page in frames:

                hits += 1

                frames.remove(page)
                frames.append(page)

            else:

                faults += 1

                if len(frames) >= frame_count:

                    frames.pop(0)

                frames.append(page)

            sequence.append(
                "[" + ", ".join(
                    str(x) for x in frames
                ) + "]"
            )

        return faults, hits, sequence