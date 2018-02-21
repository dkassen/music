class Tone:
    def __init__(self, frequency):
        self._frequency = abs(frequency)  # Hertz (Hz)

    @property
    def frequency(self):
        return self._frequency