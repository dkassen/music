from . import Key


class MinorKey(Key):
    INTERVALS_IN_HALF_STEPS = [0, 2, 3, 5, 7, 8, 10, 12]

    def notes(self):
        pass