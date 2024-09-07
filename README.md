# Cool Cleanup Utility

## Overview

The Cool Cleanup Utility is a Python-based application designed to help clean up temporary files and system junk from your Windows machine. It provides a graphical interface to execute various cleanup tasks and monitor their progress.

## Features

- **Remove Temporary Files**: Deletes files from the TEMP directory.
- **Empty Recycle Bin**: Clears all items from the Recycle Bin.
- **Remove System Files**: Cleans up system files using `cleanmgr`.
- **Remove Windows Update Cleanup**: Deletes old Windows Update files.
- **Remove Thumbnails**: Clears thumbnail cache files.
- **Remove Temporary Internet Files**: Removes files from Internet Cache.
- **Remove Delivery Optimization Files**: Deletes downloaded update files.
- **Remove Downloaded Program Files**: Clears downloaded program files.
- **Remove Offline Web Pages**: Deletes offline web pages.
- **Remove DirectX Shader Cache**: Clears DirectX shader cache files.
- **Remove Previous Windows Installations**: Cleans up previous Windows installation files.
- **Remove Temporary Files from Apps**: Deletes temporary files created by apps.
- **Remove System Restore Points**: Deletes all system restore points.
- **Remove C:\Windows\Temp Folder**: Clears the Windows Temp folder.

## Requirements

- Python 3.x
- Tkinter library (comes with Python standard library)
- Administrator privileges (for certain cleanup tasks)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ThiyansaRavidu/Win-Temp-Clear.git

2. **Navigate to the project directory:**

   ```bash
    cd Win-Temp-Clear

3. **Run the script using the command:**
  ```bash
    python Temp Clear.py

**Using the Interface:**

- The application window will appear with a "Start Cleanup" button.
- Click the "Start Cleanup" button to begin the cleanup process.
- The status area will display the progress of each cleanup task as it is executed.

**Monitoring Progress:**

- The status area will show the description of each task as it starts.
- Once a task is completed, a checkmark (✔) will indicate success, or a cross (✘) will indicate failure.
- Continue to monitor the status area for updates until all tasks are completed.
