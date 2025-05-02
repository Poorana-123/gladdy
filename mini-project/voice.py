import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from PIL import Image, ImageTk

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        root.update()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        status_label.config(text="You said: " + text)
    except sr.UnknownValueError:
        status_label.config(text="Could not understand audio.")
    except sr.RequestError:
        status_label.config(text="API error. Check your internet connection.")

# GUI setup
root = tk.Tk()
root.title("Voice to Text")
root.geometry("300x350")

# Load mic icon (ensure mic.png is in the same directory or use any PNG file path)
try:
    mic_image = Image.open("mic.png")
    mic_image = mic_image.resize((100, 100), Image.LANCZOS)
    mic_photo = ImageTk.PhotoImage(mic_image)
except FileNotFoundError:
    messagebox.showerror("Error", "mic.png not found. Please add a mic icon.")
    root.destroy()
    exit()

mic_button = tk.Button(root, image=mic_photo, command=recognize_speech)
mic_button.pack(pady=20)

status_label = tk.Label(root, text="Click the mic and speak...", wraplength=250)
status_label.pack(pady=20)

root.mainloop()
