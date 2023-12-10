import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageWatermarkApp:
    def __init__(self, root):
        self.watermark_label = None
        self.browse_watermark_button = None
        self.add_watermark_button = None
        self.browse_image_button = None
        self.watermark_display = None
        self.image_display = None
        self.image_label = None
        self.buttons_frame = None
        self.watermark_frame = None
        self.image_frame = None
        self.root = root
        self.root.title("Image Watermark App")

        self.image_path = None
        self.watermark_path = None

        self.create_widgets()

    def create_widgets(self):
        # Image Frame
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        # Watermark Frame
        self.watermark_frame = tk.Frame(self.root)
        self.watermark_frame.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Image Label
        self.image_label = tk.Label(self.image_frame, text="Select Image:")
        self.image_label.grid(row=0, column=0)

        # Watermark Label
        self.watermark_label = tk.Label(self.watermark_frame, text="Select Watermark:")
        self.watermark_label.grid(row=0, column=0)

        # Image Display
        self.image_display = tk.Label(self.image_frame)
        self.image_display.grid(row=1, column=0)

        # Watermark Display
        self.watermark_display = tk.Label(self.watermark_frame)
        self.watermark_display.grid(row=1, column=0)

        # Browse Image Button
        self.browse_image_button = tk.Button(self.buttons_frame, text="Browse Image", command=self.browse_image)
        self.browse_image_button.grid(row=0, column=0)

        # Browse Watermark Button
        self.browse_watermark_button = tk.Button(self.buttons_frame, text="Browse Watermark",
                                                 command=self.browse_watermark)
        self.browse_watermark_button.grid(row=0, column=1)

        # Add Watermark Button
        self.add_watermark_button = tk.Button(self.buttons_frame, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.grid(row=0, column=2)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.show_image(file_path)

    def browse_watermark(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.watermark_path = file_path
            self.show_watermark(file_path)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((300, 300))
        tk_image = ImageTk.PhotoImage(image)
        self.image_display.config(image=tk_image)
        self.image_display.image = tk_image

    def show_watermark(self, watermark_path):
        watermark = Image.open(watermark_path)
        watermark.thumbnail((100, 100))
        tk_watermark = ImageTk.PhotoImage(watermark)
        self.watermark_display.config(image=tk_watermark)
        self.watermark_display.image = tk_watermark

    def add_watermark(self):
        if self.image_path and self.watermark_path:
            original_image = Image.open(self.image_path)
            watermark = Image.open(self.watermark_path)

            # Add the watermark to the image
            watermark_position = (
                original_image.width - watermark.width - 10,
                original_image.height - watermark.height - 10
            )
            original_image.paste(watermark, watermark_position, watermark)

            # Save the new image with the watermark
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if save_path:
                original_image.save(save_path)
                tk.messagebox.showinfo("Success", "Watermark added successfully!")
