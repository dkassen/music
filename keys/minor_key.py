from . import Key


class MinorKey(Key):
    INTERVALS_IN_HALF_STEPS = [2, 1, 2, 2, 1, 2, 2]

    def notes(self):