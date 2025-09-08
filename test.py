import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Example(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        tk.Button(self,bg='red',text="one").grid(row=0,column=0,sticky='we', padx=5, pady=10)
        tk.Button(self,bg='blue',text="two").grid(row=1,column=0,ipadx=200,sticky='we', padx=5, pady=5)
        tk.Label(self,bg='green',text="label").grid(row=2,column=0,sticky='we',padx=5, pady=5)

        first_frame= tk.Frame(self, pady=5, padx=5)
        first_frame.grid(row=3,column=0)

        canvas=tk.Canvas(first_frame,bg="orange",height=300,width=480)
        canvas.pack(side="left", fill="both", expand=True) ### side="left" instead of "bottom"

        scrollbar = ttk.Scrollbar(first_frame, orient="vertical", command=canvas.yview) # child of first_frame instead of canvas
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        #scrollbar.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        second_frame=tk.Canvas(canvas)
        # bind on second_frame instead of scrollbar
        second_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=second_frame, anchor="nw") ### anchor="nw" instead of "ne"

        # Random data
        np.random.seed(3)
        x = 0.5 + np.arange(8)
        y = np.random.uniform(2, 7, len(x))

        # Plot 2 stacked figures
        fig, ax1= plt.subplots(2,figsize=(5,50))

        ax1[0].step(x, y, linewidth=2.5)
        ax1[0].set(xlim=(0, 8), xticks=np.arange(1, 8),
                ylim=(0, 8), yticks=np.arange(1, 8))

        ax1[1].step(x, y, linewidth=2.5)
        ax1[1].set(xlim=(0, 8), xticks=np.arange(1, 8),
                ylim=(0, 8), yticks=np.arange(1, 8))

        # Draw into canvas
        canvas_fig = FigureCanvasTkAgg(fig, second_frame) # used second_frame instead of canvas
        canvas_fig.get_tk_widget().pack(side="bottom", fill="y")
        #scrollbar.config(command=canvas_fig.get_tk_widget().yview)


app=Example()
#app.geometry("480x320")
app.title("Scrollfigure")

app.mainloop()