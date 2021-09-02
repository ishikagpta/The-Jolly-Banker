from fund import Fund

# This class represents a bank account, its funds, and transactions/transaction history
class Account:

    # The constructor takes in the first name, last name, identifier and creates an account and its needed funds
    def __init__(self, first_name, last_name, identifier):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__identifier = identifier
        self.__money_market = Fund(0, "Money Market", 0)
        self.__prime_money_market = Fund(1, "Prime Money Market", 0)
        self.__long_term_bond = Fund(2, "Long-Term Bond", 0)
        self.__short_term_bond = Fund(3, "Short-Term Bond", 0)
        self.__500_index = Fund(4, "500 Index Fund", 0)
        self.__capital_value = Fund(5, "Capital Value Fund", 0)
        self.__growth_equity = Fund(6, "Growth Equity Fund", 0)
        self.__growth_index = Fund(7, "Growth Index Fund", 0)
        self.__value = Fund(8, "Value Fund", 0)
        self.__value_stock_index = Fund(9, "Value Stock Index", 0)
        self.__transaction_history = {
            "Money Market": [],
            "Prime Money Market": [],
            "Long-Term Bond": [],
            "Short-Term Bond": [],
            "500 Index Fund": [],
            "Capital Value Fund": [],
            "Growth Equity Fund": [],
            "Growth Index Fund": [],
            "Value Fund": [],
            "Value Stock Index": []
        }
        self.__list_funds = [
            self.__money_market,
            self.__prime_money_market,
            self.__long_term_bond,
            self.__short_term_bond,
            self.__500_index,
            self.__capital_value,
            self.__growth_equity,
            self.__growth_index,
            self.__value,
            self.__value_stock_index
        ]

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_id(self):
        return self.__identifier

    def get_fund(self, fund_str):
        if fund_str == "Money Market":
            return self.__money_market
        elif fund_str == "Prime Money Market":
            return self.__prime_money_market
        elif fund_str == "Long-Term Bond":
            return self.__long_term_bond
        elif fund_str == "Short-Term Bond":
            return self.__short_term_bond
        elif fund_str == "500 Index Fund":
            return self.__500_index
        elif fund_str == "Capital Value Fund":
            return self.__capital_value
        elif fund_str == "Growth Equity Fund":
            return self.__growth_equity
        elif fund_str == "Growth Index Fund":
            return self.__growth_index
        elif fund_str == "Value Fund":
            return self.__value
        elif fund_str == "Value Stock Index":
            return self.__value_stock_index

    # A function that takes the name of the fund, the amount to deposit and a string of the transaction to add to
    # history. It adds that amount to the related fund and adds this transaction to the transaction history.
    def deposit(self, fund_str, amount, transaction_str):
        fund = self.get_fund(fund_str)
        fund.add_amount(amount)
        self.add_transaction_history(fund_str, transaction_str)

    # A function that takes the name of the fund, the amount to withdraw and a string of the transaction to add
    # to history. It withdraws that amount from the related fund and adds this transaction to the transaction history.
    def withdraw(self, fund_str, amount, transaction_str):
        # if the fund has enough amount to withdraw then the transaction is processed
        fund = self.get_fund(fund_str)
        fund_amount = fund.get_amount()
        if fund_amount >= amount:
            fund.subtract_amount(amount)
            self.add_transaction_history(fund_str, transaction_str)
        # if the fund doesn't have the needed amount then it's checked if it's a money fund and then checks if
        # both Money Market and Prime Money Market funds have the needed amount. If they do have them then the
        # transaction is processed. Otherwise, a failure message will be added
        elif fund_amount < amount:
            if fund.get_name() == "Money Market" or fund.get_name() == "Prime Money Market":
                if self.__money_market.get_amount() + self.__prime_money_market.get_amount() >= amount:
                    if fund.get_name() == "Money Market":
                        money_available = fund.get_amount()
                        fund.subtract_amount(money_available)
                        transaction_1 = transaction_str.split()[0:2]
                        transaction_1 = " ".join(transaction_1)
                        transaction_1_rem = transaction_str.split()[3:]
                        transaction_1_rem = " ".join(transaction_1_rem)
                        transaction_1 += f" {money_available}{transaction_1_rem}"
                        self.add_transaction_history("Money Market", transaction_1)
                        amount -= money_available
                        self.__prime_money_market.subtract_amount(amount)
                        transaction_2 = transaction_str.split()[0:2]
                        transaction_2 = " ".join(transaction_2)
                        transaction_2 = transaction_2[:-1]
                        transaction_2_rem = transaction_str.split()[3:]
                        transaction_2_rem = " ".join(transaction_1_rem)
                        transaction_2 += f"1 {amount}{transaction_2_rem}"
                        self.add_transaction_history("Prime Money Market", transaction_2)
                    elif fund.get_name() == "Prime Money Market":
                        money_available = fund.get_amount()
                        fund.subtract_amount(money_available)
                        transaction_1 = transaction_str.split()[0:2]
                        transaction_1 = " ".join(transaction_1)
                        transaction_1_rem = transaction_str.split()[3:]
                        transaction_1_rem = " ".join(transaction_1_rem)
                        transaction_1 += f" {money_available}{transaction_1_rem}"
                        self.add_transaction_history("Prime Money Market", transaction_1)
                        amount -= money_available
                        self.__money_market.subtract_amount(amount)
                        transaction_2 = transaction_str.split()[0:2]
                        transaction_2 = " ".join(transaction_2)
                        transaction_2 = transaction_2[:-1]
                        transaction_2_rem = transaction_str.split()[3:]
                        transaction_2_rem = " ".join(transaction_1_rem)
                        transaction_2 += f"0 {amount}{transaction_2_rem}"
                        self.add_transaction_history("Money Market", transaction_2)

                else:
                    print(f"ERROR: Not enough funds to withdraw {amount} from {self.__first_name} {self.__last_name} {fund_str}")
            # if the fund doesn't have the needed amount then it's checked if it's a bond fund and then checks if
            # both Long-Term Bond and Short-Term Bond funds have the needed amount. If they do have them then the
            # transaction is processed. Otherwise, a failure message will be added
            elif fund.get_name() == "Long-Term Bond" or fund.get_name() == "Short-Term Bond":

                if self.__long_term_bond.get_amount() + self.__short_term_bond.get_amount() >= amount:
                    if fund.get_name() == "Long-Term Bond":
                        money_available = fund.get_amount()
                        fund.subtract_amount(money_available)
                        transaction_1 = transaction_str.split()[0:2]
                        transaction_1 = " ".join(transaction_1)
                        transaction_1_rem = transaction_str.split()[3:]
                        transaction_1_rem = " ".join(transaction_1_rem)
                        transaction_1 += f" {money_available}{transaction_1_rem}"
                        self.add_transaction_history("Long-Term Bond", transaction_1)
                        amount -= money_available
                        self.__short_term_bond.subtract_amount(amount)
                        transaction_2 = transaction_str.split()[0:2]
                        transaction_2 = " ".join(transaction_2)
                        transaction_2 = transaction_2[:-1]
                        transaction_2_rem = transaction_str.split()[3:]
                        transaction_2_rem = " ".join(transaction_1_rem)
                        transaction_2 += f"3 {amount}{transaction_2_rem}"
                        self.add_transaction_history("Short-Term Bond", transaction_2)
                    elif fund.get_name() == "Short-Term Bond":
                        money_available = fund.get_amount()
                        fund.subtract_amount(money_available)
                        transaction_1 = transaction_str.split()[0:2]
                        transaction_1 = " ".join(transaction_1)
                        transaction_1_rem = transaction_str.split()[3:]
                        transaction_1_rem = " ".join(transaction_1_rem)
                        transaction_1 += f" {money_available}{transaction_1_rem}"
                        self.add_transaction_history("Short-Term Bond", transaction_1)
                        amount -= money_available
                        self.__long_term_bond.subtract_amount(amount)
                        transaction_2 = transaction_str.split()[0:2]
                        transaction_2 = " ".join(transaction_2)
                        transaction_2 = transaction_2[:-1]
                        transaction_2_rem = transaction_str.split()[3:]
                        transaction_2_rem = " ".join(transaction_1_rem)
                        transaction_2 += f"2 {amount}{transaction_2_rem}"
                        self.add_transaction_history("Long-Term Bond", transaction_2)
            else:
                self.add_transaction_history(fund_str, transaction_str + " (Failed)")
                print(f"ERROR: Not enough funds to withdraw {amount} from {self.__last_name} {self.__first_name} {fund_str}")

    #  A function that takes the name of the first fund, the second fund, and the amount to transfer.
    #  It transfers the amount from the first fund to the second fund.
    def transfer(self, from_fund, to_fund, amount):
        first_fund = self.get_fund(from_fund)
        second_fund = self.get_fund(to_fund)
        if first_fund.get_amount() >= amount:
            first_fund.subtract_amount(amount)
            second_fund.add_amount(amount)
            return True
        else:
            print(f"ERROR: Not enough funds to withdraw ${amount} from {self.__last_name} {self.__first_name} {from_fund} to {to_fund}")
            return False

    # A function that prints the history of all transactions in an account.
    def get_all_transactions_history(self):
        print(f'Transaction History for {self.__last_name} {self.__first_name} by fund.')
        for fund in self.__list_funds:
            # if the fund doesn't have a transaction history then nothing is printed
            if len(self.__transaction_history[fund.get_name()]) > 0:
                print(f'{fund.get_name()}: ${fund.get_amount()}')
                for transaction in self.__transaction_history[fund.get_name()]:
                    print(f'  {transaction}')

    # A function that prints the history of all transactions in a certain fund in an account.
    def get_fund_transaction_history(self, fund_name):
        fund = self.get_fund(fund_name)
        # if the fund doesn't have a transaction history then nothing is printed
        if len(self.__transaction_history[fund_name]) > 0:
            print(f'Transaction History for {self.__last_name} {self.__first_name} {fund_name}: ${fund.get_amount()}')
            for transaction in self.__transaction_history[fund_name]:
                print(f'  {transaction}')

    # A function that adds a a transaction history string to the transaction history dictionary.
    # It also adds a (Failed) ending if the transaction failed.
    def add_transaction_history(self, fund_name, transaction, failed=False):
        if failed:
            self.__transaction_history[fund_name].append(transaction + " (Failed)")
        else:
            self.__transaction_history[fund_name].append(transaction)

    # A function that prints all data related to the account. Name, id, fund data, and transaction history.
    def print_acc_data(self):
        print(f'{self.__last_name} {self.__first_name} Account ID: {self.__identifier}')
        for fund in self.__list_funds:
            print(f'    {fund.get_name()}: ${fund.get_amount()}')
        print()
