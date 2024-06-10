import os 
alunos=[]
def media_nota():
    nota1 = int(input('entre com a nota 1: '))
    nota2 = int(input('entre com a nota 2: '))
    nota3 = int(input('entre com a nota 3: '))
    nota_media = (nota1+nota2+nota3)/3
    return nota_media
    
def inserir_nota():
    nome_aluno_nota = input('qual o nome do aluno que quer muda a nota: ')
    for aluno in alunos :
        aluno_nome = aluno['nome']
        if aluno_nome == nome_aluno_nota :
            aluno['nota'] = media_nota()
        


def exibir_cadrastro():
    for aluno in alunos:
        nome_aluno = aluno['nome']
        idade_aluno = aluno['idade']
        nota_aluno = aluno['nota']
        print(f'-----------------aluno------------------ \n-nome:{nome_aluno}  \n-idade:{idade_aluno}  \n-nota:{nota_aluno}')
        
def cadrastro_aluno() :
    os.system('cls')
    print('cadastro aluno')
    nome_aluno = input('insira o nome do aluno: ')
    idade_aluno = input('isnsira a idade do aluno: ')
    dados_do_aluno = {'nome':nome_aluno, 'idade':idade_aluno , 'nota':'-'}
    alunos.append(dados_do_aluno)

def main():
    i=0
    while i<1000:
        cadrastro_denovo = (input('quer cadratrar outro aluno(s/n)'))
        if cadrastro_denovo == 's':
            cadrastro_inserir = int(input('você que inserir a nota do aluno(1) ou cadrastrar um novo aluno(2): '))
            if  cadrastro_inserir == 1:
                inserir_nota()
            elif cadrastro_inserir == 2:
                cadrastro_aluno()
        elif cadrastro_denovo == 'n':
            exibir_cadrastro()
            break

if __name__ == '__main__':
    main()
