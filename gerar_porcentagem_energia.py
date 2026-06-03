import random

pesos = [50,25,10,5]
situacao = ['NORMAL', 'ATENÇÃO', 'CRÍTICA', 'URGENTE']

def gerar_valores_energia():
    definir_situacao = random.choices(situacao, weights=pesos, k=1)[0]
    if definir_situacao == 'NORMAL':
        porcentagem_energia = random.randint(80, 100)
    elif definir_situacao == 'ATENÇÃO':
        porcentagem_energia = random.randint(50, 79)
    elif definir_situacao == 'CRÍTICA':
        porcentagem_energia = random.randint(30, 49)
    else:
        porcentagem_energia = random.randint(0, 29)
    return porcentagem_energia