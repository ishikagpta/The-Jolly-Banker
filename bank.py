from queue import Queue
from bst import BinarySearchTree, Node
from account import Account
from transaction import Transaction

# This class handles all of the functionalities of a Bank such as reading and storing transactions, creating accounts,
# passing transactions data to accounts, and handling any transactions that include multiple accounts.
# At the end, it prints all open accounts and funds within the accounts.
class Bank:

    # This constructor takes in the file and stores each line of transactions/accounts into a queue of Transaction
    # objects. It also creates an open account array that stores all the identifiers of open accounts.
    def __init__(self, filename):
        self.__filename = filename
        self.__transactions_queue = Queue()
        self.__accounts = BinarySearchTree()
        self.__open_accounts = []
        # This is a dictionary used to convert fund nums to their names
        self.__fund_num_to_name = {
            0: "Money Market",
            1: "Prime Money Market",
            2: "Long-Term Bond",
            3: "Short-Term Bond",
            4: "500 Index Fund",
            5: "Capital Value Fund",
            6: "Growth Equity Fund",
            7: "Growth Index Fund",
            8: "Value Fund",
            9: "Value Stock Index"
        }

    # A function that reads the file of transactions and stores it as transaction objects in the internal Queue.
    # Phase #1: Read all transactions form file and save to __transactions_queue
    def read_file(self):
        with open(self.__filename) as file:
            for line in file:
                if line != "":
                    self.__transactions_queue.put(line.strip())
