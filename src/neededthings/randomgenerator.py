import random
class Random:
    def __init__(self):
        self._random = random

    def randint_zero_to_six(self):
        return random.randint(0, 6)
