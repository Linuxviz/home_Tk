import matplotlib
from numpy import array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Tk


class PlotClass:
    def __init__(self, window, x, y):
        self.window = window
        self.plot()
        self.x = x
        self.y = y

    def plot(self):
        x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        p = array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
                      19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

        fig = Figure(figsize=(6, 2))
        a = fig.add_subplot(111)
        a.plot(range(len(p)), p, color='red')

        a.set_title("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()


# window = Tk()
# start = PlotClass(window,1,2)
# window.mainloop()
