""""Imports"""

from customtkinter import filedialog

from PIL import ImageEnhance, Image

class Modify():
    
    def __init__(self):
        pass

    def BlackandWhiteImage(image: Image.Image):

        image = image.convert('L')
        return image

    def ReSizeImage(image: Image.Image, xy:tuple[int | float, int | float]):

        image = image.resize(xy)
        return image

    def BrightnessImage(image: Image.Image, brightness):

        enhancer = ImageEnhance.Brightness(image=image)
        image = enhancer.enhance(brightness)
        return image

    def RotateImage(image: Image.Image, angle):

        image = image.rotate(angle)
        return image

class File():
    def __init__(self):
        pass

    def saveas(image: Image.Image):

        filestypes = [("Joint Photographic Experts Group", "*.jpeg; *.jpg"),
                    ("Portable Network Graphic", "*.png"),
                    ]
        fp = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filestypes)

        image.save(fp=fp)
