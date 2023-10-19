import psycopg2

postgres = psycopg2.connect(database = "postgres", host = "localhost", user="postgres", password="1234", port="5432")
runner = postgres.cursor()

execsql = lambda comando, conexao: conexao.execute(comando)

execusedb = lambda base, conexao: execsql("USE DATABASE " + base + ";\n", conexao)
execcreatedb = lambda base, conexao: execsql("CREATE DATABASE IF NOT EXISTS " + base + ";\n", conexao)
execdropdb = lambda base, conexao: execsql("DROP DATABASE I EXISTS " + base + ";\n", conexao) 
execcreatetable = lambda tabela, atributos, conexao: execsql("CREATE TABLE IF NOT EXISTS " + tabela + "(" + atributos + ");\n", conexao)
execdroptable = lambda base, conexao: execsql("DROP TABLE IF EXISTS " + base + ";\n", conexao)
execselect = lambda tabela, atributos, conexao: execsql("SELECT " + atributos + " FROM " + tabela + ";\n", conexao)
execselectwhere = lambda tabela, atributos, condicao, conexao: execsql("SELECT " + atributos + " FROM " + tabela + " WHERE " + condicao + ";\n", conexao)
execinsert = lambda tabela, atributos, valores, conexao: execsql("INSERT INTO " + tabela + "(" + atributos + ")" + " VALUES (" + valores + ");\n", conexao)


execcreatetable(" usuarios ", "id int, nome varchar(100), console varchar(50)", runner)
execcreatetable(" jogos ", "id int, nome varchar(100), data_lancamento varchar(50)", runner)
execinsert("usuarios", "id, nome, console", "'1', 'Augusto', 'PS5'", runner)
execinsert("jogos", "id, nome, data_lancamento", "'1', 'GTA 6', '11-05-2025'", runner)
execselect("usuarios", "*", runner)
execselect("jogos", "*", runner)

resultados = runner.fetchall()
printar_resultados = lambda resultados: [print (resultado) for resultado in resultados]

printar_resultados(resultados)