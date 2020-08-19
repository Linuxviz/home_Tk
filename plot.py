import matplotlib
from numpy import array, arange
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import random
import matplotlib.pyplot as plt

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
            fig, ax = plt.subplots(1, figsize=(8, 6))

            #create grid
            ax.grid()

            # Set the title for the figure
            fig.suptitle('Multiple Lines in Same Plot', fontsize=15)

            # Draw all the lines in the same plot, assigning a label for each one to be
            # shown in the legend.
            ax.plot(range(len(y)), y, color="red", label="My Line 1")
            ax.plot(range(len(y1)), y1, color="green", label="My Line 2")

            # Add a legend, and position it on the lower right (with no box)
            plt.legend(loc="lower right", title="Legend Title", frameon=False)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            x = self.x
            y = self.y

            fig = Figure(figsize=(2, 2))
            a = fig.add_subplot(111)
            a.plot(range(len(y)), y, color='red')

            a.set_title(self.title, fontsize=16)
            a.set_ylabel("sd", fontsize=14)
            a.set_xlabel("Дата", fontsize=14)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()

# window = Tk()
# start = PlotClass(window,1,2)
# window.mainloop()
