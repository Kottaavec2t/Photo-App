import customtkinter as ctk
from ImageModules import Modify
from customtkinter import CTkFrame, CTkLabel, CTkImage, RIGHT, BOTH, BOTTOM, LEFT, X
from PIL import Image

class EditPopup(ctk.CTkToplevel):
    def __init__(self, master, image):
        super().__init__(master)
        self.title("Edit Image")
        self.geometry("600x600")
        self.resizable(False, False)
        self.transient(master)  # Keep the popup on top of the master window
        self.grab_set()  # Make the popup modal

        self.image = image

        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.configure(fg_color="transparent")
        self.buttons_frame.pack(side=LEFT, pady=5, padx=5)

        self.bw_frame = ctk.CTkFrame(self.buttons_frame)
        self.bw_frame.configure(border_width=1, border_color="gray", corner_radius=10, fg_color="transparent")
        self.bw_frame.pack(pady=10)
        self.bw_button = ctk.CTkButton(self.bw_frame, text="Black & White", command=self.BlackandWhite_image)
        self.bw_button.pack(pady=5, padx=5)

        self.resize_frame = ctk.CTkFrame(self.buttons_frame)
        self.resize_frame.configure(border_width=1, border_color="gray", corner_radius=10, fg_color="transparent")
        self.resize_frame.pack(pady=10)
        self.resize_x_input = ctk.CTkEntry(self.resize_frame, placeholder_text="Width")
        self.resize_x_input.pack(pady=5, padx=10)
        self.resize_y_input = ctk.CTkEntry(self.resize_frame, placeholder_text="Height")
        self.resize_y_input.pack(pady=5, padx=10)
        self.resize_button = ctk.CTkButton(self.resize_frame, text="Resize", command=self.Resize_image)
        self.resize_button.pack(pady=5, padx=10)

        self.brightness_frame = ctk.CTkFrame(self.buttons_frame)
        self.brightness_frame.configure(border_width=1, border_color="gray", corner_radius=10, fg_color="transparent")
        self.brightness_frame.pack(pady=10)
        self.brightness_input= ctk.CTkEntry(self.brightness_frame, placeholder_text="Intensity")
        self.brightness_input.pack(pady=5, padx=10)
        self.resize_button = ctk.CTkButton(self.brightness_frame, text="Change Brightness", command=self.Brightness_image)
        self.resize_button.pack(pady=5, padx=10)

        self.rotation_frame = ctk.CTkFrame(self.buttons_frame)
        self.rotation_frame.configure(border_width=1, border_color="gray", corner_radius=10, fg_color="transparent")
        self.rotation_frame.pack(pady=10, padx=10)
        self.rotation_input= ctk.CTkEntry(self.rotation_frame, placeholder_text="Angle")
        self.rotation_input.pack(pady=5, padx=10)
        self.resize_button = ctk.CTkButton(self.rotation_frame, text="Rotate", command=self.Rotate_image)
        self.resize_button.pack(pady=5, padx=10)

        self.photo_frame = PhotoFrame(self)
        self.photo_frame.pack(side=RIGHT, pady=5, padx=5)

        self.apply_button = ctk.CTkButton(self, text="Apply Changes", command=self.apply)
        self.apply_button.pack(side=BOTTOM, fill=X, pady=10, padx=10)

    def apply(self):
        self.master.photo_frame.update_display(self.image)
        self.destroy()

    def BlackandWhite_image(self):
        self.image = Modify.BlackandWhiteImage(self.image)
        self.photo_frame.update_display()

    def Resize_image(self):
        self.image = Modify.ReSizeImage(self.image, (int(self.resize_x_input.get()), int(self.resize_y_input.get())))
        self.photo_frame.update_display()

    def Brightness_image(self):
        self.image = Modify.BrightnessImage(self.image, float(self.brightness_input.get()))
        self.photo_frame.update_display()
    
    def Rotate_image(self):
        self.image = Modify.RotateImage(self.image, float(self.rotation_input.get()))
        self.photo_frame.update_display()

    def get_image(self):
        return self.image

class PhotoFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.image_pil: Image.Image = None
        self.image_ctk = None
        self.asset_path = None

        self.image_label = CTkLabel(self, text="Aucune image chargée")
        self.image_label.pack(fill=BOTH)

        self.update_display()
    
    def update_display(self):

        self.image_pil = self.master.get_image()

        if self.image_pil is None:
            self.image_label.configure(text="Aucune image chargée", image=None)
            return
        
        width = 300
        height = 300

        try:
            temp_image = self.image_pil.copy()
            self.image_ctk = CTkImage(temp_image, size=(width, height))
            self.image_label.configure(image=self.image_ctk, text="")

        except Exception as e:
            print(f"Erreur lors de la mise à jour de l'affichage: {e}")