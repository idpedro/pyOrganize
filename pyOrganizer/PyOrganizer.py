from os.path import expanduser
class PyOrganizer:
    def __init__(self, path = expanduser('~/')):
        self.__path = path
    @property
    def path(self):
        return str(self.__path)