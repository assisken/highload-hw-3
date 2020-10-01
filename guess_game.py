from enum import Enum
from random import randint


class Result(Enum):
    LESS = 'less'
    CORRECT = 'correct'
    MORE = 'more'


class GuessGame:
    def __init__(self):
        self.number = randint(1, 10)

    def guess(self, number: int) -> Result:
        if number > self.number:
            return Result.LESS
        elif number < self.number:
            return Result.MORE
        else:
            return Result.CORRECT

    def restart(self):
        self.number = randint(1, 10)
