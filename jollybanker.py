from queue import Queue
from bst import BinarySearchTree, Node
from account import Account
from bank import Bank

# Main driver for JollyBanker which reads the files, executes the transactions,
# and prints all open accounts and transactions


class JollyBanker:
    def main():
        jolly_banker = Bank("BankTestIn.txt")
        jolly_banker.read_file()
        jolly_banker.execute_transactions()
        jolly_banker.print_all_open_accounts()


if __name__ == '__main__':
    JollyBanker.main()
