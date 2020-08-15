from datetime import datetime
from pandas import DataFrame, read_csv

datetime.now().strftime("%d-%m-%Y %H:%M")


class Data():
    def __init__(self):
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year

    def first_create(self):
        df = DataFrame({
            'day': [],
            'month': [],
            'year': [],
            'mass': [],
            'top_pressure': [],
            'bottom_pressure': [],
            'pulse': []
        })
        df.to_csv('.\\data\\health_index.csv', index_label=False)

    def save_data(self, mass, top_pressure, bottom_pressure, pulse):
        df = read_csv('.\\data\\health_index.csv')
        input_df = DataFrame({
            'day': [self.day],
            'month': [self.month],
            'year': [self.year],
            'mass': [mass],
            'top_pressure': [top_pressure],
            'bottom_pressure': [bottom_pressure],
            'pulse': [pulse]
        })
        new_df = df.append(input_df, ignore_index=True)
        new_df.to_csv('.\\data\\health_index.csv', index_label=False)


#x = Data()
#x.first_create()
#x.save_data(12.5, 15, 15, 15)
