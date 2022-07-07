class Email:
    def __init__(self, text):
        self.__text = text
        if self.check_corectness():
            self.__correct = True
        else:
            self.__correct = False

    def __str__(self):
        return self.__text

    @property
    def correct(self):
        return self.__correct

    def check_corectness(self):
        if self.__text.count('@') != 1:  # emails must have only on @ sign
            return False

        if self.__text[0] == '@':  # length of the part before the @ is 0
            return False

        first_split = self.__text.split('@')
        second_split = first_split[1].split('.')

        if len(second_split[0]) == 0:  # length of the part between @  and . is 0
            return False

        if len(second_split[-1]) == 0 or len(second_split[-1]) > 4:  # length of the part after the last . is 0 or >4
            return False
        return second_split[-1].isalnum()
