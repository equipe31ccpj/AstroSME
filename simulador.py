from funcoes import calcular_grandezas_irosa, menu_inicial, relatorio_simaulcao
import time

def main():
    cont = 0
    tempo, qnt_irosa, duracao_seg = menu_inicial()
    while cont <= duracao_seg:
        time.sleep(1)
        cont += 1

        energia, potencia, tensao, corrente, rendimento, potencia_util, fator_potencia, potencia_aparente, potencia_reativa = calcular_grandezas_irosa(tempo, qnt_irosa)

        print(f'Simulação {cont}')
        relatorio_simaulcao(energia, potencia, tensao, corrente, rendimento, potencia_util, fator_potencia, potencia_aparente, potencia_reativa)
    print('Fim da simulação!')
    time.sleep(1.5)
    print('Encerrando programa.')

if __name__ == "__main__":
    main()