from psycopg2 import pool

# Cria o pool de conexões (mínimo 1, máximo 10)
connection_pool = pool.SimpleConnectionPool(
    1, 10,
    host="187.84.150.143",
    database="dynacomp",
    user="postgres",
    password="DYNACOMP@MATEUS25#35_00351241728_gs1250",
    port=3597
)

# Pega uma conexão do pool
def get_conexao():
    return connection_pool.getconn()

# Devolve a conexão para o pool
def release_conexao(conn):
    connection_pool.putconn(conn)
