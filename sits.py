# Модуль для вычисления количества приседаний

# Здесь должен быть твой код

from scrollLabel import *

class Sits(ScrollLabel):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        text = 'Осталось приседаний: ' + str(self.total)
        super().__init__(text, **kwargs)

    def next(self, *args):
        self.current +=1
        self.remain = max(0, self.total - self.current)
        self.text = 'Осталось приседаний: ' + str(self.remain)
        super().set_text(self.text)























