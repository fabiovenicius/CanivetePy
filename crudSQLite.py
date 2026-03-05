import sqlite3


def conectarBaseDados(database):
    con = sqlite3.connect(database)
    return con


def acessarDados(database):
    con = conectarBaseDados(database)
    cur = con.cursor()
    return cur


def salvar(database):
    con = conectarBaseDados(database)
    con.commit()
    con.close()


def criarTabela(database, tabela, *campos):
    cur = acessarDados(database)
    if len(campos) == 1:
        somente1campo = campos[0]
        try:
            cur.execute(f"""CREATE TABLE {tabela}({somente1campo})""")
            print(f"Tabela {tabela} criada com sucesso!")
            salvar(database)
            return True
        except sqlite3.OperationalError:
            raise Exception("Tabela já existe!")
    else:
        try:
            cur.execute(f"""CREATE TABLE {tabela}{campos}""")
            print(f"Tabela {tabela} criada com sucesso!")
            salvar(database)
            return True
        except sqlite3.OperationalError:
            raise Exception("Tabela já existe!")


def pegarDados(database, tabela):
    cur = acessarDados(database)
    cur.execute(f"select * from {tabela}")
    return cur.fetchall()


def pegarDadosSelecionados(database, tabela, selecao, valor):
    cur = acessarDados(database)
    try:
        cur.execute(f'select * from {tabela} where "{selecao}" = {valor}')
    except sqlite3.OperationalError:
        cur.execute(f'select * from {tabela} where "{selecao}" = "{valor}"')
    return cur.fetchall()


def atualizarDados(
    database, tabela, campoAjustado, valorAjuste, campoReferencia, valorReferencia
):
    con = conectarBaseDados(database)
    cur = con.cursor()
    try:
        cur.execute(
            f'''UPDATE {tabela} 
        SET {campoAjustado} = {valorAjuste} 
        WHERE {campoReferencia} = "{valorReferencia}"'''
        )
        print("Registro alterado com sucesso!")
        con.commit()
        con.close()
        return True
    except sqlite3.OperationalError:
        raise Exception("Erro na instrução SQL!")


def inserirValores(database, tabela, *valores):
    con = conectarBaseDados(database)
    cur = con.cursor()
    try:
        cur.execute(f"""INSERT INTO {tabela} VALUES{valores}""")
        print("Registro inserido com sucesso!")
        con.commit()
        con.close()
        return True
    except sqlite3.OperationalError:
        raise Exception(f"Erro na instrução SQL!")


def deletarTabela(database, tabela):
    cur = acessarDados(database)
    try:
        cur.execute(f"""DROP TABLE {tabela}""")
        return True
    except sqlite3.OperationalError:
        raise Exception("Tabela Não Encontada!")
    salvar(database)


def deletarValores(database, tabela, campo, condicao):
    con = conectarBaseDados(database)
    cur = con.cursor()
    try:
        cur.execute(f"""DELETE FROM {tabela} where {campo} = {condicao}""")
        print("Registro deletado com sucesso!")
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        cur.execute(f'''DELETE FROM {tabela} where {campo} = "{condicao}"''')
        con.commit()
        con.close()
    else:
        print("Erro na Execução do SQL!")


# deletarTabela('Receitas')
# criarTabela()
# criarTabela('TiposDespesa2', 'Nome')
# inserirValores('Receitas','Saldo BB', 7500)
# inserirValores('Receitas','Salário', 6670.15)
# inserirValores('Receitas','Saldo BB', 12084.34)
# atualizarDados('Receitas', 'Valor', 7533.35,'Nome', 'Saldo BB')
# receitas = pegarDados('Receitas')
# print(receitas)
# print(pegarDadosSelecionados('Receitas', 'Valor', 7533.35))
# deletarValores('Receitas', 'Nome', 'Saldo BB')
# print(pegarDados('Receitas'))
