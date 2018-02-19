class Accidental:
    def symbol(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError

    def half_step_value(self):
        raise NotImplementedError

    @staticmethod
    def new(name):
        switcher = {
            'sharp': Sharp,
            'flat': Flat,
            'natural': Natural
        }

