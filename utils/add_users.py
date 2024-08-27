import sqlite3
import hashlib


# Função para hashear a senha com SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect('databases/db_producao.db')
cursor = conn.cursor()

# Adicionar um usuário de exemplo com senha criptografada
username = 'mariana'
password = 'mariana'
hashed_password = hash_password(password)

# Inserir usuário no banco de dados
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

