# Operating System Simulator

## Project Description

Operating System Simulator is a Python-based desktop application
developed using Tkinter. The project demonstrates important
Operating System concepts through an interactive graphical interface.

## Technologies Used

- Python
- Tkinter
- Operating System Concepts
- File Handling

## Main Features

### 1. Process Management

- Create Process
- Terminate Process
- Process Queue
- Process ID
- Process Name
- Arrival Time
- Burst Time
- Priority
- Process Status

### 2. CPU Scheduling

The simulator supports:

- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin
- Gantt Chart
- Waiting Time
- Turnaround Time
- Completion Time
- Average Waiting Time
- Average Turnaround Time

### 3. Memory Management

The simulator demonstrates:

- Paging
- Page Allocation
- Page Table
- FIFO Page Replacement
- LRU Page Replacement
- Page Fault
- Page Hit

### 4. File Management

The File Management module supports:

- Create File
- Delete File
- Read File
- Write File
- Refresh File List

Files are stored inside the project's data folder.

### 5. Deadlock Management

The simulator implements:

- Banker's Algorithm
- Maximum Resource Matrix
- Allocation Matrix
- Available Resources
- Need Matrix
- Safe State Detection
- Safe Sequence

## Project Structure

```text
Operating System Simulator
│
├── main.py
│
├── data
│   └── Text files
│
├── modules
│   ├── process_management.py
│   ├── cpu_scheduling.py
│   ├── memory_management.py
│   ├── file_management.py
│   └── deadlock_management.py
│
└── README.md