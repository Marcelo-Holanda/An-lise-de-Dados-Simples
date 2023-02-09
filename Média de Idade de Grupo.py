somaidade = 0
mediaidade = 0
maioridadehomem = ''
nomevelho = 0
totmulher20 = 0


for p in range(1,5):
    print('------{}ºpessoa------'.format(p))
    nome = str(input('Digite o nome:')).strip().upper()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o Sexo:[F/M]:')).strip().upper()
    while sexo not in 'FfMm':
        sexo = str(input('Sexo Inválido!Digite o seu sexo:'))
        continue
    somaidade += idade
    mediaidade = somaidade / 3

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


print('A Média de idade do grupo é de {:.2f} Anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Temos o total de {} mulher(es) com menos de 20 anos.'.format(totmulher20))