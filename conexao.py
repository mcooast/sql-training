import sqlite3

# Conectar ao banco de dados 'banco.db' (cria o arquivo se não existir)
conexao = sqlite3.connect('banco.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela 'usuarios'
# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# Criar a tabela 'gerentes'
# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# Criar a tabela 'produtos' para uso com DROP
# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

# Excluir a tabela 'produtos'
# cursor.execute('DROP TABLE produtos')

# Alterar o nome da tabela de 'usuarios' para 'usuario'
# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

# Incluir a coluna 'telefone'
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT(50)')

# Exemplo ficticio: Renomear a coluna 'telefoni' para 'telefone'
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# Inserir dados na tabela 'usuario'
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, "Jessica", "São Paulo", "jessica@gmail.com", 123456789)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, "Paula", "Campinas", "paula@gmail.com", 3245687189)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, "Cecilia", "Recife", "cecilia@gmail.com", 987456321)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (4, "Amanda", "Campina Grande", "amanda@gmail.com", 357169842)')

# Inserir dados na tabela 'gerentes'
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (4, "Amanda", "Campina Grande", "amanda@gmail.com")')
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (8, "Joana", "Rio de Janeiro", "joana@gmail.com")')
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (5, "Rita", "Salvador", "rita@gmail.com")')

# Deletar um registro da tabela 'usuario'
# cursor.execute('DELETE FROM usuario WHERE id=2')

# Atualizar um registro na tabela 'usuario'
# cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE nome = "Paula"')

# Ordenar e visualizar dados da tabela 'usuario' em ordem decrescente
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

# Limitar e visualizar dados distintos da tabela 'usuario'
# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2')

# WHERE é usado antes do GROUP BY, e HAVING depois do GROUP BY

# GROUP BY
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id > 3')

# INNER JOIN entre as tabelas 'usuario' e 'gerentes'
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# LEFT JOIN entre as tabelas 'usuario' e 'gerentes'
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')

# RIGHT JOIN entre as tabelas 'usuario' e 'gerentes'
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

# FULL JOIN entre as tabelas 'usuario' e 'gerentes'
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

# Sub-consulta na tabela 'usuario'
# dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')

# Ver dados retornados pela consulta
for usuario in dados:
    print(usuario)

# Confirmar as alterações no banco de dados
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()
