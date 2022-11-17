import aula4_2022_11_16c as bd
con, cur = bd.conectar()
nome = input("Informe o nome do personagem: ")
nome_civil = input("Informe o nome real do personagem: ")
tipo_numerico = int(input("Digite 1 para Herói(na) e 2 para Vilã(o): "))
#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]
if tipo_numerico == 1:
  tipo = "Herói(na)"
elif tipo_numerico == 2:
  tipo = "Vilã(o)"
sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"
cur.execute(sql)
con.commit()
con.close()
