import tkinter as tk

from modules.process_management import ProcessManagement
from modules.cpu_scheduling import CPUScheduling
from modules.memory_management import MemoryManagement
from modules.file_management import FileManagement
from modules.deadlock_management import DeadlockManagement


# ==========================================
# OPEN MODULES
# ==========================================

def open_process_management():
    ProcessManagement(root)


def open_cpu_scheduling():
    CPUScheduling(root)


def open_memory_management():
    MemoryManagement(root)


def open_file_management():
    FileManagement(root)


def open_deadlock_management():
    DeadlockManagement(root)


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Operating System Simulator")
root.geometry("1000x700")
root.configure(bg="#0f172a")


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="OPERATING SYSTEM SIMULATOR",
    font=("Arial", 26, "bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=(40, 10))


# ==========================================
# SUBTITLE
# ==========================================

subtitle = tk.Label(
    root,
    text="OS Management & Simulation System",
    font=("Arial", 12),
    bg="#0f172a",
    fg="#94a3b8"
)

subtitle.pack()


# ==========================================
# STATUS
# ==========================================

status = tk.Label(
    root,
    text="Select a module to begin",
    font=("Arial", 11),
    bg="#0f172a",
    fg="#64748b"
)

status.pack(pady=15)


# ==========================================
# BUTTON FRAME
# ==========================================

frame = tk.Frame(
    root,
    bg="#0f172a"
)

frame.pack(pady=25)


# ==========================================
# COMMON BUTTON SETTINGS
# ==========================================

button_width = 25
button_height = 2

button_font = (
    "Arial",
    13,
    "bold"
)


# ==========================================
# PROCESS MANAGEMENT
# ==========================================

process_button = tk.Button(
    frame,
    text="Process Management",
    font=button_font,
    width=button_width,
    height=button_height,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=open_process_management
)

process_button.grid(
    row=0,
    column=0,
    padx=20,
    pady=12
)


# ==========================================
# CPU SCHEDULING
# ==========================================

cpu_button = tk.Button(
    frame,
    text="CPU Scheduling",
    font=button_font,
    width=button_width,
    height=button_height,
    bg="#1e293b",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=open_cpu_scheduling
)

cpu_button.grid(
    row=0,
    column=1,
    padx=20,
    pady=12
)


# ==========================================
# MEMORY MANAGEMENT
# ==========================================

memory_button = tk.Button(
    frame,
    text="Memory Management",
    font=button_font,
    width=button_width,
    height=button_height,
    bg="#1e293b",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=open_memory_management
)

memory_button.grid(
    row=1,
    column=0,
    padx=20,
    pady=12
)


# ==========================================
# FILE MANAGEMENT
# ==========================================

file_button = tk.Button(
    frame,
    text="File Management",
    font=button_font,
    width=button_width,
    height=button_height,
    bg="#1e293b",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=open_file_management
)

file_button.grid(
    row=1,
    column=1,
    padx=20,
    pady=12
)


# ==========================================
# DEADLOCK MANAGEMENT
# ==========================================

deadlock_button = tk.Button(
    frame,
    text="Deadlock Management",
    font=button_font,
    width=button_width,
    height=button_height,
    bg="#1e293b",
    fg="white",
    activebackground="#334155",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=open_deadlock_management
)

deadlock_button.grid(
    row=2,
    column=0,
    columnspan=2,
    padx=20,
    pady=12
)


# ==========================================
# PROJECT INFORMATION
# ==========================================

info_frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=20,
    pady=12
)

info_frame.pack(
    padx=30,
    pady=10
)

info_text = tk.Label(
    info_frame,
    text="Process Management  •  CPU Scheduling  •  Memory Management\n"
         "File Management  •  Deadlock Management",
    font=("Arial", 10),
    bg="#1e293b",
    fg="#94a3b8",
    justify="center"
)

info_text.pack()


# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    root,
    text="Python + Tkinter | Operating Systems Project",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#64748b"
)

footer.pack(
    side="bottom",
    pady=15
)


# ==========================================
# RUN APPLICATION
# ==========================================

root.mainloop()