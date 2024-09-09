
-- Création du tableau contenant mes catégories de transactions

CREATE TABLE IF NOT EXISTS Transactions_Types(
    Type TEXT,
    Number_of_transactions INTEGER DEFAULT 0,
    Total_amount FLOAT DEFAULT 0.0
);

INSERT INTO Transactions_Types (Type) VALUES
    ('Spending'),
    ('Revenue'),
    ('Deposit'),
    ('Withdrawal');

SELECT
    Type,
    COALESCE(Number_of_transactions, 0) AS Number_of_transactions,
    COALESCE(Total_amount, 0) AS Total_amount
FROM Transactions_Types;
-------------------------

-- Création des tableaux contenant les sous-catégories
CREATE TABLE IF NOT EXISTS Spending_Types(
    Type TEXT,
    Number_of_transactions INTEGER DEFAULT 0,
    Total_amount FLOAT DEFAULT 0.0
);

INSERT INTO Spending_Types (Type) VALUES
    ('Nutrition'),
    ('Clothing'),
    ('Housing'),
    ('Transport'),
    ('Investment'),
    ('Distraction');

SELECT
    Type,
    COALESCE(Number_of_transactions, 0) AS Number_of_transactions,
    COALESCE(Total_amount, 0) AS Total_amount
FROM Spending_Types;
-------------------------
CREATE TABLE IF NOT EXISTS Revenue_Types(
    Type TEXT,
    Number_of_transactions INTEGER DEFAULT 0,
    Total_amount FLOAT DEFAULT 0.0
);

INSERT INTO Revenue_Types (Type) VALUES
    ('Salary'),
    ('Dividend'),
    ('Capital Gain');

SELECT
    Type,
    COALESCE(Number_of_transactions, 0) AS Number_of_transactions,
    COALESCE(Total_amount, 0) AS Total_amount
FROM Revenue_Types;
-------------------------
CREATE TABLE IF NOT EXISTS Deposit_Types(
    Type TEXT,
    Number_of_transactions INTEGER DEFAULT 0,
    Total_amount FLOAT DEFAULT 0.0
);

INSERT INTO Deposit_Types (Type) VALUES
    ('Cash'),
    ('Cheque'),
    ('Wire');

SELECT
    Type,
    COALESCE(Number_of_transactions, 0) AS Number_of_transactions,
    COALESCE(Total_amount, 0) AS Total_amount
FROM Deposit_Types;
-------------------------
CREATE TABLE IF NOT EXISTS Withdrawal_Types(
    Type TEXT,
    Number_of_transactions INTEGER DEFAULT 0,
    Total_amount FLOAT DEFAULT 0.0
);

INSERT INTO Withdrawal_Types (Type) VALUES
    ('Cash'),
    ('Cheque'),
    ('Wire'),
    ('Subscription');

SELECT
    Type,
    COALESCE(Number_of_transactions, 0) AS Number_of_transactions,
    COALESCE(Total_amount, 0) AS Total_amount
FROM Withdrawal_Types;
-------------------------

-- Création du tableau contenant les types d'entités pouvant transiger
CREATE TABLE IF NOT EXISTS Entity_Types(
    Type TEXT,
    "Nombre_d'entités" INTEGER DEFAULT 0
);

INSERT INTO Entity_Types (Type) VALUES
    ('Friend'),
    ('Employer'),
    ('Bank'),
    ('Broker'),
    ('Merchant');

SELECT
    Type,
    COALESCE("Nombre_d'entités", 0) AS "Nombre_d'entités"
FROM Entity_Types;
-------------------------

-- NOTE I won't be writing in these tables, I will only write in the Transactions table
-- Création des tableaux contenant les transactions de tous les types créés précédement
CREATE TABLE IF NOT EXISTS Spending(
    ID INT NOT NULL,
    Amount FLOAT,
    Origin TEXT,
    Destination TEXT,
    "Date" DATE,
    Sub_Category TEXT,
    "Recurrence(days)" INT,
    Funds FLOAT,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);

CREATE TABLE IF NOT EXISTS Revenue(
    ID INT NOT NULL,
    Amount FLOAT,
    Origin TEXT,
    Destination TEXT,
    "Date" DATE,
    Sub_Category TEXT,
    "Recurrence(days)" INT,
    Funds FLOAT,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);

CREATE TABLE IF NOT EXISTS Deposit(
    ID INT NOT NULL,
    Amount FLOAT,
    Origin TEXT,
    Destination TEXT,
    "Date" DATE,
    Sub_Category TEXT,
    "Recurrence(days)" INT,
    Funds FLOAT,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);

CREATE TABLE IF NOT EXISTS Withdrawal(
    ID INT NOT NULL,
    Amount FLOAT,
    Origin TEXT,
    Destination TEXT,
    "Date" DATE,
    Sub_Category TEXT,
    "Recurrence(days)" INT,
    Funds FLOAT,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);
-------------------------

-- THIS IS THE TABLE I WRITE IN, AND EACH TRANSACTION WILL BE DUPLICATED IN THE APPROPRIATE TABLE
-- Création du tableau contenant l'ensemble des transactions
CREATE TABLE IF NOT EXISTS Transactions(
    ID INT NOT NULL,
    Amount FLOAT,
    Origin TEXT,
    Destination TEXT,
    "Date" DATE, -- SQLite has a built-in function called DATETIME, dates are treated as strings
    Category TEXT,
    Sub_Category TEXT,
    "Recurrence(days)" INT, -- IF NULL no recurrence
    Funds FLOAT,
    PRIMARY KEY (ID),
    UNIQUE (ID)
);

-------------------------
-- DON'T THINK I WILL NEED THIS

-- Create a table to store the next available ID
--CREATE TABLE IF NOT EXISTS IdGenerator (
--    TableName TEXT PRIMARY KEY,
--    NextId INTEGER
--);
--
---- NEED TO INITIALIZE FOR ALL TABLES WHICH CONTAIN ID
---- Initialize the next available ID for each table
--INSERT INTO IdGenerator (TableName, NextId) VALUES ('Spending', 1);
---- INSERT INTO IdGenerator (TableName, NextId) VALUES ('OtherTable', 1);
--
---------------------------
---- WILL NEED TO FIGURE OUT HOW TO CALL IT IN MY SQL CODE
---- Create a function to assign the next available ID to a table
--CREATE FUNCTION IF NOT EXISTS GetNextId(TableName TEXT)
--RETURNS INTEGER
--BEGIN
--    UPDATE IdGenerator SET NextId = NextId + 1 WHERE TableName = TableName;
--    RETURN (SELECT NextId - 1 FROM IdGenerator WHERE TableName = TableName);
--END;

-- WILL ALSO NEED TO CREATE TRIGGERS TO UPDATE THE IDs










