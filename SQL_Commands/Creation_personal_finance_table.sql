
-- Création du tableau contenant mes catégories de transactions

CREATE TABLE IF NOT EXISTS Transactions_Types(
    Type TEXT,
    "Number of transactions" INTEGER NOT NULL,
    "Total amount" FLOAT NOT NULL

)
INSERT INTO Transactions_Types (Type) VALUES
    ('Spending'),
    ('Revenue'),
    ('Deposit'),
    ('Withdrawal');


-- Création des tableaux contenant les sous-catégories

CREATE TABLE IF NOT EXISTS Spending_Types(
    Type TEXT
)
INSERT INTO Spending_Types (Type) VALUES
    ('Nutrition'),
    ('Clothing'),
    ('Housing'),
    ('Transport'),
    ('Investment'),
    ('Distraction');
-------------------------
CREATE TABLE IF NOT EXISTS Revenue_Types(
    Type TEXT,
)
INSERT INTO Revenue_Types (Type) VALUES
    ('Salary'),
    ('Dividend'),
    ('Capital Gain');
-------------------------
CREATE TABLE IF NOT EXISTS Deposit_Types(
    Type TEXT
)
INSERT INTO Deposit_Types (Type) VALUES
    ('Cash'),
    ('Cheque'),
    ('Wire');
-------------------------
CREATE TABLE IF NOT EXISTS Withdrawal_Types(
    Type TEXT
)
INSERT INTO Withdrawal_Types (Type) VALUES
    ('Cash'),
    ('Cheque'),
    ('Wire'),
    ('Subscription');

-- Création du tableau contenant les types d'entités pouvant transiger
CREATE TABLE IF NOT EXISTS Entity_Types(
    Type TEXT,
    "Nombre d'entités" INT NOT NULL
)
INSERT INTO Entity_Types (Type) VALUES
    ('Friend'),
    ('Employer'),
    ('Broker'),
    ('Merchant');