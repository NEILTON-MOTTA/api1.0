from psycopg2 import pool

# Cria o pool de conexões (mínimo 1, máximo 10)
connection_pool = pool.SimpleConnectionPool(
    1, 10,
    host="127.0.0.1",
    database="dynacomp",
    user="postgres",
    password="1234"
)

# Pega uma conexão do pool
def get_conexao():
    return connection_pool.getconn()

# Devolve a conexão para o pool
def release_conexao(conn):
    connection_pool.putconn(conn)
