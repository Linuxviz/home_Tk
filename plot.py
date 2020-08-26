from numpy import array
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from colors import *


class Plot:
    def __init__(self, window, x, y, title, unit, x1, y1):
        self.window = window
        self.x = array(x)
        self.y = array(y)
        self.title = title
        self.x1 = x1
        self.y1 = y1
        self.unit = unit

        self.plot()

    def plot(self):
        if self.x1 != 0 and self.y1 != 0:
            x = self.x
            y = self.y
            x1 = array(self.x1)
            y1 = array(self.y1)

            fig = Figure(figsize=(7, 2.5), facecolor=main_color_gray)
            a = fig.add_subplot(111)
            a.grid()
            a.plot(range(len(y)),
                   y,
                   color=secondary_color_black,
                   linestyle='-',
                   linewidth=2,
                   label="Верхнее давление")
            a.plot(range(len(y1)),
                   y1,
                   color=secondary_color_black,
                   linestyle='--',
                   linewidth=2,
                   label="Нижнее давление")
            a.set_title(self.title, font='Tahoma', fontsize=18, color=tertiary_color_very_light)
            a.set_ylabel(self.unit, font='Tahoma', fontsize=14, color=tertiary_color_very_light)
            a.legend(loc="upper right", fontsize=10)
            for side in ['bottom', 'top', 'left', 'right']:
                a.spines[side].set_color(tertiary_color_very_light)
            a.tick_params(axis='both', colors=tertiary_color_very_light)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            x = self.x
            y = self.y

            fig = Figure(figsize=(7, 2.5), facecolor=main_color_gray)

            a = fig.add_subplot(111)
            a.grid()
            a.plot(range(len(y)), y, color=secondary_color_black, label="Верхнее давление")
            a.set_title(self.title, font='Tahoma', fontsize=18, color=tertiary_color_very_light)
            a.set_ylabel(self.unit, font='Tahoma', fontsize=14, color=tertiary_color_very_light)
            a.legend(loc="upper right", fontsize=10)
            for side in ['bottom', 'top', 'left', 'right']:
                a.spines[side].set_color(tertiary_color_very_light)
            a.tick_params(axis='both', colors=tertiary_color_very_light)

            canvas = FigureCanvasTkAgg(fig, master=self.window)
            canvas.get_tk_widget().pack()
            canvas.draw()
