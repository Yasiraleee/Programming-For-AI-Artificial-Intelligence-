class account:
    def __init__(self, ac, ab, sc):
        self.__ac = ac
        self.__ab = ab
        self.__sc = sc

    def printing(self):
        print(self.__ac)
        print(self.__ab)
        print(self.__sc)


a = account(1, 2, 3)
a.printing()