
# Python Keylogger

A simple keylogger implemented in Python that logs keystrokes on your system. This is for educational purposes only and should be used ethically and responsibly.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Ethical Considerations](#ethical-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Logs all keystrokes: Captures letters, numbers, symbols, and special characters.
- Timestamps: Every keystroke is logged with a timestamp.
- Special key logging: Captures keys like **Space**, **Enter**, **Shift**, **Backspace**, and others.
- Background operation: Runs in the background without disrupting your activities.
- Text file output: Logs are saved in a file named `keylog.txt`.

## Installation

Follow these steps to set up and run the keylogger on your machine.

### Step 1: Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/python-keylogger.git
cd python-keylogger
```

### Step 2: Install dependencies

Ensure that Python 3.x is installed. Then install the required Python packages using pip:

```bash
pip install pynput
```

### Step 3: Run the keylogger

Once the dependencies are installed, you can run the keylogger by executing the following command:

```bash
python keylogger.py
```

The keylogger will start running in the background and begin logging all keystrokes. The keystrokes will be saved to a file named `keylog.txt` in the same directory.

### Step 4: Stopping the keylogger

To stop the keylogger, press the **Escape (Esc)** key. This will safely exit the program.

## Usage

Once the keylogger is running, all keystrokes will be logged to `keylog.txt`.

Example Log Output:

```txt
2024-12-22 00:17:37,036 : o
2024-12-22 00:17:37,204 : u
2024-12-22 00:17:38,152 : ?
2024-12-22 00:17:39,271 : /n
2024-12-22 00:17:47,466 : /t
2024-12-22 00:17:48,235 : Key.backspace
2024-12-22 00:17:54,783 : Key.ctrl_r
2024-12-22 00:17:55,082 : Key.ctrl_l
```

## Ethical Considerations

**Important**: This keylogger is for educational purposes only. Unauthorized use of keyloggers is illegal and violates privacy rights.

- Always obtain consent before running a keylogger on any system that you don't own.
- This project should only be used in environments where you have explicit permission (e.g., on your own system or a test system).


## Acknowledgments

- [pynput](https://pypi.org/project/pynput/): This library is used to capture keyboard events.
- Inspired by educational cybersecurity tools and ethical hacking demonstrations.
