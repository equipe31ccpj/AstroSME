from gerar_porcentagem_energia import gerar_valores_energia
import random
import math



def calcular_grandezas_irosa():
    porcentagem = gerar_valores_energia()
    tempo = 1.0 # Tempo medido em horas
    potencia = 30 * 4  # quantidade de paineis solares
    energia = potencia * tempo
    tensao = 160
    corrente = potencia / tensao
    rendimento = porcentagem / 100.0
    potencia_util = potencia * rendimento
    fator_potencia = random.uniform(0.85, 0.98)
    potencia_aparente = potencia / fator_potencia
    potencia_reativa = math.sqrt(potencia_aparente**2 - potencia**2)
    return energia, potencia, tensao, corrente, rendimento, potencia_util, fator_potencia, potencia_aparente, potencia_reativa
