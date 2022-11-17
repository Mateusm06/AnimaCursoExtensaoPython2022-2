# Importando a biblioteca sqlite3
import sqlite3 
# Estabelecendo uma conexão com o banco de dados
conexao = sqlite3.connect('dc_universe.db')
# Criar um objeto do tipo cursor
cursor = conexao.cursor()
# Comando sql do banco
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"
# Executa o comando sql    
cursor.execute(sql)
# Confirma o insert e fecha o banco de dados
conexao.commit()
conexao.close()
