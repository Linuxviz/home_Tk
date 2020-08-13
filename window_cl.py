from tkinter import Tk, Label, Button, Entry, PhotoImage, StringVar


class Window:
    """ Материнский класс виджетов приложений """

    def __init__(self):
        self.win_width = 400
        self.win_height = 800
        self.title = ''
        self.root = Tk()
        print('created')

    def _special_initialization(self):
        """В этом методе в дочерних классах описывается спецефичное для них поведение во инициализации их параметров"""
        print('Я вызван')
        return 0

    def create(self):
        """Публичный метод проводящий инициализацию виджетов tk внутри открытого окна"""
        self.root.geometry(str(self.win_width) + 'x' + str(self.win_height))
        self.root.title(self.title)
        print('-')
        self._special_initialization()
        print('+')
        self.root.mainloop()
        print('mainloop')

    def stop(self):
        self.root.destroy()


class AuthorizationWindow(Window):
    """Класс окна отвечающего за авторизацию пользователя"""

    def __init__(self):
        super().__init__()
        self.title = 'Авторизация'
        self.true_password = '1239'
        self.input_password = StringVar()
        self.flag = False
        self.authorization_complete = False

    def is_authorization_complete(self):
        """Метод возвращает состояние поля с успешной атворизацией"""
        return self.authorization_complete

    def __is_user(self, password: str) -> bool:
        """ Проверка пароля """
        if password == self.true_password:
            return True
        else:
            return False

    def __authorization(self):
        """Метод вызываемый при нажатии кнопки, вызывает сравнение пароля введенного пользователем и
        тем что лежит в классе"""
        password = self.input_password.get()
        print(password)
        if self.__is_user(password):
            self.authorization_complete = True
            print('Успех')
            self.root.quit()
        else:
            if self.flag:
                self.error_text.configure(text='Досихпор неверно')
                self.error_text.pack()
            else:
                self.flag = True
                self.error_text.pack()

    def _special_initialization(self):
        print('Я вызван и это хорошо')
        # bg = PhotoImage(file="imgbg.png")
        authorization_text = Label(self.root, text="Это точно ты? Введи пароль!")
        authorization_password = Entry(self.root, width=0, textvariable=self.input_password)
        self.error_text = Label(self.root,
                                text="Ошибка, пароль не подошел",
                                justify="center",
                                anchor='center', )
        authorization_button_submit = Button(self.root,
                                             text="OK",
                                             background="#555",
                                             activebackground="white",
                                             activeforeground="#556",
                                             foreground="#ccc",
                                             padx="20",  # отступ от границ до содержимого по горизонтали
                                             pady="8",  # отступ от границ до содержимого по вертикали
                                             font="16",  # высота шрифта
                                             command=self.__authorization)
        authorization_text.pack()
        authorization_password.pack()
        authorization_button_submit.pack()


class ReminderWindow(Window):
    """Окно напоминания"""

    def __init__(self):
        super().__init__()
        self.title = 'Напоминание'
        self.win_height = 200

    def is_ready(self):
        return self.ready

    def __ready(self):
        self.ready = True
        self.root.quit()
        pass

    def _special_initialization(self):
        authorization_text = Label(self.root, text="У тебя много дел на сегодня!")
        authorization_button_submit = Button(self.root,
                                             text="Готов их сделать",
                                             background="#555",
                                             activebackground="white",
                                             activeforeground="#556",
                                             foreground="#ccc",
                                             padx="20",  # отступ от границ до содержимого по горизонтали
                                             pady="8",  # отступ от границ до содержимого по вертикали
                                             font="16",  # высота шрифта
                                             command=self.__ready
                                             )
        authorization_text.pack()
        authorization_button_submit.pack()
