import sqlite3
import random

conexao = sqlite3.connect('Banco_Dados')

cursor = conexao.cursor()
'''
#CRIANDO TABELA
cursor.execute(
    'CREATE TABLE MINHA_TABELA (Data Text, Nome text, Idade real ) '
)
'''
#FAZEER COMMIT so quando cria uma tabela para ela ser criada
conexao.commit()

#Inserindo Valores

cursor.execute('insert into MINHA_TABELA values ("17/02/1997", "Pedro Vinicius", "26")')

for i in range(0,10):
    numero = random.randint(1,100)

    cursor.execute(f'insert into MINHA_TABELA values ("15/02/1988", "Pedro Vinicius", {numero})')

#CONSULTA  QUERY

consulta = cursor.execute('SELECT Nome, Idade FROM MINHA_TABELA').fetchall()

print(consulta)
