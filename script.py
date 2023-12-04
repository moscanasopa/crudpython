import mysql.connector
import unidecode

def criar():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pythonmysql'
    )

    cursor = conexao.cursor()

    try:
        id_produto = input('Insira o ID do produto (inteiro): ')
        nome_produto = input('Insira o nome do produto: ')
        valor_produto = input('Insira o valor do produto (inteiro): ')

        nome_produto_ar = unidecode.unidecode(nome_produto)

        comando = 'INSERT INTO vendas (id_produto, nome_produto, valor_produto) VALUES ("{}", "{}" , "{}")'.format(id_produto, nome_produto_ar.upper(), valor_produto)
        cursor.execute(comando)  # Executa o comando
        conexao.commit()  # Edita o banco de dados

        cursor.close()
        conexao.close()

        print('Produto "{}" cadastrado com sucesso!'.format(nome_produto_ar.upper()))
    except:
        print('Ocorreu um erro ao cadastrar o produto!')


def ler():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pythonmysql'
    )
        
    cursor = conexao.cursor()

    comando = 'SELECT id_produto, nome_produto, valor_produto FROM vendas'
    cursor.execute(comando)
    
    for (id_produto, nome_produto, valor_produto) in cursor:
        print('ID: "{}" / Produto: "{}" / Valor: "{}"'.format(id_produto, nome_produto.upper(), valor_produto))

    cursor.close()
    conexao.close()


def alterar():

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pythonmysql'
    )
            
    cursor = conexao.cursor()

    alterar_produto = input('Digite o ID do produto que voce deseja editar o valor: ')
    produto_selecionado = 'SELECT nome_produto FROM vendas WHERE id_produto = {}'.format(alterar_produto)
    alterar_valor = input('Digite o novo valor do produto: ')

    cursor.execute(produto_selecionado)

    try:
        for (nome_produto) in cursor:
            nome = nome_produto
            confirmar = input('Voce realmente deseja alterar o valor do produto: "{}" para "{}"? (S/N)'.format(nome[0].upper(), alterar_valor))

        if confirmar.upper() == 'S':
            comando = 'UPDATE vendas SET valor_produto = {} WHERE id_produto = "{}"'.format(alterar_valor, alterar_produto.upper())

            cursor.execute(comando)
            conexao.commit()

            print('Valor de "{}" alterado para "{}", com sucesso!'.format(nome[0], alterar_valor))
        else:
            print('Valor do produto "{}" nao alterado!'.format(nome[0].upper()))
    except:
        print('Produto nao encontrado!')

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()


def deletar():

    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pythonmysql'
    )

    cursor = conexao.cursor()

    deletar_produto = input('Digite o ID do produto que voce deseja deletar: ')
    produto_selecionado = 'SELECT nome_produto FROM vendas WHERE id_produto = {}'.format(deletar_produto)

    cursor.execute(produto_selecionado)

    try:
        for (nome_produto) in cursor:
            nome = nome_produto
            confirmar = input('Voce realmente deseja deletar o produto: "{}" ? (S/N)'.format(nome[0].upper()))

        if confirmar.upper() == 'S':
            comando = 'DELETE FROM vendas WHERE id_produto = "{}"'.format(deletar_produto, deletar_produto)

            cursor.execute(comando)
            conexao.commit()

            print('Produto "{}" deletado com sucesso!'.format(nome[0].upper()))
        else:
            print('Produto "{}" nao deletado!'.format(nome[0].upper()))
    except:
        print('Produto nao encontrado!')

    cursor.close()
    conexao.close()
