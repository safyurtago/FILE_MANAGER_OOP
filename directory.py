from container import Container


class Directory (Container):
    def __init__(self, name: str):
        super().__init__(name, "DIRECTORY")
        self.__contents = list()

    def contents(self):
        return self.__contents

    def add(self, container):
        self.__contents.append(container)

    def delete(self, cont):
        for container in self.__contents:
            if container.get_name() == cont:
                self.__contents.remove(container)

    def size(self):
        full_size = 0

        for container in self.__contents:
            full_size += container.size()

        return full_size

    def __str__(self):
        return "%10s | %10s, %5d KB" % (self.get_signature(), self.get_name(), self.size())
