
# Command Line Task Automator

This project is a simple Python-based command-line tool that automates various system tasks like listing processes, killing tasks, checking system resource usage (CPU, RAM), and cleaning system cache (for Linux). It is designed to help users manage their system tasks easily via simple command-line arguments.

## Features

- **List all running processes**: Displays a list of active processes with their PID (Process ID) and names.
- **Kill a process**: Terminate a process by specifying its PID.
- **Show system information**: Displays CPU and RAM usage.
- **Clean system cache** (Linux only): Clears the system cache (useful for freeing up memory on Linux systems).

## Tech Stack

- **Python 3.x**: The project is implemented in Python and uses standard Python libraries to interact with the system.
- **psutil**: A Python library used for retrieving system information such as CPU, memory usage, and process management.
- **platform**: A built-in Python module to check the operating system (Linux/Windows).
- **argparse**: Python library used for handling command-line arguments.

## Prerequisites

1. **Python 3.x**: Make sure Python 3.x is installed on your system.
2. **psutil**: Install the `psutil` library using `pip`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sujalgangarde/Basic-Command-Line-Task-Automator
   cd https://github.com/sujalgangarde/Basic-Command-Line-Task-Automator
   ```

2. Install the required dependencies:
   ```bash
   pip3 install psutil
   ```

   If you haven't installed Python 3 or `pip3` on your system, you can install them using your package manager:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

## Usage

You can run the **Command Line Task Automator** by providing various command-line arguments.

### Available Commands:

- **List processes**:
  ```bash
  python3 task_automator.py --list
  ```

- **Kill a process by PID**:
  ```bash
  python3 task_automator.py --kill <PID>
  ```

- **Show system info (CPU and RAM usage)**:
  ```bash
  python3 task_automator.py --info
  ```

- **Clean system cache** (Linux only):
  ```bash
  python3 task_automator.py --clean
  ```

## Example Usage

1. To list all running processes:
   ```bash
   python3 task_automator.py --list
   ```

2. To kill a process with a specific PID (e.g., 1234):
   ```bash
   python3 task_automator.py --kill 1234
   ```

3. To display CPU and RAM usage:
   ```bash
   python3 task_automator.py --info
   ```

4. To clean the system cache (Linux only):
   ```bash
   python3 task_automator.py --clean
   ```

## Running on WSL (Windows Subsystem for Linux)

1. Open your WSL terminal.
2. Ensure Python 3 and `pip3` are installed:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
3. Install required Python packages:
   ```bash
   pip3 install psutil
   ```
4. Run the Python script with desired arguments.

Example:
```bash
python3 task_automator.py --list
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributions

Feel free to fork the repository and submit pull requests. Contributions are welcome!
