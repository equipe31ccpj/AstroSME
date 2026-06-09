from gerar_porcentagem_energia import gerar_valores_energia
import random
import math
import time


def calcular_grandezas_irosa(tempo, qnt_irosa):
    porcentagem = gerar_valores_energia()
    potencia = 30 * qnt_irosa
    energia = potencia * tempo
    tensao = 160
    corrente = potencia / tensao
    rendimento = porcentagem / 100.0
    potencia_util = potencia * rendimento
    fator_potencia = random.uniform(0.85, 0.98)
    potencia_aparente = potencia / fator_potencia
    potencia_reativa = math.sqrt(potencia_aparente**2 - potencia**2)
    return energia, potencia, tensao, corrente, rendimento, potencia_util, fator_potencia, potencia_aparente, potencia_reativa

def verificar_alertas_e_decisao(rendimento, fator_potencia, corrente):
    print("\n[SISTEMA DE MONITORAMENTO - DIAGNÓSTICO]")
    alertas_ativos = False

    if rendimento < 0.40: 
        alertas_ativos = True
        print("[ALERTA]: Rendimento dos painéis iROSA abaixo de 40%!")
        print("Ativando motores de rotação para reenquadramento solar dos painéis.")
        print("Entrando em Modo de Economia de Energia (Desligando laboratório de pesquisas).")
    elif rendimento < 0.65:
        alertas_ativos = True
        print("[AVISO]: Rendimento moderado. Monitorando variações térmicas.")

    if fator_potencia < 0.85:
        alertas_ativos = True
        print(f"[ALERTA]: Fator de Potência crítico ({fator_potencia:.2f})! Risco de sobrecarga reativa.")
        print("Acionando banco de capacitores estáticos para correção do FP.")

    if corrente > 100: 
        alertas_ativos = True
        print(f"[ALERTA]: Corrente total elevada ({corrente:.2f} A) detectada na rede principal!")
        print("Armando disjuntores térmicos das subestações secundárias.")

    if not alertas_ativos:
        print("[STATUS]: Todos os sistemas operando dentro dos limites de segurança nominais.")
    
    print(f"{'-' * 40}")

def menu_inicial():
    print(f'{'=~' * 20}')
    print('Bem vindo AstroSME!!!')
    print(f'{'-' * 40}')
    print('Esse é um simulador de monitoramento de sistemas energéticos da missão espacial experiemtal Mission Control AI.')
    print('Neste simulador está utilizando de base o painel solar Irosa')
    print(f'{'=~' * 20}')
    while True:
        try:
            duracao_min = float(input('Digite em minutos a duração desejada da simulação: '))
            if duracao_min <= 0: raise ValueError
            break
        except ValueError:
            print('[ERRO]: Por favor, digite um valor de duração maior que zero.\n')
    duracao_seg = duracao_min * 60
    while True:
        try:
            tempo = float(input('Digite em horas o espaçamento de tempo entre os medidores: '))
            if tempo <= 0: raise ValueError
            break
        except ValueError:
            print('[ERRO]: Por favor, digite um valor para o espaçamento de tempo maior que zero.\n')
    while True:
        try:
            qnt_irosa = int(input('Digite quantos paineis a nave irá possuir: '))
            if qnt_irosa <= 0: raise ValueError
            break
        except ValueError:
            print('[ERRO]: A nave precisa ter pelo menos 1 painel solar instalado.\n')
    print(f'{'-' * 20}')
    for i in range(5,0,-1):
        print(f'Simulação irá inciar em {i} segundos...')
        time.sleep(1)
    print(f'{'=~' * 20}')
    return tempo, qnt_irosa, duracao_seg

def relatorio_simaulcao(energia, potencia, tensao, corrente, rendimento, potencia_util, fator_potencia, potencia_aparente, potencia_reativa):
        print(f'{'-' * 40}')
        print(f'Tensão ------------> {tensao} V')
        print(f'Corrente ----------> {corrente} A')
        print(f'Potencia ----------> {potencia} W')
        print(f'Energia -----------> {energia} Wh')
        print(f'Rendimento --------> {rendimento * 100:.1f} %')
        print(f'Potência Útil -----> {potencia_util:.2f} W')
        print(f'Fator de Potência -> {fator_potencia:.2f}')
        print(f'Potência Aparente -> {potencia_aparente:.2f} VA')
        print(f'Potência Reativa --> {potencia_reativa:.2f} VAR')
        print(f'{'=~' * 20}')