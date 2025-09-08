import os
from customtkinter import *
import json
from PIL import Image, ImageTk
# from hPyT import title_bar_color
import time
import sys
import ImageModules

with open(os.path.join(os.path.dirname(__file__), "settings.json"), "r") as f:
    read = f.read()
    settings = json.loads(read)

class TopBarApp(CTkFrame):
    ''' Top Bar of the App. '''
    def __init__(self, master):
        super().__init__(master)

        self.configure(height=40)

        self.menu = self.Menu(self)
        self.menu.pack(side=LEFT, padx=5, pady=5)

        self.menu = self.ActionsHandler(self)
        self.menu.pack(side=LEFT, padx=5, pady=5)

        self.menu = self.ImageImport(self)
        self.menu.pack(side=LEFT, padx=5, pady=5)

        self.menu = self.Zoom(self)
        self.menu.pack(side=LEFT, padx=5, pady=5)

        self.search_bar = self.SearchBar(self)
        self.search_bar.pack(padx=5, pady=5)

        self.pack(fill=X, padx=5, pady=(5, 0))

    class SearchBar(CTkFrame):
        def __init__(self, master):
            super().__init__(master)

            self.configure(corner_radius=0, fg_color="transparent")

            self.search_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "search.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "search.png")), (20, 20))

            self.search_button = CTkButton(self, image=self.search_image, text="", width=30, height=30, fg_color="transparent", command=self.search)
            self.search_input = self.SearchInput(self)

            self.search_input.grid(row=0, column=0)
            self.search_button.grid(row=0, column=1)

        def search(self):
            '''' Perform search action. '''
            query = self.search_input.search_entry.get()
            if query.startswith('/'):
                split_query = query.split(' ')
                match split_query[0]:
                    case '/state':
                        print(f"Previous state: {self.master.master.state()}")
                        if split_query[1] == 'normal':
                            self.master.master.state('normal')
                        elif split_query[1] == 'zoomed':
                            self.master.master.state('zoomed')
                        print(f"Current state: {self.master.master.state()}")
                    case '/color-theme':
                        if split_query[1] in ['blue', 'dark-blue', 'green']:
                            set_default_color_theme(split_query[1])
                            settings["color-theme"] = split_query[1]
                    case '/appearance':
                        if split_query[1] in ['System', 'Dark', 'Light']:
                            set_appearance_mode(split_query[1])
                            settings["appearance"] = split_query[1]
                    case '/restart':
                        self.master.master.restart()

        class SearchInput(CTkFrame):
            ''' Search input field with clear button. '''
            def __init__(self, master):
                super().__init__(master)

                self.configure(corner_radius=0, fg_color="transparent")

                self.clear_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "cross.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "cross.png")), (20, 20))

                self.search_entry = CTkEntry(self, placeholder_text="Search...", width=200, height=30, border_width=1, corner_radius=10, fg_color="transparent", border_color="#1D1D1D" if get_appearance_mode() == "Light" else "#DDDDDD", text_color="#000000" if get_appearance_mode() == "Light" else "#FFFFFF", font=("Arial", 14))
                self.search_entry.bind("<Return>", lambda event: self.master.search())
                self.search_entry.pack(side=LEFT, fill="x", expand=True, padx=5)
                
                self.clear_button = CTkButton(self, image=self.clear_image, text="", width=30, height=30, fg_color="transparent", command=lambda: self.search_entry.delete(0, 'end'))
                self.clear_button.pack(side=RIGHT)

    class Menu(CTkFrame):
        ''' App menu. '''
        def __init__(self, master):
            super().__init__(master)

            self.configure(corner_radius=0, fg_color="transparent")

            self.menu_frame = MenuFrame(self.master.master)

            self.menu_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "options.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "options.png")), (20, 20))
            self.menu_button = CTkButton(self, image=self.menu_image, text="", width=30, height=30, fg_color="transparent", command=self.menu_frame.open_menu)
            self.menu_button.pack()
            
    class ActionsHandler(CTkFrame):
        ''' Functions to redo. '''
        def __init__(self, master):
            super().__init__(master)

            self.configure(height=40, fg_color="transparent")

            self.redo_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "redo.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "redo.png")), (20, 20))
            self.undo_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "undo.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "undo.png")), (20, 20))

            self.redo_button = CTkButton(self, image=self.redo_image, text="", width=30, height=30, fg_color="transparent", command=self.redo)
            self.undo_button = CTkButton(self, image=self.undo_image, text="", width=30, height=30, fg_color="transparent", command=self.undo)
            
            self.undo_button.grid(row=0, column=0)
            self.redo_button.grid(row=0, column=1)

        def redo(self):
            ''' Redo the last action. '''
            pass

        def undo(self):
            ''' Undo the last action. '''
            pass

    class ImageImport(CTkFrame):
        def __init__(self, master):
            super().__init__(master)

            self.configure(height=40, fg_color="transparent")

            self.import_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "open-folder.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "open-folder.png")), (20, 20))
            self.save_as_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "save.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "save.png")), (20, 20))

            self.import_button = CTkButton(self, image=self.import_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.master.photo_frame.set())
            self.save_as_button = CTkButton(self, image=self.save_as_image, text="", width=30, height=30, fg_color="transparent", command=lambda: ImageModules.saveas(master.master.photo_frame.get_image()))
            
            self.import_button.grid(row=0, column=0)
            self.save_as_button.grid(row=0, column=1)
    
    class Zoom(CTkFrame):
        def __init__(self, master):
            super().__init__(master)

            self.configure(height=40, fg_color="transparent")

            self.zoom_out_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "zoom-in.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "zoom-in.png")), (20, 20))
            self.zoom_in_image = CTkImage(Image.open(os.path.join(os.path.dirname(__file__), "img_dark", "zoom-out.png")), Image.open(os.path.join(os.path.dirname(__file__), "img_light", "zoom-out.png")), (20, 20))

            self.zoom_out_button = CTkButton(self, image=self.zoom_out_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.master.photo_frame.increment_zoom(0.1))
            self.zoom_in_button = CTkButton(self, image=self.zoom_in_image, text="", width=30, height=30, fg_color="transparent", command=lambda: master.master.photo_frame.increment_zoom(-0.1))
            
            self.zoom_out_button.grid(row=0, column=0)
            self.zoom_in_button.grid(row=0, column=1)

