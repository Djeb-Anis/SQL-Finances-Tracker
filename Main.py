import sqlite3
import argparse
# Will probably need to import sys or something else for the correct file paths

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

#-----CRÉATION BASE DE DONNÉES AVEC MES TABLES-----#
conn = sqlite3.connect('pers_finance.db')
cursor = conn.cursor()
cursor.execute()

#-----CRÉATION BASE DE DONNÉES AVEC MES TABLES-----#



#-----FUNCTIONS HERE-----#

# Example Function
# def create_tables():
#     execute_sql_script('create_tables.sql')

def AddTransaction():
    cursor.execute('SELECT Category FROM pers_finance.Transactions ')
    categorie = str(input("Quel Catégorie de transaction souhaitez-vous ajouter?"))





#-----FUNCTIONS HERE-----#



#-----ARGPARSE-----#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute SQL scripts')
    subparsers = parser.add_subparsers(dest='command')

    # -----COMMANDS-----#
# Example Command being created (Related to Example Functino)
#     create_tables_parser = subparsers.add_parser('create_tables', help='Create tables')
#     create_tables_parser.set_defaults(func=create_tables)

    # -----COMMANDS-----#

    args = parser.parse_args()
    if args.command:
        args.func()
    else:
        parser.print_help()
#-----ARGPARSE-----#