import matplotlib
from numpy import array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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
            x1 = array(self.x)
            y1 = array(self.y)

            fig = Figure(figsize=(5.5, 4))
            #a = fig.add_subplot(111)
            a = fig.add_subplot()
            a.plot(range(len(y)), y, color='red')
            a.plot(range(len(y1)), y1, color='blue')

            a.set_title(self.title, fontsize=16)
            a.set_ylabel("sd", fontsize=14)
            a.set_xlabel("Дата", fontsize=14)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            x = self.x
            y = self.y

            fig = Figure(figsize=(5.5, 4))
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
