
**Goal**

Design a database (Personal Finance Tracker) to track expenses, income, and budgets.
You can include features like adding transactions, categorizing expenses, and generating reports on spending habits.
---
**Methodology**

I will write various SQL scripts in various .sql files
Each file will be for a specific task

Once that's done, I will run the main file, which creates the database, initializes the connection, and imports all other .sql files
I will use the sqlite3 and argparse libraries
---
**Specifics**

- Categories of transactions : Spending, Revenue, Deposit, Withdrawal
    - Categories of Spending : Nutrition, Clothing, Housing, Transport, Investment, Distraction
    - Categories of Revenue : Salary, Dividend, Capital Gain
    - Categories of Deposit : Cash, Cheque, Wire
    - Category of Withdrawal : Cash, Cheque, Wire, Subscription

- Categories of Entities transacting :
    Friend, Employer, Broker, Merchant

- Each transaction will have :
    A unique ID, a sign (+,-) with the amount, origin and destination, date, type of transaction, type of transaction subclass, recurrence (if applicable)


(Will need a list of all)

---
**Functions**

- AddTransaction
- RemoveTransaction
- ModifyTransaction


- AddSpendingType
- RemoveSpendingType
- ModifySpendingType


- AddRevenueType
- RemoveRevenueType
- ModifyRevenueType


- AddDepositType
- RemoveDepositType
- ModifyDepositType


- AddWithdrawalType
- RemoveWithdrawalType
- ModifyWithdrawalType



- AddEntity
- RemoveEntity


- SetBudget

 