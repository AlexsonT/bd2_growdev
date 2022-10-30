import pprint

import pymongo

# conexao = pymongo.MongoClient('mongodb://localhost:27017/')


def cria_banco():  # função para criar banco.
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    nome_banco = input(
        'Insira o nome do banco que deseja criar:')
    conexao[nome_banco]
    print('Banco criado com sucesso!')
    print('Obs: O banco aparecerá na lista após inserir documentos no mesmo.')
    print('='*65)


# cria colecao em banco determinado
def cria_colecao():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    # print('Bancos já criados')
    # databases = conexao.list_database_names()
    # print(databases)
    banco = (input('Em qual banco deseja criar a coleção(digite o nome):'))
    db = conexao[banco]
    colecao = input('Insira o nome da coleção que deseja criar:')
    db[colecao]


def lista_colecoes():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    print('Bancos já criados')
    databases = conexao.list_database_names()
    print(databases)
    banco = (input('De qual banco deseja listar as coleções(digite o nome):'))
    db = conexao[banco]
    show = db.list_collection_names()
    print(show)


def insere_docs():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    banco = (input('Em qual banco deseja inserir documentos? (digite):'))
    db = conexao[banco]
    colecao = (
        input('Em qual coleção deseja inserir documentos? (digite):'))
    db[colecao]
    chave = input('chave:')
    valor = input('valor:')
    colecao_criada = {chave: valor}
    db.colecao.insert_one(colecao_criada)


# função para "printar" texto de finalização.


def texto_um():
    print('='*65)
    print('Obrigado por usar o gerador de Bando de Dados com Mongo DB.')
    print('>>> O programa foi finalizado com sucesso! <<<')
    print('='*65)


def texto_opcoes():
    pprint.pprint(['[1] BUSCAR MAIS DOCUMENTOS',
                   '[2] SAIR',
                   '[3] DELETAR DOCUMENTOS',
                   '[4] REMOVER COLEÇÕES',
                   '[5] LISTAR BANCOS',
                   '[6] LISTAR COLEÇÕES DE UM BANCO'])


def buscar_docs():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    banco = (input('De qual banco deseja buscar documentos? (digite o nome):'))
    db = conexao[banco]

    colecao = (
        input('De qual coleção deseja buscar documentos? (digite o nome):'))
    db[colecao]

    print('Buscar um ou todos os documentos da coleção?')
    quantidade_docs = (input('[1]APENAS UM\n[2]TODOS\n'))

    if quantidade_docs == '1':
        print('Digite a chave e valor do documento que deseja buscar:')
        chave = (input('Digite a chave:'))
        valor = (input('Digite o valor:'))
        busca_colecao = db.colecao.find_one({chave: valor})
        pprint.pprint(busca_colecao)

    if quantidade_docs == '2':
        busca_colecao = db.colecao.find({})
        for i in busca_colecao:
            pprint.pprint(i)


def del_docs():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    print('Bancos já criados')
    databases = conexao.list_database_names()
    print(databases)
    banco = (input('De qual banco deseja deletar documentos? (digite o nome)'))
    db = conexao[banco]
    colecao = db.list_collection_names()
    print(colecao)
    colecao = (
        input('De qual coleção deseja deletar documentos? (digite o nome):'))
    db[colecao]
    print('Digite a chave e valor do documento que deseja deletar:')
    chave = (input('Digite a chave:'))
    valor = (input('Digite o valor:'))
    db.colecao.remove({chave: valor})


def remover_colecoes():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    print('Bancos já criados')
    databases = conexao.list_database_names()
    print(databases)
    banco = (input('De qual banco deseja listar as coleções?'))
    db = conexao[banco]
    print('Deseja remover todas as coleções deste banco?')
    drop_collections = (input('[S] SIM \n[N] NÃO\n')).upper().strip()
    if drop_collections == 'S':
        db.collection_drop()


def listar_bancos():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    print('Bancos criados!')
    databases = conexao.list_database_names()
    print(databases)


def listar_colecoes_bd():
    conexao = pymongo.MongoClient('mongodb://localhost:27017/')
    print('Bancos já criados')
    databases = conexao.list_database_names()
    print(databases)
    banco = (input('De qual banco deseja listar as coleções?'))
    db = conexao[banco]
    colecao = db.list_collection_names()
    print(colecao)
