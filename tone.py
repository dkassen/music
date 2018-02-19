from constants import SOUND_AIR_VELOCITY


class Tone:
    def __init__(self, frequency, intensity=0):
        self._frequency = abs(frequency)  # Hertz (Hz)
        self._phase = 0 if frequency >= 0 else 180  # degrees (˚)
        self._intensity = intensity  # Decibels (dB)

    @property
    def frequency(self):
        return self._frequency

    @property
    def intensity(self):
        return self._intensity
