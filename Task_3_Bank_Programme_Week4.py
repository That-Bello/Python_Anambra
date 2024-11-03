# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:41:37 2024

TASK 3

Create a class Bank Account with methods to deposit, 
withdraw, and check balance.

@author: Mr Bello
"""

class BankAccount:
    def __init__(self):
        self.balance = 0
        print("The Bank Account Deposit / Withdraw")

    def accDeposit(self):
        dep_Amount = int(input("Enter the deposit amount: "))
        self.balance += dep_Amount
        print(f"Your new account balance is: {self.balance}")
        
    def accWithdrawal(self):
        withdrawals_Amount = int(input("Enter the amount to withdraw: "))
        if self.balance >= withdrawals_Amount:
            self.balance -= withdrawals_Amount
            print(f"Your current balance is: {self.balance}")
        else:
            print("Insufficient balance")
            
account = BankAccount()
account.accDeposit()
account.accWithdrawal()


