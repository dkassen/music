from . import MinorKey, MajorKey
from ..note import Note

class Key:
    def __new__(cls, minor=False):
        if cls == Key:
            if minor:
                return super().__new__(MinorKey)
            else:
                return super().__new__(MajorKey)
        super().__new__(cls)

    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root

    def notes(self):
        [self.generate_note(interval, interval_half_steps)
         for interval, interval_half_steps in enumerate(self.__class__.INTERVALS_IN_HALF_STEPS, 1)]

    def generate_note(self, interval, half_steps_from_root):
        name_index = (Note.NAMES.index(self.root.name) + interval) % Note.NAMES.__len__()
        name = Note.NAMES[name_index]
        half_steps_from_c0 = self._root.half_steps_from_c0() + half_steps_from_root
        return Note.for_name_and_pitch(name, half_steps_from_c0)
