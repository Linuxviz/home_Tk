import window_cl


class MainCommander():
    def __init__(self):
        self.start_rem_window()

    def start_rem_window(self):
        obj = window_cl.ReminderWindow()
        obj.create()
        if obj.is_ready():
            obj.stop()
            del obj
            self.start_authorization_window()
    def start_authorization_window(self):
        obj = window_cl.AuthorizationWindow()
        obj.create()
        if obj.is_authorization_complete():
            obj.stop()
            del obj
            self.start_main_window()

    def start_main_window(self):
        obj = window_cl.MainWindow()
        obj.create()


if __name__ == '__main__':
    run = MainCommander()
