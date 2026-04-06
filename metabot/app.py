import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if file_path:
        image_label.config(text=file_path)
        generate_btn.config(state="normal")

def generate_video():
    messagebox.showinfo("Success", "Video generated successfully! (demo)")
    os.startfile("sample.mp4")  # demo video open

app = tk.Tk()
app.title("AI Image to Video")
app.geometry("400x300")

title = tk.Label(app, text="Image to Video AI", font=("Arial", 16))
title.pack(pady=10)

upload_btn = tk.Button(app, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

image_label = tk.Label(app, text="No image selected")
image_label.pack()

generate_btn = tk.Button(app, text="Generate Video", command=generate_video)
generate_btn.pack(pady=20)

generate_btn.config(state="disabled")

app.mainloop()