class PhotoFrame(CTkLabel):
    ''' Frame to display video content. '''
    def __init__(self, master):
        super().__init__(master)

        self.configure(text="")
        self.pack(fill=BOTH, pady=5, padx=5)

        self.zoom = 0.5
        # self.image = Image.new(mode="RGB", size=(400, 400), color="white")
        # self.set(image=self.image)
    
    def set(self, asset_path=None):
        ''' Set the video to display. '''

        self.asset_path = asset_path or filedialog.askopenfilename()

        image = Image.open(self.asset_path)

        width = image.width * self.zoom
        height = image.height * self.zoom

        imageTk = CTkImage(image, size=(width, height))

        self.configure(image=imageTk)
        self.image = imageTk

    def get_image(self):
        return self.image._light_image or self.image._dark_image
    
    def update_zoom(self, image: Image.Image):

        width = image.width * self.zoom
        height = image.height * self.zoom

        imageTk = CTkImage(image, size=(width, height))

        self.configure(image=imageTk)
        self.image = imageTk

    def change_zoom(self, zoom: float):
        if zoom > 0:
            self.zoom = zoom
            self.update_zoom(self.get_image())

    def increment_zoom(self, zoom: float):
        if self.zoom + zoom > 0:
            self.zoom += zoom
            self.update_zoom(self.get_image())

    
class MenuFrame(CTkFrame):
    ''' Frame for the app menu options. '''
    def __init__(self, master):
        super().__init__(master)

        
    def open_menu(self):
        ''' Open the app menu. '''
        if self.winfo_ismapped():
            self.place_forget()
        else:
            self.place(
                x=5,
                y=50,
                relheight=1.0,
                anchor=NW
            )
            
            self.lift()

class App(CTk):
    ''' Main Application Class. '''
    def __init__(self):
        super().__init__()
        self.title("Videhome")
        self.geometry("800x600")

        set_appearance_mode(settings["appearance"])
        set_default_color_theme(settings["color-theme"])

        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        self.top_bar = TopBarApp(self)
        self.photo_frame = PhotoFrame(self)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<F11>", lambda event: self.toggle_fullscreen())
        
        self.after(100, self.load_settings)
        
    def load_settings(self):
        ''' Load settings from the settings.json file. '''
        if settings["geometry"]: self.geometry(settings["geometry"])
        if settings["fullscreen"]: 
            self.state("zoomed")
    
    def on_closing(self):
        ''' Save settings and close the app. '''
        if self.state() == 'zoomed':
            settings["fullscreen"] = True
            settings["geometry"] = None
        else:
            settings["fullscreen"] = False
            settings["geometry"] = self.geometry()

        settings["appearance"] = get_appearance_mode()
        with open(os.path.join(os.path.dirname(__file__), "settings.json"), "w") as f:
            f.write(json.dumps(settings, indent=4))
        self.destroy()

    def toggle_fullscreen(self):
        ''' Toggle fullscreen mode. '''
        if self.state() == 'normal':
            self.state('zoomed')
        elif self.state() == 'zoomed':
            self.state('normal')
    
    def restart(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        self.on_closing()
        time.sleep(0.5)
        python = sys.executable
        os.execl(python, python, * sys.argv)