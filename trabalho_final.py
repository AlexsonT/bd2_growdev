# dando a opção de iniciar ou não o bd.
iniciar = ''
while iniciar != 'S':
    print('='*65)
    print('Gostaria de iniciar o Gerenciador de Banco de Dados?')
    iniciar = input("Digite 'S' para SIM ou 'N' para NÃO:").upper().strip()
    print('='*65)

# encerra o programa caso a opção seja "N".
    if iniciar == 'N':
        from funcoes_texto import texto_um
        texto_um()

# início do programa.
    if iniciar == 'S':
        print('Digite uma das seguintes opções:')
        criar_banco = input('[1]CRIAR BANCO\n[2]ENCERRAR O PROGRAMA\n')
        print('='*65)

        if criar_banco == '2':  # encerra o programa.
            from funcoes_texto import texto_um
            texto_um()
            break

        while criar_banco == '1':  # importa a função para criar um banco.
            from funcoes_texto import cria_banco
            cria_banco()
            print('='*65)
            criar_banco = input('[1]CRIAR BANCO\n[2]CRIAR COLEÇÃO\n')

        # criar coleção
        from funcoes_texto import cria_colecao
        cria_colecao()
        print('='*65)

        criar_nova_colecao = input(
            '[1]CRIAR COLEÇÃO\n[2]SAIR\n[3]INSERIR DOCUMENTOS\n')
        if criar_nova_colecao == '2':
            from funcoes_texto import texto_um
            texto_um()
            print('='*65)
            break

        while criar_nova_colecao == '1':
            from funcoes_texto import cria_colecao
            cria_colecao()
            print('='*65)
            criar_nova_colecao = input(
                '[1]CRIAR COLEÇÃO\n[2]SAIR\n[3]INSERIR DOCUMENTOS\n')

        # insere documentos
        from funcoes_texto import insere_docs
        insere_docs()
        print('='*65)

        inserir_documentos = input(
            '[1]BUSCAR DOCUMENTOS\n[2]SAIR\n[3]INSERIR DOCUMENTOS\n')

        if inserir_documentos == '2':
            from funcoes_texto import texto_um
            texto_um()
            print('='*65)
            break

        while inserir_documentos == '3':
            from funcoes_texto import insere_docs
            insere_docs()
            print('='*65)
            inserir_documentos = input(
                '[1]BUSCAR DOCUMENTOS\n[2]SAIR\n[3]INSERIR MAIS DOCUMENTOS\n')

        from funcoes_texto import buscar_docs
        buscar_docs()
        print('='*65)

        buscar_documentos = (
            input('[1]BUSCAR DOCS\n[2]SAIR\n[3]PRÓXIMO MENÚ\n'))

        while buscar_documentos == '1':
            from funcoes_texto import buscar_docs
            buscar_docs()
            print('='*65)
            buscar_documentos = (
                input('[1]BUSCAR DOCS\n[2]SAIR\n[3]PRÓXIMO MENÚ\n'))

        if buscar_documentos == '2':
            from funcoes_texto import texto_um
            texto_um()
            print('='*65)
            break

        if buscar_documentos == '3':
            from funcoes_texto import texto_opcoes
            texto_opcoes()
            print('='*65)
            opcoes = ['1', '2', '3', '4', '5', '6']
            print('O que deseja fazer?')
            menu = (input('Digite:'))

            while menu in opcoes:

                while menu == '1':
                    from funcoes_texto import buscar_docs
                    buscar_docs()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    print('='*65)
                    menu = input()

                while menu == '2':
                    from funcoes_texto import texto_um
                    texto_um()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    menu = input()

                while menu == '3':
                    from funcoes_texto import del_docs
                    del_docs()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    menu = input()

                while menu == '4':
                    from funcoes_texto import remover_colecoes
                    remover_colecoes()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    menu = input()

                while menu == '5':
                    from funcoes_texto import listar_bancos
                    listar_bancos()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    menu = input()

                while menu == '6':
                    from funcoes_texto import listar_colecoes_bd
                    listar_colecoes_bd()
                    print('='*65)
                    from funcoes_texto import texto_opcoes
                    texto_opcoes()
                    menu = input()
