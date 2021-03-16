import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} nossa história começa nos primórdios de 2018 com lines de Rainbow 6. Para não ter uma resposta muito longa, o ademiro recomenda que você acesse essa matéria onde contamos mais sobre nós! ;) LINK.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Atualmente contamos com duas lines (incompletas até então): CS:GO e Free Fire.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}Agradecemos o seu interesse, {nome}! As vagas disponíveis no momento são: vaga1, vaga2, vaga3, ..., vagaN.{os.linesep}')
    else:
        print(f'Opa, pera ai! Digite apenas 1, 2 ou 3.{os.linesep}')


def start():
    # Apresentar o chatbot
    print('Olá, seja bem vindo(a) ao bot de relações do LoG Ceará Club! Bot para automação de chat feio por @log_murilohyper')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu melhor número (Não se preocupe! Essa informação é sigilosa e será somente usada para o um retorno mais rápido! ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Qual a história do LoG?{os.linesep}[2] - Vocês possuem quais lines ativas no momento?{os.linesep}[3] - Quais são as vagas disponíveis?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)



if __name__ == '__main__':
    start()
