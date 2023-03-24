from container import Container


class File (Container):
    def __init__(self, name):
        super().__init__(name, "FILE")
        self.__content = str()

    def add_content(self, text: str, append: bool):
        if append:
            self.__content += text
        else:
            self.__content = text

    def size(self):
        return len(self.__content)

    def contents(self):
        return self.__content

    def __str__(self):
        return "%10s | %10s, %5d KB" % (self.get_signature(), self.get_name(), self.size())
