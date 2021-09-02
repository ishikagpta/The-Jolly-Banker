# Fund class represents a fund and all of its functionalities. It is used inside of the Account class to create
# multiple different fund objects.
class Fund:

    # The constructor takes in the code of the fund, the name of the fund, and the amount of money in the fund
    def __init__(self, code, name, amount):
        self.__code = code
        self.__name = name
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def add_amount(self, new_amount):
        self.__amount += new_amount

    def subtract_amount(self, new_amount):
        self.__amount -= new_amount

    def set_amount(self, new_amount):
        self.__amount = new_amount

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code
