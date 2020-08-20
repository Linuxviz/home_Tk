import matplotlib
from numpy import array, arange
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import random
import matplotlib.pyplot as plt
from colors import *

class Plot:
    def __init__(self, window, x, y, title, x1, y1):
        self.window = window
        self.x = array(x)
        self.y = array(y)
        self.title = title
        self.x1 = x1
        self.y1 = y1
        self.plot()



    def plot(self):
        if self.x1 != 0 and self.y1 != 0:
            x = self.x
            y = self.y
            x1 = array(self.x1)
            y1 = array(self.y1)


            # Initialise the figure and axes.
            fig, ax = plt.subplots(1, figsize=(7, 2.5))

            #create grid
            ax.grid()

            # Set the title for the figure
            fig.suptitle('Давление', fontsize=15, font='Tahoma')

            # Draw all the lines in the same plot, assigning a label for each one to be
            # shown in the legend.
            ax.plot(range(len(y)), y, color="red", label="Верхнее давление")
            ax.plot(range(len(y1)), y1, color="green", label="Нижнее давление")

            # Add a legend, and position it on the lower right (with no box)
            plt.legend(loc="upper right", frameon=False)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            x = self.x
            y = self.y

            fig = Figure(figsize=(7, 2.5), facecolor=main_color_gray)
            a = fig.add_subplot(111)
            a.grid()
            a.plot(range(len(y)), y, color='red')

            a.set_title(self.title, font='Tahoma', fontsize=18, color=tertiary_color_very_light)
            a.set_ylabel("Кг", fontsize=14)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()

# window = Tk()
# start = PlotClass(window,1,2)
# window.mainloop()
