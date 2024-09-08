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