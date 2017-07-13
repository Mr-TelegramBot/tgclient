import time
import threading



class Timer:


    class Thread(threading.Thread):
        def __init__(self, second, action):

            super().__init__()

            self.__second = int(second)
            self.__action = action

        def run(self):

            time.sleep(self.__second)

            self.__action()

    def __init__(self, second, action):
        self.Thread(second, action).start()

    @staticmethod
    def min_to_sec(minute):

        return int(minute) * 60

    @staticmethod
    def hour_to_sec(hour):

        return (int(hour) * 60) * 60