# Phase #2: process all transactions

    # A function that executes all the transactions in the Queue.
    def execute_transactions(self):
        # Checking if the queue is not empty yet and then pulling the transaction and passing it to the
        # intended function
        while not self.__transactions_queue.empty():
            transaction_str = self.__transactions_queue.get()
            transaction = Transaction(transaction_str)
            # Validating transaction.
            if not transaction.get_validity():
                continue
            if transaction.get_type() == "O":
                self.__open_account(transaction)
            elif transaction.get_type() == "D":
                self.__deposit_to_account(transaction)
            elif transaction.get_type() == "W":
                self.__withdraw_from_account(transaction)
            elif transaction.get_type() == "T":
                if transaction.get_first_id() == transaction.get_second_id():
                    self.__transfer_within(transaction)
                else:
                    self.__transfer_to_another_acc(transaction)
            elif transaction.get_type() == "H":
                trans = transaction.get_transaction_str().split()[1]
                # checking if this is asking for a fund's history or an account's history
                if len(trans) == 4:
                    self.__history_of_all_funds(transaction)
                else:
                    self.__history_of_single_fund(transaction)

    # A function that takes in a transaction object and verifies the account identifier is not in the BST and then
    # creates it and adds it to the BST.
    def __open_account(self, transaction):
        identifier = int(transaction.get_first_id())
        # check if the account is already their - with this id
        if self.__accounts.contains(identifier):
            print(f'ERROR: Account {identifier} is already open. Transaction refused.')
        # check if the id is bigger or smaller than 4 nums
        elif identifier > 9999 or identifier < 1000:
            print(f'ERROR: Account {identifier} is an invalid ID. Transaction refused')
        else:
            # creating the account based on the transaction data and then inserting it to the BST
            new_account = Account(transaction.get_first_name(), transaction.get_last_name(), transaction.get_first_id())
            self.__accounts.insert(identifier, new_account)
            self.__open_accounts.append(identifier)

    # A function that takes in a transaction object and extracts the needed data(id, amount, fund name).
    # Then, it checks if the id is in the accounts(BST). If it's there, it passes to that account the transaction
    # data to deposit to the account fund. Otherwise it prints an error.
    def __deposit_to_account(self, transaction):
        # getting the needed data from the transaction to deposit it into the account
        identifier = int(transaction.get_first_id())
        amount = int(transaction.get_amount())
        fund_name = self.__fund_num_to_name[int(transaction.get_first_fund())]
        # verify the account is in the BST then deposit
        if self.__accounts.contains(identifier):
            queried_account = self.__accounts.get(identifier)
            queried_account.deposit(fund_name, amount, transaction.get_transaction_str())
        else:
            print(f'ERROR: Account {identifier} not found. Transferal refused.')

    # A function that takes in a transaction object and extracts the needed data(id, amount, fund name).
    # Then, it checks if the id is in the accounts(BST). If it's there, it passes to that account the transaction
    # data to withdraw from the account fund. Otherwise it prints an error.
    def __withdraw_from_account(self, transaction):
        # getting the needed data from the transaction to withdraw from the account
        identifier = int(transaction.get_first_id())
        amount = int(transaction.get_amount())
        fund_name = self.__fund_num_to_name[int(transaction.get_first_fund())]
        if self.__accounts.contains(identifier):
            queried_account = self.__accounts.get(identifier)
            queried_account.withdraw(fund_name, amount, transaction.get_transaction_str())
        else:
            print(f'ERROR: Account {identifier} is an invalid ID. Transaction refused')

    # A function that takes in a transaction object and extracts the needed data(id, amount, from fund, to fund).
    # Then, it checks if the id is in the accounts(BST). If it's there, it passes to that account the transaction
    # data to withdraw from from_fund to deposit and transfer to to_fund. Otherwise it prints an error.
    def __transfer_within(self, transaction):
        # Getting the needed data to transfer within the same account
        identifier = int(transaction.get_first_id())
        amount = int(transaction.get_amount())
        from_fund = self.__fund_num_to_name[int(transaction.get_first_fund())]
        to_fund = self.__fund_num_to_name[int(transaction.get_second_fund())]
        # verifying the account availability and then checking if it failed or not to add the (Failure) statement to
        # the transaction history
        if self.__accounts.contains(identifier):
            queried_account = self.__accounts.get(identifier)
            transfer_result = queried_account.transfer(from_fund, to_fund, amount)
            if transfer_result:
                queried_account.add_transaction_history(from_fund, transaction.get_transaction_str())
                queried_account.add_transaction_history(to_fund, transaction.get_transaction_str())
            else:
                queried_account.add_transaction_history(from_fund, transaction.get_transaction_str(), True)
                queried_account.add_transaction_history(to_fund, transaction.get_transaction_str(), True)
        else:
            print(f'ERROR: Account {identifier} is an invalid ID. Transaction refused')

    # A function that takes in a transaction object and extracts the needed
    # data(first and second ids for the accounts, first and second funds, and the amount to transfer).
    # Then, it checks if the ids are in the accounts(BST). If they're there, it passes to the accounts the transactions
    # data to withdraw from the first fund and account and deposit to the second fund and account,
    # transferring the amount. Otherwise it prints an appropriate error.
    def __transfer_to_another_acc(self, transaction):
        # getting the needed data from the transaction to transfer between 2 __accounts
        first_identifier = int(transaction.get_first_id())
        second_identifier = int(transaction.get_second_id())
        amount = int(transaction.get_amount())
        first_fund = self.__fund_num_to_name[int(transaction.get_first_fund())]
        second_fund = self.__fund_num_to_name[int(transaction.get_second_fund())]
        # checking the 2 __accounts are available
        if self.__accounts.contains(first_identifier) and self.__accounts.contains(second_identifier):
            first_account = self.__accounts.get(first_identifier)
            second_account = self.__accounts.get(second_identifier)
            first_account_fund = first_account.get_fund(first_fund)
            # checking if the first account has enough money to transfer
            if first_account_fund.get_amount() >= amount:
                first_account.withdraw(first_fund, amount, transaction.get_transaction_str())
                second_account.deposit(second_fund, amount, transaction.get_transaction_str())
            else:
                # if not enough money, then the failure statement is added to the transaction
                print(f'ERROR: Account {first_identifier} has insufficient funds. Transaction refused.')
                first_account.add_transaction_history(first_fund, transaction.get_transaction_str(), True)
                second_account.add_transaction_history(second_fund, transaction.get_transaction_str(), True)
        # checking if one of the __accounts is missing - or both of them
        elif self.__accounts.contains(first_identifier) and not self.__accounts.contains(second_identifier):
            print(f'ERROR: Account {second_identifier} not found. Transferal refused.')
        elif not self.__accounts.contains(first_identifier) and self.__accounts.contains(second_identifier):
            print(f'ERROR: Account {first_identifier} not found. Transferal refused.')
        else:
            print(f'ERROR: No account was found. Transferal refused.')

    # A function that takes in a transaction object and extracts the needed data(id,  fund name).
    # Then, it checks if the id is in the accounts(BST). If it's there, it passes to that account the transaction
    # data to print the transaction history of that fund within that account. Otherwise it prints an error.
    def __history_of_single_fund(self, transaction):
        # getting the data needed and verifying the account then pulling the data
        identifier = int(transaction.get_first_id())
        fund_name = self.__fund_num_to_name[int(transaction.get_first_fund())]
        if self.__accounts.contains(identifier):
            queried_account = self.__accounts.get(identifier)
            queried_account.get_fund_transaction_history(fund_name)
        else:
            print(f'ERROR: Account {identifier} is an invalid ID. Transaction refused')

    # A function that takes in a transaction object and extracts the needed data(id).
    # Then, it checks if the id is in the accounts(BST). If it's there, it passes to that account the transaction
    # data to print the transaction history of all funds within that account. Otherwise it prints an error.
    def __history_of_all_funds(self, transaction):
        # getting the data needed and verifying the account then pulling the data
        identifier = int(transaction.get_first_id())
        if self.__accounts.contains(identifier):
            queried_account = self.__accounts.get(identifier)
            queried_account.get_all_transactions_history()
        else:
            print(f'ERROR: Account {identifier} is an invalid ID. Transaction refused')
# 3. Phase #3: Print all __accounts

    # A function that prints the data of all accounts in the bank.
    def print_all_open_accounts(self):
        print("\nProcessing Done. Final Balances")
        # looping through the data and printing the info
        for identifier in self.__open_accounts:
            self.__accounts.get(identifier).print_acc_data()
