from file import File
from directory import Directory
from os import system


ERROR_TEXT = "\nBuyuruqda xatolik mavjud.\n\n"
HELP_TEXT = """FILE MANAGER.

help                - Yordam oynasi
pwd                 - Hozir turgan papkani ko'rsatish
file <fayl_nomi>    - Yangi fayl yaratish
dir <papka_nomi>    - Yangi papka yaratish
ls                  - Fayllarni ko'rish
    ls a            - Barcha fayllarni ko'rish
cd <papka_nomi>     - Papka ichiga o'tish
back                - Bir pog'ona ortga chiqish
cat <fayl_nomi>     - Faylni korish
edit <fayl_nomi>    - Faylni tahrirlash
hile <obyekt_nomi>  - Fayl yoki papkani yashirish
"""


class Manager:
    def __init__(self):
        self.__current_folder = Directory("root")
        self.__parents = list()

    def command(self, cmd, key=None):
        if cmd == "help":
            print(HELP_TEXT)
        elif cmd == "file":
            self.__create(key, False)
        elif cmd == "dir":
            self.__create(key, True)
        elif cmd == "ls":
            if key == 'a':
                self.__show()
            else:
                self.__show(False)
        elif cmd == "cd":
            self.__change_dir(key)
        elif cmd == "back":
            self.__go_back()
        elif cmd == "cat":
            self.__show_file(key)
        elif cmd == "edit":
            self.__edit_file(key)
        elif cmd == "hide":
            self.__set_hidden(key)
        elif cmd == "pwd":
            self.__pwd()
        else:
            print(ERROR_TEXT + HELP_TEXT)

    def __create(self, name, is_dir):
        f = Directory(name) if is_dir else File(name)
        self.__current_folder.add(f)

    def __show(self, hidden=True):
        if hidden:
            for container in self.__current_folder.contents():
                print(container)
        else:
            for container in self.__current_folder.contents():
                if container.is_hidden():
                    continue

                print(container)

    def __change_dir(self, name):
        for directory in self.__current_folder.contents():
            if directory.get_name() == name and directory.get_signature() == "DIRECTORY":
                self.__parents.append(self.__current_folder)
                self.__current_folder = directory

    def __go_back(self):
        if len(self.__parents) == 0:
            print("This is a parent directory")
        else:
            self.__current_folder = self.__parents.pop()

    def __show_file(self, name):
        for file in self.__current_folder.contents():
            if file.get_name() == name and file.get_signature() == "FILE":
                print(file.contents())

    def __edit_file(self, name):
        system("clear")
        add = int(input("Open mode [1=append | 0=write]: "))
        text = input("Enter text:\n")
        for file in self.__current_folder.contents():
            if file.get_name() == name and file.get_signature() == "FILE":
                file.add_content(text, add)

    def __set_hidden(self, name):
        for container in self.__current_folder.contents():
            if container.get_name() == name:
                container.set_hidden()

    def __pwd(self):
        path = ""
        for directory in self.__parents:
            path += directory.get_name() + '/'

        path += self.__current_folder.get_name() + '/'
        print(path)

    def __show_file(self, name):
        for i in self.__parents:
            if name == i.get_name():
                print(i.contents())
