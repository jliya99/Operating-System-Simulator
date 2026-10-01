import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ProcessManagement:
    def __init__(self, parent):
        self.parent = parent
        self.processes = []

        self.window = tk.Toplevel(parent)
        self.window.title("Process Management")
        self.window.geometry("900x600")
        self.window.configure(bg="#0f172a")

        self.create_interface()

    def create_interface(self):

        # Title
        title = tk.Label(
            self.window,
            text="PROCESS MANAGEMENT",
            font=("Arial", 22, "bold"),
            bg="#0f172a",
            fg="white"
        )
        title.pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=20,
            pady=20
        )
        input_frame.pack(padx=30, fill="x")

        # Process ID
        tk.Label(
            input_frame,
            text="Process ID",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.pid_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.pid_entry.grid(row=0, column=1, padx=10)

        # Process Name
        tk.Label(
            input_frame,
            text="Process Name",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=2, padx=10)

        self.name_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.name_entry.grid(row=0, column=3, padx=10)

        # Arrival Time
        tk.Label(
            input_frame,
            text="Arrival Time",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.arrival_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.arrival_entry.grid(row=1, column=1, padx=10)

        # Burst Time
        tk.Label(
            input_frame,
            text="Burst Time",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=1, column=2, padx=10)

        self.burst_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.burst_entry.grid(row=1, column=3, padx=10)

        # Priority
        tk.Label(
            input_frame,
            text="Priority",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.priority_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.priority_entry.grid(row=2, column=1, padx=10)

        # Create Button
        create_button = tk.Button(
            input_frame,
            text="Create Process",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            width=18,
            command=self.create_process
        )
        create_button.grid(row=2, column=2, padx=10)

        # Queue Title
        queue_title = tk.Label(
            self.window,
            text="PROCESS QUEUE",
            font=("Arial", 16, "bold"),
            bg="#0f172a",
            fg="white"
        )
        queue_title.pack(pady=(25, 10))

        # Table
        table_frame = tk.Frame(self.window)
        table_frame.pack(padx=30, fill="both", expand=True)

        columns = (
            "PID",
            "Name",
            "Arrival",
            "Burst",
            "Priority",
            "Status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=120, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Terminate Button
        terminate_button = tk.Button(
            self.window,
            text="Terminate Selected Process",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            width=25,
            command=self.terminate_process
        )
        terminate_button.pack(pady=15)

    def create_process(self):

        pid = self.pid_entry.get()
        name = self.name_entry.get()
        arrival = self.arrival_entry.get()
        burst = self.burst_entry.get()
        priority = self.priority_entry.get()

        if not pid or not name or not arrival or not burst or not priority:
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        try:
            arrival = int(arrival)
            burst = int(burst)
            priority = int(priority)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Arrival Time, Burst Time and Priority must be numbers."
            )
            return

        for process in self.processes:
            if process["pid"] == pid:
                messagebox.showerror(
                    "Duplicate PID",
                    "This Process ID already exists."
                )
                return

        process = {
            "pid": pid,
            "name": name,
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "status": "Ready"
        }

        self.processes.append(process)

        self.tree.insert(
            "",
            "end",
            values=(
                pid,
                name,
                arrival,
                burst,
                priority,
                "Ready"
            )
        )

        self.clear_fields()

        messagebox.showinfo(
            "Success",
            f"Process {pid} created successfully."
        )

    def terminate_process(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a process first."
            )
            return

        for item in selected:
            values = self.tree.item(item, "values")
            pid = values[0]

            self.processes = [
                process
                for process in self.processes
                if process["pid"] != pid
            ]

            self.tree.delete(item)

        messagebox.showinfo(
            "Process Terminated",
            "Selected process has been terminated."
        )

    def clear_fields(self):

        self.pid_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)