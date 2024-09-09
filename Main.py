import sqlite3
import argparse
import os


# def execute_sql_script(function_filename):
#     try:
#         with open(function_filename, 'r') as f:
#             script = f.read()
#         conn = sqlite3.connect('pers_finance.db')
#         cursor = conn.cursor()
#         cursor.executescript(script)
#         conn.commit()
#         conn.close()
#         print(f"Script {function_filename} executed successfully.")
#     except Exception as e:
#         print(f"Error executing script {function_filename}: {str(e)}")
#


#-----CONSTRUCTION DE TOUS LES CHEMINS NÉCESSAIRES-----#
script_folder_path = os.path.join(os.getcwd(), "SQL_Commands")
Creation_script = os.path.join(script_folder_path, "Creation_personal_finance_table.sql")
AddTransaction_script = os.path.join(script_folder_path, "AddTransaction_script.sql")
#-----CONSTRUCTION DE TOUS LES CHEMINS NÉCESSAIRES-----#



#-----FUNCTIONS HERE-----#

# Example Function
# def create_tables():
#     execute_sql_script('create_tables.sql')

def CreationBaseDonnees():
    try:
        with open(Creation_script, "r") as f:
            script = f.read()
        conn = sqlite3.connect('pers_finance.db')
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def AddTransaction():
    # Initialising my variables
    Amount = None
    Origin = None
    Origin_Type = None
    Destination = None
    Destination_Type = None
    Category = None
    Sub_Category = None
    Recurrence = None

    # Creating my list
    row = ()

    print("""
    Please input your transaction data in following format :
        Amount (integer, + or -)
        Origin (Where did your money come)
        Origin_Type (Friend, Employer, Bank, Broker, Merchant)
        Destination (Where is your money going)
        Destination_Type (Friend, Employer, Bank, Broker, Merchant)
        Category (Spending, Revenue, Deposit, Withdrawal)
        Sub_Category (Will depend on Category)
        Recurence (If recurrence is applicable, number of days between each transaction. Else, leave blank)
        
    To exit at any time, type exit
    """)

    # Vérification de chaque élément de ma future rangée
    while True:
        try:
            Amount = input("Amount : ")
            if Amount.lower() == 'exit':
                print("Exiting")
                break
            isinstance(Amount, int)
            row += row + (Amount,)
        except ValueError:
            print(f"{Amount} n'est pas un format acceptable")

        try:
            Origin = input("Origin : ")
            if Origin.lower() == 'exit':
                print("Exiting")
                break
            isinstance(Origin, str)
            row += row + (Origin,)
        except ValueError:
            print(f"{Origin} n'est pas un format acceptable")

        try:
            Origin_Type = str(input("Origin : "))
            if Origin_Type in ["Friend", "Employer", "Bank", "Broker", "Merchant"]:
                row += row + (Origin_Type,)
                continue
            if Origin_Type.lower() == 'exit':
                print("Exiting")
                break
        except ValueError:
            print(f"{Origin_Type} n'est pas un format acceptable")

        try:
            Destination = input("Destination : ")
            if Destination.lower() == 'exit':
                print("Exiting")
                break
            isinstance(Destination, str)
            row += row + (Destination,)
        except ValueError:
            print(f"{Destination} n'est pas un format acceptable")

        try:
            Destination_Type = str(input("Destination_Type : "))
            if Destination_Type in ["Friend", "Employer", "Bank", "Broker", "Merchant"]:
                row += row + (Destination_Type,)
                continue
            if Destination_Type.lower() == 'exit':
                print("Exiting")
                break
        except ValueError:
            print(f"{Destination_Type} n'est pas un format acceptable")

        try:
            Category = str(input("Destination_Type : "))
            if Category in ["Spending", "Revenue", "Deposit", "Withdrawal"]:
                row += row + (Category,)
                continue
            if Category.lower() == 'exit':
                print("Exiting")
                break
        except ValueError:
            print(f"{Category} n'est pas un format acceptable")

        # -------Conditions liées à Sub-Category-------
        try:
            if Category == "Spending":
                Sub_Category = input("Sub_Category (Nutrition, Clothing, Housing, Transport, Investment, Distraction): ")
                if Sub_Category in ["Nutrition", "Clothing", "Housing", "Transport", "Investment", "Distraction"]:
                    row += row + (Sub_Category,)
                    continue
                if Sub_Category.lower() == 'exit':
                    print("Exiting")
                    break
        except ValueError:
            print(f"{Sub_Category} n'est pas un format acceptable")

        try:
            if Category == "Revenue":
                Sub_Category = input("Sub_Category (Salary, Dividend, Capital Gain): ")
                if Sub_Category in ["Salary", "Dividend", "Capital Gain"]:
                    row += row + (Sub_Category,)
                    continue
                if Sub_Category.lower() == 'exit':
                    print("Exiting")
                    break
        except ValueError:
            print(f"{Sub_Category} n'est pas un format acceptable")

        try:
            if Category == "Deposit":
                Sub_Category = input("Sub_Category (Cash, Cheque, Wire): ")
                if Sub_Category in ["Cash", "Cheque", "Wire"]:
                    row += row + (Sub_Category,)
                    continue
                if Sub_Category.lower() == 'exit':
                    print("Exiting")
                    break
        except ValueError:
            print(f"{Sub_Category} n'est pas un format acceptable")

        try:
            if Category == "Withdrawal":
                Sub_Category = input("Sub_Category (Cash, Cheque, Wire): ")
                if Sub_Category in ["Cash", "Cheque", "Wire"]:
                    row += row + (Sub_Category,)
                    continue
                if Sub_Category.lower() == 'exit':
                    print("Exiting")
                    break
        except ValueError:
            print(f"{Sub_Category} n'est pas un format acceptable")
        # -------Conditions liées à Sub-Category-------

        try:
            Recurrence = input("Recurrence : ")
            if not Recurrence:
                row += row + (Recurrence,)
                continue
            else:
                if Recurrence.lower() == "exit":
                    print("Exiting")
                    break
            isinstance(Recurrence, int)
            row += row + (Recurrence,)
        except ValueError:
            print(f"{Recurrence} n'est pas un format acceptable")

    # Commande SQL
    try:
        with open(AddTransaction_script, "r") as f:
            script = f.read()
        conn = sqlite3.connect('pers_finance.db')
        cursor = conn.cursor()
        cursor.executescript(script)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        if 'conn' in locals():
            conn.close()


#-----FUNCTIONS HERE-----#



#-----ARGPARSE-----#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute SQL scripts')
    subparsers = parser.add_subparsers(dest='command')


    # -----COMMANDS-----#
# Example Command being created (Related to Example Function)
#     create_tables_parser = subparsers.add_parser('create_tables', help='Create tables')
#     create_tables_parser.set_defaults(func=create_tables)

    create_db_parser = subparsers.add_parser('CreationDB', help="Création de la base de données principale")
    create_db_parser.set_defaults(func=CreationBaseDonnees)

    # -----COMMANDS-----#


    args = parser.parse_args()
    if args.command:
        args.func()
    else:
        parser.print_help()
#-----ARGPARSE-----#