from . import Key


class MajorKey(Key):
    INTERVALS_IN_HALF_STEPS = [2, 1, 2, 2, 1, 2, 2]

    def notes(self):
