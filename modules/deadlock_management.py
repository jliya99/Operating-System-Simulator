import tkinter as tk
from tkinter import messagebox


class DeadlockManagement:

    def __init__(self, parent):

        self.parent = parent

        self.window = tk.Toplevel(parent)
        self.window.title("Deadlock Management - Banker's Algorithm")
        self.window.geometry("950x700")
        self.window.configure(bg="#0f172a")

        self.create_interface()

    # ==========================================
    # INTERFACE
    # ==========================================

    def create_interface(self):

        tk.Label(
            self.window,
            text="DEADLOCK MANAGEMENT",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=20)

        tk.Label(
            self.window,
            text="Banker's Algorithm",
            font=("Arial", 16, "bold"),
            bg="#0f172a",
            fg="#60a5fa"
        ).pack(pady=5)

        # ==========================================
        # INPUT FRAME
        # ==========================================

        input_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=20,
            pady=20
        )

        input_frame.pack(
            padx=30,
            pady=15,
            fill="x"
        )

        # Processes

        tk.Label(
            input_frame,
            text="Processes",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.process_entry = tk.Entry(
            input_frame,
            width=10,
            font=("Arial", 11)
        )

        self.process_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        self.process_entry.insert(
            0,
            "5"
        )

        # Resources

        tk.Label(
            input_frame,
            text="Resources",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.resource_entry = tk.Entry(
            input_frame,
            width=10,
            font=("Arial", 11)
        )

        self.resource_entry.grid(
            row=0,
            column=3,
            padx=10
        )

        self.resource_entry.insert(
            0,
            "3"
        )

        # Generate button

        tk.Button(
            input_frame,
            text="Generate Matrix",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            width=18,
            command=self.generate_matrix
        ).grid(
            row=0,
            column=4,
            padx=15
        )

        # ==========================================
        # MATRIX AREA
        # ==========================================

        matrix_frame = tk.Frame(
            self.window,
            bg="#0f172a"
        )

        matrix_frame.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=True
        )

        # Maximum Matrix

        tk.Label(
            matrix_frame,
            text="MAXIMUM",
            font=("Arial", 14, "bold"),
            bg="#0f172a",
            fg="white"
        ).grid(
            row=0,
            column=0,
            pady=8
        )

        self.max_text = tk.Text(
            matrix_frame,
            height=10,
            width=35,
            font=("Consolas", 11)
        )

        self.max_text.grid(
            row=1,
            column=0,
            padx=10
        )

        # Allocation Matrix

        tk.Label(
            matrix_frame,
            text="ALLOCATION",
            font=("Arial", 14, "bold"),
            bg="#0f172a",
            fg="white"
        ).grid(
            row=0,
            column=1,
            pady=8
        )

        self.allocation_text = tk.Text(
            matrix_frame,
            height=10,
            width=35,
            font=("Consolas", 11)
        )

        self.allocation_text.grid(
            row=1,
            column=1,
            padx=10
        )

        # Available

        tk.Label(
            matrix_frame,
            text="AVAILABLE",
            font=("Arial", 14, "bold"),
            bg="#0f172a",
            fg="white"
        ).grid(
            row=0,
            column=2,
            pady=8
        )

        self.available_entry = tk.Entry(
            matrix_frame,
            width=25,
            font=("Arial", 11)
        )

        self.available_entry.grid(
            row=1,
            column=2,
            padx=10,
            pady=20
        )

        # ==========================================
        # BUTTONS
        # ==========================================

        button_frame = tk.Frame(
            self.window,
            bg="#0f172a"
        )

        button_frame.pack(
            pady=15
        )

        tk.Button(
            button_frame,
            text="Check Safe State",
            font=("Arial", 12, "bold"),
            bg="#16a34a",
            fg="white",
            width=20,
            command=self.check_safe_state
        ).pack(
            side="left",
            padx=10
        )

        tk.Button(
            button_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="#dc2626",
            fg="white",
            width=15,
            command=self.clear_all
        ).pack(
            side="left",
            padx=10
        )

        # ==========================================
        # RESULT
        # ==========================================

        tk.Label(
            self.window,
            text="RESULT",
            font=("Arial", 15, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=5)

        self.result_label = tk.Label(
            self.window,
            text="Enter matrices and check the safe state.",
            font=("Arial", 12, "bold"),
            bg="#0f172a",
            fg="white"
        )

        self.result_label.pack(
            pady=10
        )

    # ==========================================
    # GENERATE MATRIX
    # ==========================================

    def generate_matrix(self):

        try:

            processes = int(
                self.process_entry.get()
            )

            resources = int(
                self.resource_entry.get()
            )

            if processes <= 0 or resources <= 0:

                raise ValueError

            self.max_text.delete(
                "1.0",
                tk.END
            )

            self.allocation_text.delete(
                "1.0",
                tk.END
            )

            # Create empty matrices

            for i in range(processes):

                self.max_text.insert(
                    tk.END,
                    " ".join(
                        ["0"] * resources
                    ) + "\n"
                )

                self.allocation_text.insert(
                    tk.END,
                    " ".join(
                        ["0"] * resources
                    ) + "\n"
                )

            self.available_entry.delete(
                0,
                tk.END
            )

            self.available_entry.insert(
                0,
                " ".join(
                    ["0"] * resources
                )
            )

            messagebox.showinfo(
                "Matrix Generated",
                "Enter Maximum, Allocation and Available values."
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )

    # ==========================================
    # READ MATRIX
    # ==========================================

    def read_matrix(self, text_widget, processes, resources):

        lines = text_widget.get(
            "1.0",
            "end-1c"
        ).strip().splitlines()

        if len(lines) != processes:

            raise ValueError(
                "Number of rows is incorrect."
            )

        matrix = []

        for line in lines:

            values = list(
                map(
                    int,
                    line.split()
                )
            )

            if len(values) != resources:

                raise ValueError(
                    "Number of resources is incorrect."
                )

            matrix.append(values)

        return matrix

    # ==========================================
    # BANKER'S ALGORITHM
    # ==========================================

    def check_safe_state(self):

        try:

            processes = int(
                self.process_entry.get()
            )

            resources = int(
                self.resource_entry.get()
            )

            maximum = self.read_matrix(
                self.max_text,
                processes,
                resources
            )

            allocation = self.read_matrix(
                self.allocation_text,
                processes,
                resources
            )

            available = list(
                map(
                    int,
                    self.available_entry.get().split()
                )
            )

            if len(available) != resources:

                raise ValueError(
                    "Available resource count is incorrect."
                )

            # ==================================
            # CALCULATE NEED MATRIX
            # Need = Maximum - Allocation
            # ==================================

            need = []

            for i in range(processes):

                row = []

                for j in range(resources):

                    value = (
                        maximum[i][j]
                        -
                        allocation[i][j]
                    )

                    if value < 0:

                        raise ValueError(
                            "Allocation cannot be greater than Maximum."
                        )

                    row.append(value)

                need.append(row)

            # ==================================
            # BANKER'S ALGORITHM
            # ==================================

            work = available.copy()

            finish = [False] * processes

            safe_sequence = []

            while len(safe_sequence) < processes:

                found = False

                for i in range(processes):

                    if not finish[i]:

                        possible = True

                        for j in range(resources):

                            if need[i][j] > work[j]:

                                possible = False
                                break

                        if possible:

                            # Release allocated resources

                            for j in range(resources):

                                work[j] += allocation[i][j]

                            finish[i] = True

                            safe_sequence.append(i)

                            found = True

                if not found:
                    break

            # ==================================
            # RESULT
            # ==================================

            if len(safe_sequence) == processes:

                sequence_text = " → ".join(
                    f"P{i}"
                    for i in safe_sequence
                )

                self.result_label.config(
                    text=f"SAFE STATE\nSafe Sequence: {sequence_text}",
                    fg="#22c55e"
                )

                messagebox.showinfo(
                    "Safe State",
                    f"System is in a SAFE STATE.\n\n"
                    f"Safe Sequence:\n{sequence_text}"
                )

            else:

                self.result_label.config(
                    text="UNSAFE STATE - Deadlock may occur!",
                    fg="#ef4444"
                )

                messagebox.showwarning(
                    "Unsafe State",
                    "System is in an UNSAFE STATE.\n\n"
                    "No safe sequence was found."
                )

        except ValueError as e:

            messagebox.showerror(
                "Invalid Input",
                str(e)
            )

    # ==========================================
    # CLEAR
    # ==========================================

    def clear_all(self):

        self.max_text.delete(
            "1.0",
            tk.END
        )

        self.allocation_text.delete(
            "1.0",
            tk.END
        )

        self.available_entry.delete(
            0,
            tk.END
        )

        self.result_label.config(
            text="Enter matrices and check the safe state.",
            fg="white"
        )