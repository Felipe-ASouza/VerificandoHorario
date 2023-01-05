horas = input('Que horas são? ') #Recebe o dado do usuário

try:
    horas_convertidas = int(horas) #Converte o dado recebido em um número inteiro
    if horas_convertidas >= 0 and horas_convertidas <= 11: #verifica se o número informado é maior ou igual a 0 ou menor igual 11
        print('Bom dia')
    elif horas_convertidas  >= 12 and horas_convertidas <= 17: #Verifica a mesma condição, só que com 12 e 17
        print('Boa tarde')
    elif horas_convertidas >= 18 and horas_convertidas <= 23: #Mesma condição com 18 e 23
        print('Boa noite')
    else:
        print('Não conheço esse horário')
except:
    ...
