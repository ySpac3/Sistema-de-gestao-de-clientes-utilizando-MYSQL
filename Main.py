import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)

cursor = connection.cursor()
while True:
    choice = int(input("Oq deseja fazer cadastrar-1, verificar-2"))

    match choice:
        case 1:
            name = input("Digite o nome do usuario >> ")
            plano = input("Digite o plano do usuario >> ")
            
            comando = f'INSERT INTO clientes (nome_cliente, plano) VALUES ("{name}","{plano}")'
            cursor.execute(comando)
            connection.commit()
        case 2:
            df = pd.read_sql(f"Select * FROM clientes", connection)
            print(df)
            



cursor.close()
connection.close()


# CREATE

# nome = "PEDRO PEREIRA"
# plano = "Tv + Internet"



# READ



# UPDADE
# DELETE
