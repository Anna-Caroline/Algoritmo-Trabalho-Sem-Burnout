print('-='*67)
print('''\033[30;42mA infelicidade no trabalho pode causar uma série de consequências, o objetivo deste algoritmo é servir de alerta tanto para o empregado 
como para o empregador para tomar as medidas necessárias antes que se instalem consequências mais graves relacionadas ao trabalho, como \ndepressão ou síndrome de Burnout.\033[m''')
print('-='*67)
print('\033[1;31mSerão 10 perguntas no total, responda: \n 1 para NÃO,\n 2 para ÀS VEZES,\n 3 para SIM.\033[m')
print('\033[7;31mOBSERVAÇÃO1: LEIA ATENTAMENTE AS INTRUÇÕES ANTES DE RESPONDER, NÃO DIGITAR ENTER ANTES DE RESPONDER.\033[m')
print('\033[7;31mOBSERVAÇÃO2: RESPONDER APENAS COM VALORES NUMÉRICOS AS 10 PERGUNTAS SOBRE COMO VOCÊ SE SENTE NO SEU TRABALHO.\033[m')
print('\033[7;31mOBSERVAÇÃO3: CASO ALGUMA RESPOSTA GERE UMA MENSAGEM DE ERRO, FECHE O PROGRAMA E TENTE RODAR NOVAMENTE.\033[m')
print('~~'*67)
p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
while p1 != 1 and p1 != 2 and p1 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
while p2 != 1 and p2 != 2 and p2 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado quando vai chegando o fim do expediente de trabalho.  '))
while p3 != 1 and p3 != 2 and p3 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
while p4 != 1 and p4 != 2 and p4 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
while p5 != 1 and p5 != 2 and p5 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
while p6 != 1 and p6 != 2 and p6 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
while p7 != 1 and p7 != 2 and p7 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva. '))
        p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
p8 = int(input('\033[32mPergunta 8: \033[mSinto que NÃO posso confiar nos meus colegas de trabalho. '))
while p8 != 1 and p8 != 2 and p8 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p8 = int(input('\033[32mPergunta 8: \033[mSinto que NÃO posso confiar nos meus colegas de trabalho. '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
        p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
        p8 = int(input('\033[32mPergunta 8: \033[mSinto que NÃO posso confiar nos meus colegas de trabalho. '))
p9 = int(input('\033[32mPergunta 9: \033[mSe meu salário fosse mais justo, me motivaria mais a trabalhar. '))
while p9 != 1 and p9 != 2 and p9 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p9 = int(input('\033[32mPergunta 9: \033[mSe meu salário fosse mais justo, me motivaria mais a trabalhar. '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
        p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
        p8 = int(input('\033[32mPergunta 8: \033[mSinto que NÃO posso confiar nos meus colegas de trabalho. '))
        p9 = int(input('\033[32mPergunta 9: \033[mSe meu salário fosse mais justo, me motivaria mais a trabalhar. '))
p10 = int(input('\033[32mPergunta 10: \033[mJá sofri/sofro assédio moral no meu trabalho. '))
while p10 != 1 and p10 != 2 and p10 != 3:
    print('Você digitou um número inválido. \033[32m[1] para NÃO / [2] para ÀS VEZES / [3] para SIM\033[m')
    c1 = str(input('Deseja continuar de onde parou?[Sim ou Não?] ')).strip().upper()[0]
    if c1 in 'S':
        p10 = int(input('\033[32mPergunta 10: \033[mJá sofri/sofro assédio moral no meu trabalho. '))
    elif c1 in 'N':
        p1 = int(input('\033[32mPergunta 1: \033[mÉ dificil para mim terminar tarefas de trabalho em tempo hábil. '))
        p2 = int(input('\033[32mPergunta 2: \033[mQuase nunca consigo ser pontual no trabalho.  '))
        p3 = int(input('\033[32mPergunta 3: \033[mSinto-me sempre aliviado(a) quando vai chegando o fim do expediente de trabalho.  '))
        p4 = int(input('\033[32mPergunta 4: \033[mFico ansioso(a) para que chegue logo a sexta-feira.  '))
        p5 = int(input('\033[32mPergunta 5: \033[mMe sinto explorado no meu trabalho.  '))
        p6 = int(input('\033[32mPergunta 6: \033[mNão encontro sentido em fazer o que faço no meu trabalho. Apenas o salário me motiva.  '))
        p7 = int(input('\033[32mPergunta 7: \033[mSinto-me constantemente oprimido(a) pelo meu/minha chefe. '))
        p8 = int(input('\033[32mPergunta 8: \033[mSinto que NÃO posso confiar nos meus colegas de trabalho. '))
        p9 = int(input('\033[32mPergunta 9: \033[mSe meu salário fosse mais justo, me motivaria mais a trabalhar. '))
        p10 = int(input('\033[32mPergunta 10: \033[mJá sofri/sofro assédio moral no meu trabalho. '))
print('~~'*67)
if (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10) == 10:
    print('\033[32mVocê está aparentemente feliz com o seu trabalho e pode se desenvolver melhor nas outras áreas da sua vida!\033[m')
elif 10 < (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10) <= 18:
    print('\033[32mVocê está no lugar certo mas sente que pode melhorar!Alguns ajustes podem ser feitos. Converse com seu chefe.\033[m')
elif 18 < (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10) <= 25:
    print('\033[1;31mVocê está aparentemente infeliz no seu trabalho. Procure ajuda.\033[m')
elif 25 < (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10) <= 30:
    print('\033[7;31mVocê precisa de ajuda. Não negligencie o fato de estar completamente infeliz no trabalho!\033[m')





