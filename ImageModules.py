""""Imports"""

from customtkinter import filedialog

from PIL import ImageEnhance, Image

class Modify():
    
    def __init__(self):
        pass

    def BlackandWhiteImage(image: Image.Image):

        image = image.convert('L')

    def ReSizeImage(image: Image.Image, xy:tuple[int | float, int | float]):

        image = image.resize(xy)

    def BrightnessImage(image: Image.Image, brightness):

        enhancer = ImageEnhance.Brightness(image=image)
        image = enhancer.enhance(brightness)

    def RotateImage(image: Image.Image, angle):

        image = image.rotate(angle)

class File():
    def __init__(self):
        pass

    def saveas(image: Image.Image):

        filestypes = [("Joint Photographic Experts Group", "*.jpeg; *.jpg"),
                    ("Portable Network Graphic", "*.png"),
                    ]
        fp = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filestypes)

        image.save(fp=fp)

