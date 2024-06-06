def opcao_invalida():
    print('opçao invalida')
    input('digite uma tecla para reiniciar')
    finalizar()

def finalizar():
    i = 1
    jogo_cadastrado = []

    print("""𝖈𝖔𝖑𝖊𝖈̧𝖆̃𝖔 𝖉𝖊 𝖏𝖔𝖌𝖔𝖘""")



    while i < 1000: 

        print('1. Cadastrar jogo')
        print('2. Lista de jogos cadastrados')
        print('3. Ativar jogo')
        print('4. Sair \n') 

        opcao_escholhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escholhida}')

        if opcao_escholhida == 1:
            jogo_cadastrado.append(input('qual jogo voce dejeja cadastrar: '))
            print('cadastro realizado com sucesso')
            continua = int(input('dejeja cadastrar outros jogos(se sim digite 1 se nao digite 2)'))
            if continua == 1:
                j = 1
                while j < 1000 :
                    jogo_cadastrado.append(input('qual jogo voce dejeja cadastrar: '))    
                    cont = int(input('dejeja continuar a cadastrar outros jogos(se sim digite 1 se nao digite 2)'))
                    if cont == 1 :
                        jogo_cadastrado.append(input('qual jogo voce dejeja cadastrar: '))
                        print('cadastro realizado com sucesso')
                    elif cont == 2 :
                        break
        elif opcao_escholhida == 2:
            print(jogo_cadastrado)
        elif opcao_escholhida == 3 :
            jogo_ativo = input('qual jogo quer ativar: ')
            print(f'jogo {jogo_ativo} esta sendo ativado')
        elif opcao_escholhida == 4 : 
            saida_certeza = int(input('você tem certeza que quer sair,se sim digite 1 se não digite 2 : '))
            if saida_certeza == 1:
                print('tchau')
                break
            else:
                print('boa decisão') 
        else :
            opcao_invalida()
if __name__ == '__main__':
    finalizar()

