from tkinter import Tk, Label, Button, Entry, PhotoImage, StringVar


class Window:
    def __init__(self):
        self.win_width = 400
        self.win_height = 800
        self.title = ''
        self.root = Tk()
        print('created')

    def _special_initialization(self):
        print('Я вызван')
        return 0

    def create(self):
        self.root.geometry(str(self.win_width) + 'x' + str(self.win_height))
        self.root.title(self.title)
        print('-')
        self._special_initialization()
        print('+')
        self.root.mainloop()
        print('mainloop')
        return 0

    def stop(self):
        self.root.destroy()


class AuthorizationWindow(Window):
    def __init__(self):
        super().__init__()
        self.title = 'Авторизация'
        self.true_password = '1239'
        self.input_password = StringVar()
        self.flag = False
        self.authorization_complete = False

    def is_authorization_complete(self):
        return self.authorization_complete

    def __is_user(self, password: str) -> bool:
        print(password)
        print(self.true_password)
        if password == self.true_password:
            return True
        else:
            return False

    def __authorization(self):
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
                           anchor='center',)
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
