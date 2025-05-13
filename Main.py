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
            dt = {'nome': [],'plano': []}
            comando = f'SELECT nome_cliente,plano FROM clientes'
            cursor.execute(comando)
            result = cursor.fetchall()
            
            for i in range(len(result)):
                dt['nome'].append(result[i][0])
                dt['plano'].append(result[i][1])
            
            df = pd.DataFrame(dt)
            print(df)
            



cursor.close()
connection.close()


# CREATE

# nome = "PEDRO PEREIRA"
# plano = "Tv + Internet"



# READ



# UPDADE
# DELETE
