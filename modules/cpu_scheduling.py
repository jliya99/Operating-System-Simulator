import tkinter as tk
from tkinter import ttk, messagebox


class CPUScheduling:

    def __init__(self, parent):
        self.parent = parent
        self.processes = []

        self.window = tk.Toplevel(parent)
        self.window.title("CPU Scheduling")
        self.window.geometry("1100x750")
        self.window.configure(bg="#0f172a")

        self.create_interface()

    def create_interface(self):

        # =========================
        # Title
        # =========================
        tk.Label(
            self.window,
            text="CPU SCHEDULING",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=20)

        # =========================
        # Algorithm Selection
        # =========================
        algorithm_frame = tk.Frame(
            self.window,
            bg="#0f172a"
        )
        algorithm_frame.pack()

        tk.Label(
            algorithm_frame,
            text="Select Algorithm:",
            font=("Arial", 12, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(side="left", padx=10)

        self.algorithm = ttk.Combobox(
            algorithm_frame,
            values=["FCFS", "SJF", "Round Robin"],
            state="readonly",
            width=18
        )

        self.algorithm.set("FCFS")
        self.algorithm.pack(side="left")

        # =========================
        # Time Quantum
        # =========================
        tk.Label(
            algorithm_frame,
            text="Time Quantum:",
            font=("Arial", 12, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(side="left", padx=(30, 5))

        self.quantum_entry = tk.Entry(
            algorithm_frame,
            width=8,
            font=("Arial", 11)
        )
        self.quantum_entry.pack(side="left")

        # =========================
        # Input Frame
        # =========================
        input_frame = tk.Frame(
            self.window,
            bg="#1e293b",
            padx=20,
            pady=20
        )

        input_frame.pack(
            padx=30,
            pady=20,
            fill="x"
        )

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

        # Arrival Time
        tk.Label(
            input_frame,
            text="Arrival Time",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=2, padx=10)

        self.arrival_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.arrival_entry.grid(row=0, column=3, padx=10)

        # Burst Time
        tk.Label(
            input_frame,
            text="Burst Time",
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.burst_entry = tk.Entry(
            input_frame,
            width=15,
            font=("Arial", 11)
        )
        self.burst_entry.grid(row=1, column=1, padx=10)

        # Add Process
        tk.Button(
            input_frame,
            text="Add Process",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            width=18,
            command=self.add_process
        ).grid(row=1, column=2, padx=10)

        # Clear
        tk.Button(
            input_frame,
            text="Clear All",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            width=18,
            command=self.clear_all
        ).grid(row=1, column=3, padx=10)

        # =========================
        # Process Table
        # =========================
        table_frame = tk.Frame(self.window)
        table_frame.pack(
            padx=30,
            fill="x"
        )

        columns = (
            "PID",
            "Arrival Time",
            "Burst Time",
            "Completion Time",
            "Waiting Time",
            "Turnaround Time"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=7
        )

        for column in columns:
            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=150,
                anchor="center"
            )

        self.tree.pack(fill="x")

        # =========================
        # Run Scheduler
        # =========================
        tk.Button(
            self.window,
            text="RUN SCHEDULER",
            font=("Arial", 13, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            height=2,
            command=self.run_scheduler
        ).pack(pady=20)

        # =========================
        # Gantt Chart
        # =========================
        tk.Label(
            self.window,
            text="GANTT CHART",
            font=("Arial", 16, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        self.gantt_frame = tk.Frame(
            self.window,
            bg="#0f172a"
        )

        self.gantt_frame.pack(pady=10)

        # =========================
        # Result
        # =========================
        self.result_label = tk.Label(
            self.window,
            text="Average Waiting Time: -    |    Average Turnaround Time: -",
            font=("Arial", 12, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        self.result_label.pack(pady=15)

    # ==================================================
    # ADD PROCESS
    # ==================================================
    def add_process(self):

        pid = self.pid_entry.get()
        arrival = self.arrival_entry.get()
        burst = self.burst_entry.get()

        if not pid or not arrival or not burst:
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        try:
            arrival = int(arrival)
            burst = int(burst)

            if arrival < 0 or burst <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Arrival Time must be 0 or greater and Burst Time must be greater than 0."
            )
            return

        for process in self.processes:

            if process["pid"] == pid:
                messagebox.showerror(
                    "Duplicate PID",
                    "This Process ID already exists."
                )
                return

        self.processes.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst
        })

        self.tree.insert(
            "",
            "end",
            values=(
                pid,
                arrival,
                burst,
                "-",
                "-",
                "-"
            )
        )

        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)

    # ==================================================
    # RUN SCHEDULER
    # ==================================================
    def run_scheduler(self):

        if not self.processes:

            messagebox.showwarning(
                "No Process",
                "Please add at least one process."
            )

            return

        algorithm = self.algorithm.get()

        if algorithm == "FCFS":

            results, gantt = self.fcfs()

        elif algorithm == "SJF":

            results, gantt = self.sjf()

        elif algorithm == "Round Robin":

            try:
                quantum = int(
                    self.quantum_entry.get()
                )

                if quantum <= 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Invalid Quantum",
                    "Please enter a positive Time Quantum."
                )

                return

            results, gantt = self.round_robin(
                quantum
            )

        self.show_results(
            results,
            gantt
        )

    # ==================================================
    # FCFS
    # ==================================================
    def fcfs(self):

        processes = sorted(
            self.processes,
            key=lambda x: x["arrival"]
        )

        current_time = 0
        results = []
        gantt = []

        for process in processes:

            if current_time < process["arrival"]:

                current_time = process["arrival"]

            start = current_time

            completion = (
                current_time +
                process["burst"]
            )

            turnaround = (
                completion -
                process["arrival"]
            )

            waiting = (
                turnaround -
                process["burst"]
            )

            gantt.append(
                (
                    process["pid"],
                    start,
                    completion
                )
            )

            results.append({
                "pid": process["pid"],
                "arrival": process["arrival"],
                "burst": process["burst"],
                "completion": completion,
                "waiting": waiting,
                "turnaround": turnaround
            })

            current_time = completion

        return results, gantt

    # ==================================================
    # SJF
    # ==================================================
    def sjf(self):

        processes = [
            process.copy()
            for process in self.processes
        ]

        completed = []
        gantt = []
        current_time = 0

        while processes:

            available = [
                p for p in processes
                if p["arrival"] <= current_time
            ]

            if not available:

                current_time = min(
                    p["arrival"]
                    for p in processes
                )

                continue

            selected = min(
                available,
                key=lambda p: (
                    p["burst"],
                    p["arrival"]
                )
            )

            processes.remove(selected)

            start = current_time

            completion = (
                current_time +
                selected["burst"]
            )

            turnaround = (
                completion -
                selected["arrival"]
            )

            waiting = (
                turnaround -
                selected["burst"]
            )

            gantt.append(
                (
                    selected["pid"],
                    start,
                    completion
                )
            )

            completed.append({
                "pid": selected["pid"],
                "arrival": selected["arrival"],
                "burst": selected["burst"],
                "completion": completion,
                "waiting": waiting,
                "turnaround": turnaround
            })

            current_time = completion

        return completed, gantt

    # ==================================================
    # ROUND ROBIN
    # ==================================================
    def round_robin(self, quantum):

        processes = sorted(
            [
                {
                    "pid": p["pid"],
                    "arrival": p["arrival"],
                    "burst": p["burst"],
                    "remaining": p["burst"]
                }
                for p in self.processes
            ],
            key=lambda x: x["arrival"]
        )

        queue = []
        completed = {}
        gantt = []

        current_time = 0
        index = 0

        while index < len(processes) or queue:

            # Add newly arrived processes
            while (
                index < len(processes)
                and processes[index]["arrival"]
                <= current_time
            ):

                queue.append(
                    processes[index]
                )

                index += 1

            # CPU idle
            if not queue:

                current_time = processes[index]["arrival"]

                continue

            process = queue.pop(0)

            pid = process["pid"]

            start = current_time

            execution_time = min(
                quantum,
                process["remaining"]
            )

            current_time += execution_time

            process["remaining"] -= execution_time

            gantt.append(
                (
                    pid,
                    start,
                    current_time
                )
            )

            # Add newly arrived processes
            while (
                index < len(processes)
                and processes[index]["arrival"]
                <= current_time
            ):

                queue.append(
                    processes[index]
                )

                index += 1

            # Process finished
            if process["remaining"] == 0:

                completion = current_time

                turnaround = (
                    completion -
                    process["arrival"]
                )

                waiting = (
                    turnaround -
                    process["burst"]
                )

                completed[pid] = {
                    "pid": pid,
                    "arrival": process["arrival"],
                    "burst": process["burst"],
                    "completion": completion,
                    "waiting": waiting,
                    "turnaround": turnaround
                }

            else:

                queue.append(process)

        results = []

        for process in processes:

            results.append(
                completed[process["pid"]]
            )

        return results, gantt

    # ==================================================
    # SHOW RESULTS
    # ==================================================
    def show_results(
        self,
        results,
        gantt
    ):

        for item in self.tree.get_children():

            self.tree.delete(item)

        total_waiting = 0
        total_turnaround = 0

        for result in results:

            self.tree.insert(
                "",
                "end",
                values=(
                    result["pid"],
                    result["arrival"],
                    result["burst"],
                    result["completion"],
                    result["waiting"],
                    result["turnaround"]
                )
            )

            total_waiting += result["waiting"]

            total_turnaround += (
                result["turnaround"]
            )

        average_waiting = (
            total_waiting /
            len(results)
        )

        average_turnaround = (
            total_turnaround /
            len(results)
        )

        self.create_gantt_chart(
            gantt
        )

        self.result_label.config(
            text=(
                f"Average Waiting Time: "
                f"{average_waiting:.2f}"
                f"    |    "
                f"Average Turnaround Time: "
                f"{average_turnaround:.2f}"
            )
        )

    # ==================================================
    # GANTT CHART
    # ==================================================
    def create_gantt_chart(
        self,
        gantt
    ):

        for widget in (
            self.gantt_frame.winfo_children()
        ):

            widget.destroy()

        for pid, start, end in gantt:

            box = tk.Frame(
                self.gantt_frame,
                bg="#2563eb",
                bd=1,
                relief="solid"
            )

            box.pack(
                side="left"
            )

            tk.Label(
                box,
                text=pid,
                font=("Arial", 11, "bold"),
                bg="#2563eb",
                fg="white",
                width=8,
                height=2
            ).pack()

            tk.Label(
                box,
                text=f"{start} - {end}",
                font=("Arial", 9),
                bg="#2563eb",
                fg="white"
            ).pack()

    # ==================================================
    # CLEAR ALL
    # ==================================================
    def clear_all(self):

        self.processes.clear()

        for item in self.tree.get_children():

            self.tree.delete(item)

        for widget in (
            self.gantt_frame.winfo_children()
        ):

            widget.destroy()

        self.result_label.config(
            text=(
                "Average Waiting Time: -"
                "    |    "
                "Average Turnaround Time: -"
            )
        )