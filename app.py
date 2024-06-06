print("""𝖈𝖔𝖑𝖊𝖈̧𝖆̃𝖔 𝖉𝖊 𝖏𝖔𝖌𝖔𝖘""")

jogo_cadastrado = []
i = 1
while i < 1000: 

    print('1. Cadastrar jogo')
    print('2. Lista de jogos cadastrados')
    print('3. Ativar jogo')
    print('4. Sair \n') 

    opcao_escholhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção: {opcao_escholhida}')

    if opcao_escholhida == 1:
        jogo_cadastrado.append(input('qual jogo voce dejeja cadastrar: '))
        print(f'voce cadastrou o jogo {jogo_cadastrado}')
    elif opcao_escholhida == 2:
        print(jogo_cadastrado)
    elif opcao_escholhida == 3 :
        jogo_ativo = input('qual jogo quer ativar: ')
        print(f'jogo {jogo_ativo} esta sendo ativado')
    else : 
        saida_certeza = int(input('você tem certeza que quer sair,se sim digite 1 se não digite 2 : '))
        if saida_certeza == 1:
            print('boa escholha')
            break
        else:
            print('boa decisão')






