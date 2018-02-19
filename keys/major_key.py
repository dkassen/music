from . import Key


class MajorKey(Key):
    INTERVALS_IN_HALF_STEPS = [0, 2, 4, 5, 7, 9, 11, 12]

    def notes(self):
        pass
        # not sure how to generate this yet