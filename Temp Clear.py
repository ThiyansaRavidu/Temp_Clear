import tkinter as tk
from tkinter import scrolledtext
import subprocess

def run_cleanup():
    # Clear the status area
    status_area.delete(1.0, tk.END)
    status_area.insert(tk.END, "Starting cleanup...\n")
    status_area.update_idletasks()  # Force GUI to update

    # List of tasks to run
    tasks = [
        ("01. Remove Temporary Files", 'del /s /q %TEMP%\\*.*'),
        ("02. Remove Temporary Folders", 'for /d %p in ("%TEMP%\\*.*") do rmdir "%p" /s /q'),
        ("03. Empty Recycle Bin", 'rd /s /q %systemdrive%\\$Recycle.Bin'),
        ("04. Remove System Files", 'cleanmgr /sagerun:1'),
        ("05. Remove Windows Update Cleanup", 'cleanmgr /sagerun:50'),
        ("06. Remove Thumbnails", 'del /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\Explorer\\thumbcache_*.db'),
        ("07. Remove Temporary Internet Files", 'del /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\*.*'),
        ("08. Remove Delivery Optimization Files", 'del /s /q %systemdrive%\\Windows\\SoftwareDistribution\\Download\\*.*'),
        ("09. Remove Downloaded Program Files", 'del /s /q %userprofile%\\Downloads\\*.*'),
        ("10. Remove Offline Web Pages", 'rd /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE'),
        ("11. Remove DirectX Shader Cache", 'del /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\DXCache\\*.*'),
        ("12. Remove Previous Windows Installations", 'dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase'),
        ("13. Remove Temporary Files from Apps", 'rd /s /q %userprofile%\\AppData\\Local\\Temp'),
        ("14. Remove System Restore Points", 'vssadmin.exe Delete Shadows /All /Quiet'),
        ("15. Remove C:\\Windows\\Temp folder", 'rd /s /q C:\\Windows\\Temp')
    ]

    # Execute each task and update status
    for description, command in tasks:
        status_area.insert(tk.END, f"{description}...\n")
        status_area.update_idletasks()  # Update the GUI
        try:
            result = subprocess.run(f'cmd /c {command}', shell=True, check=True, text=True, capture_output=True)
            status_area.insert(tk.END, f"✔ {description} completed.\n")
        except subprocess.CalledProcessError as ex:
            status_area.insert(tk.END, f"✘ {description} failed. Error: {ex}\n")
        status_area.update_idletasks()  # Update the GUI
    
    status_area.insert(tk.END, "All tasks completed.\n")

# Create the main window
root = tk.Tk()
root.title("Cool Cleanup Utility")
root.geometry("600x400")

# Create a title label
title_label = tk.Label(root, text="Cool System Cleanup Utility", font=("Arial", 16))
title_label.pack(pady=10)

# Create the status text area
status_area = scrolledtext.ScrolledText(root, width=80, height=20)
status_area.pack(pady=10)

# Create the start cleanup button
start_button = tk.Button(root, text="Start Cleanup", command=run_cleanup, bg="green", fg="white", font=("Arial", 12))
start_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
