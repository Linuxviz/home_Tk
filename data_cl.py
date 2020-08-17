from datetime import datetime
from pandas import DataFrame, read_csv

datetime.now().strftime("%d-%m-%Y %H:%M")


class Data:
    def __init__(self):
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year
        self.df = read_csv('.\\data\\health_index.csv')

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
        self.df = read_csv('.\\data\\health_index.csv')

    def data_backup(self):
        df = read_csv('.\\data\\health_index.csv')
        df.to_csv('.\\data\\health_index' + '_{}.{}.{}_backup'.format(self.day, self.month, self.year) + '.csv',
                  index_label=False)

    def get_mass(self):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['mass']
        return x, tuple(y)

    def get_top_pressure(self):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['top_pressure']
        return x, tuple(y)

    def get_bottom_pressure(self):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['bottom_pressure']
        return x, tuple(y)

    def get_pulse(self):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['pulse']
        return x, tuple(y)

    def __concatenate_data(self, day, month, year):
        str_list = list()
        for i in range(len(day)):
            str_list.append('{}.{}.{}'.format(day[i], month[i], year[i]))
        return tuple(str_list)

# x = Data()
# x.data_backup()
# x.first_create()
# x.save_data(12.5, 15, 15, 15)
# print(x.get_mass())
