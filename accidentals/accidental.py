class Accidental:
    def __new__(cls, name):
        from accidentals import Flat, Natural, Sharp

        if cls is Accidental:
            name = name.lower()
            if name == 'flat':
                return super().__new__(Flat)
            if name == 'sharp':
                return super().__new__(Sharp)
            return super().__new__(Natural)
        super().__new__(cls)

    @property
    def symbol(self):
        return self.__class__.SYMBOL

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def half_step_value(self):
        return self.__class__.HALF_STEP_VALUE

