from . import MinorKey, MajorKey


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
    # maybe something to do with minor and major intervals