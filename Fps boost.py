import os
import tkinter as tk
from tkinter import messagebox
import webbrowser  # <-- Added for opening Discord link

def run_minimum():
    messagebox.showinfo("Blightedd - Minimum Mode", "Running light cleanup...")
    os.system("powershell -Command \"Start-Sleep -Seconds 1\"")
    os.system("del /q /f /s %TEMP%\\*")

def run_medium():
    messagebox.showinfo("Blightedd - Medium Mode", "Killing light background tasks...")
    os.system("taskkill /f /im OneDrive.exe")
    os.system("taskkill /f /im YourPhone.exe")
    os.system("del /q /f /s %TEMP%\\*")

def run_max():
    messagebox.showinfo("Blightedd - MAX Mode", "Full FPS Boost Activated")
    
    os.system('REG ADD "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" /v PowerThrottlingOff /t REG_DWORD /d 1 /f')
    os.system('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
    os.system('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61')
    os.system('REG ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f')
    os.system('REG ADD "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')

    kill_list = [
        "OneDrive.exe", "YourPhone.exe", "Teams.exe", "SteamWebHelper.exe",
        "SearchIndexer.exe", "AdobeARM.exe", "Update.exe", "Cortana.exe"
    ]
    for proc in kill_list:
        os.system(f"taskkill /f /im {proc}")

    services = [
        "Spooler", "SysMain", "Xbox Live Auth Manager",
        "Xbox Live Game Save", "Xbox NetApiSvc"
    ]
    for svc in services:
        os.system(f"net stop \"{svc}\"")

    os.system("del /q /f /s %TEMP%\\*")

    messagebox.showinfo("Blightedd", "Max FPS Mode Applied!")

def join_discord():
    webbrowser.open("https://discord.gg/gcMBw2ezpe")

# GUI Setup
root = tk.Tk()
root.title("Blightedd FPS Booster")
root.geometry("350x300")  # Increased height slightly for Discord button
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Title and instructions
tk.Label(
    root,
    text="🕹️ Blightedd Boost",
    font=("Segoe UI", 16, "bold"),
    fg="white",
    bg="#1e1e1e"
).pack(pady=10)

tk.Label(
    root,
    text="Select a Boost Mode",
    font=("Segoe UI", 11),
    fg="#aaaaaa",
    bg="#1e1e1e"
).pack()

# Buttons
tk.Button(
    root,
    text="Minimum Boost",
    command=run_minimum,
    width=25,
    bg="#2d89ef",
    fg="white"
).pack(pady=10)

tk.Button(
    root,
    text="Medium Boost",
    command=run_medium,
    width=25,
    bg="#00b294",
    fg="white"
).pack(pady=5)

tk.Button(
    root,
    text="MAX Boost 🔥",
    command=run_max,
    width=25,
    bg="#e81123",
    fg="white"
).pack(pady=10)

# Join Discord button
tk.Button(
    root,
    text="Join Discord",
    command=join_discord,
    width=25,
    bg="#5865F2",  # Discord's blurple
    fg="white"
).pack(pady=5)

# Footer
tk.Label(
    root,
    text="by @Packmonke - Blightedd v1.0",
    font=("Segoe UI", 8),
    bg="#1e1e1e",
    fg="#444"
).pack(side="bottom", pady=10)

root.mainloop()
