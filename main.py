from tkinter import Tk
#from tkinter import Button
#from tkinter import Label, Entry
import window_cl
import data_cl


# def authorization(win_width, win_height):
#     authorization_root = Tk()
#     authorization_root.geometry(str(win_width) + 'x' + str(win_height))
#     root.title("Авторизация")
#     authorization_text = Label(authorization_root, text="Это точно ты? Введи пароль!")
#     authorization_password = Entry(authorization_root, width=0)
#     authorization_button_submit = Button(authorization_root, text="OK",
#                                          activebackground="pink",
#                                          activeforeground="blue",
#                                          foreground="red",
#                                          command=is_user(authorization_password))
#     authorization_button_submit.place(x=30, y=40)
#     authorization_button_submit.pack()
#     authorization_password.pack()
#     authorization_text.pack()
#
# def is_user(authorization_password):
#     if str(authorization_password) == "223":
#         pass
#
#
#
# def submit():
#     authorization(win_width, win_height)
#     return 0
#print(locals())
#W = window_cl.Window().create()
#print(locals())
# G = window_cl.AuthorizationWindow()
# G.create()
# if G.is_authorization_complete():
#     del G
# print(locals())

# T = window_cl.ReminderWindow()
# T.create()
# print(locals())
# #if T.is_ready():
#     #del T

Z = window_cl.MainWindow()
Z.create()


# root = Tk()
# win_width = 300
# win_height = 200
# root.geometry(str(win_width) + 'x' + str(win_height))
# root.title("Ежедневник")
# button_submit = Button(root, text="OK", activebackground="pink", activeforeground="blue", foreground="red",
#                        command=submit)
# button_submit.place(x=30, y=40)
# button_submit.pack()
# root.mainloop()
