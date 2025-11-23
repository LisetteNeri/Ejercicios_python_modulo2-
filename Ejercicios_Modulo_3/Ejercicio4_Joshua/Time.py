def formatear_numero(valor):
    return str(valor).zfill(2)

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        h = formatear_numero(self.__hours)
        m = formatear_numero(self.__minutes)
        s = formatear_numero(self.__seconds)
        return h + ":" + m + ":" + s

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)