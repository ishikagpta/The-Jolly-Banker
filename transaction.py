# Transaction class represents all the different transactions read from the input file
class Transaction:

    # The constructor takes in the transaction string and gets the transaction type from the transaction string.
    # It initializes multiple attributes of the transaction to none. It also calls the update_transaction_data
    # method to update the different attributes to their appropriate data.
    def __init__(self, transaction):
        self.__transaction_str = transaction
        self.__valid = False
        self.__type = transaction[0]
        self.__first_name = None
        self.__last_name = None
        self.__first_id = None
        self.__second_id = None
        self.__first_fund = None
        self.__second_fund = None
        self.__amount = None
        self.__update_transaction_data()

    # A function that returns the type of the transaction.
    def get_type(self):
        return self.__type

    # A function that returns the transaction as a string.    
    def get_transaction_str(self):
        return self.__transaction_str

    # A function that returns the first name passed in the transaction.
    def get_first_name(self):
        return self.__first_name

    # A function that returns the last name passed in the transaction.
    def get_last_name(self):
        return self.__last_name

    # A function that returns the first id passed in the transaction.
    def get_first_id(self):
        return self.__first_id

    # A function that returns the second id passed in the transaction.
    def get_second_id(self):
        return self.__second_id

    # A function that returns the first fund passed in the transaction.
    def get_first_fund(self):
        return self.__first_fund

    # A function that returns the second fund passed in the transaction.
    def get_second_fund(self):
        return self.__second_fund

    # A function that returns the amount passed in the transaction.
    def get_amount(self):
        return self.__amount

    def get_validity(self):
        return self.__valid

    # A function that updates all the attributes of the transaction object based on the data passed.
    def __update_transaction_data(self):
        transaction = self.__transaction_str
        transaction_splitted = self.__transaction_str
        transaction_splitted = transaction_splitted.split()
        # Validating the transactions before passing them to update the attributes of the transaction object.
        if self.__type == "O":
            if not self.__validate_open(transaction):
                self.__valid = False
                return
            self.__valid = True
            self.__open_acc(transaction_splitted)
        elif self.__type == "D":
            if not self.__validate_deposit_withdraw(transaction):
                self.__valid = False
                return
            self.__valid = True
            self.__deposit_trans(transaction_splitted)
        elif self.__type == "W":
            if not self.__validate_deposit_withdraw(transaction):
                self.__valid = False
                return
            self.__valid = True
            self.__withdraw_trans(transaction_splitted)
        elif self.__type == "T":
            if not self.__validate_transfer(transaction):
                self.__valid = False
                return
            self.__valid = True
            self.__transfer_trans(transaction_splitted)
        elif self.__type == "H":
            if not self.__validate_history(transaction):
                self.__valid = False
                return
            self.__valid = True
            self.__history_trans(transaction_splitted)
        else:
            print(f'ERROR: Invalid transaction type!')

    # A function that updates the open account data in the transaction object.
    def __open_acc(self, transaction_splitted):
        self.__first_name = transaction_splitted[1]
        self.__last_name = transaction_splitted[2]
        self.__first_id = transaction_splitted[3]

    # A function that updates the deposit data in the transaction object.
    def __deposit_trans(self, transaction_splitted):
        self.__first_id = transaction_splitted[1][:-1]
        self.__first_fund = transaction_splitted[1][-1]
        self.__amount = transaction_splitted[2]

    # A function that updates the withdraw data in the transaction object.
    def __withdraw_trans(self, transaction_splitted):
        self.__first_id = transaction_splitted[1][:-1]
        self.__first_fund = transaction_splitted[1][-1]
        self.__amount = transaction_splitted[2]

    # A function that updates the transfer data in the transaction object.
    def __transfer_trans(self, transaction_splitted):
        self.__first_id = transaction_splitted[1][:-1]
        self.__first_fund = transaction_splitted[1][-1]
        self.__amount = transaction_splitted[2]
        self.__second_id = transaction_splitted[3][:-1]
        self.__second_fund = transaction_splitted[3][-1]

    # A function that updates the history data in the transaction object.
    def __history_trans(self, transaction_splitted):
        # if the transaction has an id only then this will be an all funds history
        # otherwise it will be a one fund history transaction
        if len(transaction_splitted[1]) == 4:
            self.__first_id = transaction_splitted[1]
        elif len(transaction_splitted[1]) == 5:
            self.__first_id = transaction_splitted[1][:-1]
            self.__first_fund = transaction_splitted[1][-1]

    # Validating the id to be both an integer and within the correct range of numbers.
    def __validate_id(self, identifier):
        try:
            identifier = int(identifier)
            if identifier < 1000 or identifier > 9999:
                print(f'ERROR: Invalid ID!')
                return False
        except:
            print(f'ERROR: The ID can only be numbers!')
            return False
        return True

    # Validating the fund to be both able to convert to integer and within the correct range.
    def __validate_fund(self, fund):
        try:
            fund = int(fund)
            if fund < 0 or fund > 9:
                print(f'ERROR: Invalid fund num!')
                return False
        except:
            print(f'ERROR: Invalid fund num!')
            return False
        return True

    # Validating the amount to be both an integer and a positive one.
    def __validate_amount(self, amount):
        try:
            amount = int(amount)
            if amount < 1:
                print(f'ERROR: Amount must be positive!')
                return False
        except:
            print(f'ERROR: Amount must be an integer!')
            return False
        return True

    # Validating the transaction initial character to be a correct one (O,D,W,T,H).
    def __validate_trans_type(self, type):
        if not type in ['O', 'D', 'W', 'T', 'H']:
            print(f'Invalid transaction type!')
            return False
        return True

    #  Validating the data to be in the correct format to open an account.
    def __validate_open(self, transaction):
        transaction_splitted = transaction.split()
        if len(transaction_splitted) != 4:
            print(f'ERROR: Number of parameters is wrong!')
            return False
        if not self.__validate_trans_type(transaction_splitted[0]):
            return False
        if not transaction_splitted[1].isalpha() or not transaction_splitted[2].isalpha():
            print(f'ERROR: Account holder name should be only letters!')
            return False
        if not self.__validate_id(transaction_splitted[3]):
            return False
        return True

    # Validating the data to be in the correct format to deposit or withdraw from an account.
    def __validate_deposit_withdraw(self, transaction):
        transaction_splitted = transaction.split()
        if len(transaction_splitted) != 3:
            print(f'ERROR: Number of parameters is wrong!')
            return False
        if not self.__validate_trans_type(transaction_splitted[0]):
            return False
        identifier = transaction_splitted[1][:-1]
        if not self.__validate_id(identifier):
            return False
        fund = transaction_splitted[1][-1]
        if not self.__validate_fund(fund):
            return False
        amount = transaction_splitted[2]
        if not self.__validate_amount(amount):
            return False
        return True

    # Validating the data to be in correct format to transfer.
    def __validate_transfer(self, transaction):
        transaction_splitted = transaction.split()
        if len(transaction_splitted) != 4:
            print(f'ERROR: Number of parameters is wrong!')
            return False
        if not self.__validate_trans_type(transaction_splitted[0]):
            return False
        identifier1 = transaction_splitted[1][:-1]
        if not self.__validate_id(identifier1):
            return False
        fund1 = transaction_splitted[1][-1]
        if not self.__validate_fund(fund1):
            return False
        amount = transaction_splitted[2]
        if not self.__validate_amount(amount):
            return False
        identifier2 = transaction_splitted[3][:-1]
        if not self.__validate_id(identifier2):
            return False
        fund2 = transaction_splitted[3][-1]
        if not self.__validate_fund(fund2):
            return False
        return True

    # Validating the data to be in the correct format to do a history transaction.
    def __validate_history(self, transaction):
        transaction_splitted = transaction.split()
        if len(transaction_splitted) != 2:
            print(f'ERROR: Invalid history transaction!')
            return False
        if not self.__validate_trans_type(transaction_splitted[0]):
            return False
        if len(transaction_splitted[1]) == 4:
            identifier = transaction_splitted[1]
            if not self.__validate_id(identifier):
                return False
        elif len(transaction_splitted[1]) == 5:
            identifier = transaction_splitted[1][:-1]
            if not self.__validate_id(identifier):
                return False
            fund = transaction_splitted[1][-1]
            if not self.__validate_fund(fund):
                return False
        elif len(transaction_splitted[1]) > 5 or len(transaction_splitted[1]) < 4:
            print(f'ERROR: Invalid identifier or fund!')
            return False
        return True
