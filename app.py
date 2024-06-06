print("""𝖈𝖔𝖑𝖊𝖈̧𝖆̃𝖔 𝖉𝖊 𝖏𝖔𝖌𝖔𝖘""")

print('1. Cadastrar jogo')
print('2. Listar jogos')
print('3. Ativar jogo')
print('4. Sair \n')
 
opcao_escholhida = int(input('Escolha uma opção: '))

if opcao_escholhida == 1:
    print(f'Você escolheu  o cadastrar jogo {opcao_escholhida}')
elif opcao_escholhida == 2:
    print(f'Você escolheu o Listar jogos {opcao_escholhida}')
elif opcao_escholhida == 3:
    print(f'Você escolheu o ativar jogo {opcao_escholhida}')
else:
    print(f'Você escolheu sair {opcao_escholhida}')
