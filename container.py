from random import randint as rd


class Container:
    def __init__(self, name: str, signature: str):
        self.__signature = signature
        self.__id = rd(1000, 10000)
        self._name = name
        self.__hidden = False

    def rename(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def get_id(self):
        return self.__id

    def is_hidden(self):
        return self.__hidden

    def set_hidden(self):
        self.__hidden = not self.__hidden

    def get_signature(self):
        return self.__signature

    def size(self):
        pass

    def contents(self):
        pass
