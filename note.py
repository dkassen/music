from tone import Tone
from accidentals.accidental import Accidental
from constants import HALF_STEPS_PER_OCTAVE, C0_FREQUENCY


# A note is a tone that has a name and an octave number
class Note(Tone):
    NAMES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    NEXT_NOTE_NAME = {
        'C': 'D',
        'D': 'E',
        'E': 'F',
        'F': 'G',
        'G': 'A',
        'A': 'B',
        'B': 'C',
    }
    HALF_STEPS_FROM_C = {
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7,
        'A': 9,
        'B': 11,
    }

    def __init__(self, name, accidental=None, octave_number=0):
        self._name = name
        self._accidental = accidental or Accidental('natural')
        self._octave_number = octave_number
        self._validate()
        self._set_frequency()
        super().__init__(self, self._frequency)

    @property
    def name(self):
        return self._name

    @property
    def accidental(self):
        return self._accidental

    @property
    def octave_number(self):
        return self._octave_number

    @classmethod
    def for_name_and_pitch(cls, name, half_steps_from_c0):
        accidental = None
        natural_note = cls(name)
        if natural_note.half_steps_from_c0() == half_steps_from_c0:
            return natural_note
        if natural_note.half_steps_from_c0() < half_steps_from_c0:
            accidental = Accidental('sharp')
        elif natural_note.half_steps_from_c0() > half_steps_from_c0:
            accidental = Accidental('flat')
        return cls(name, accidental)

    def _set_frequency(self):
        self._frequency = C0_FREQUENCY * self._frequency_multiplier()
        return

    def _frequency_multiplier(self):
        return 2 ** (self.half_steps_from_c0() / HALF_STEPS_PER_OCTAVE)

    def half_steps_from_c0(self):
        return self._octave_half_steps() + self._half_steps_from_c() + self._accidental.half_step_value()

    def _octave_half_steps(self):
        return self._octave_number * HALF_STEPS_PER_OCTAVE

    def _half_steps_from_c(self):
        return self.__class__.HALF_STEPS_FROM_C[self._name]

    def _validate(self):
        self._validate_octave_number()
        self._validate_name()
        self._validate_accidental()

    def _validate_octave_number(self):
        if type(self._octave_number) is not int:
            raise TypeError('octave_number must be an int')

    def _validate_accidental(self):
        if self._accidental.__class__ not in Accidental.__subclasses__():
            raise TypeError(f"accidental must be an {Accidental.__name__} subclass instance")

    def _validate_name(self):
        if self._name not in self.__class__.NAMES:
            raise ValueError(f"Name not valid, expected one of {self.__class__.NAMES.join(', ')}")
