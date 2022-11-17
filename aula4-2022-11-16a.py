# Importando a biblioteca sqlite3
import sqlite3
# Estabelecendo uma conexão com o banco de dados
conexao = sqlite3.connect('dc_universe.db') 
# Criar um objeto do tipo cursor
cursor = conexao.cursor()
# Comando sql do banco
sql = 'SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas'
cursor.execute(sql)
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)