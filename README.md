# AstroSME — Mission Control AI 🚀

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

O **AstroSME** é um simulador em terminal focado no monitoramento de sistemas energéticos para a missão espacial experimental **Mission Control AI**. O projeto realiza o cálculo e a telemetria em tempo real das grandezas elétricas geradas por painéis solares do tipo **iROSA** (Roll-Out Solar Array), simulando variações de eficiência baseadas em estados operacionais da nave.

---

## 📊 Grandezas Calculadas e Física Aplicada

O simulador utiliza conceitos fundamentais de engenharia elétrica e a **Lei de Joule** para calcular a estabilidade do sistema a cada segundo de voo:

* **Potência Ativa ($W$):** Baseada na quantidade de painéis instalados ($30\text{ W}$ por painel).
* **Corrente Elétrica ($A$):** Calculada através da relação $I = \frac{P}{V}$ sob uma tensão nominal de $160\text{ V}$.
* **Energia ($Wh$):** Consumo e geração acumulada calculados por $E = P \cdot t$.
* **Triângulo das Potências:** O código aplica o Teorema de Pitágoras para encontrar as componentes reativas e aparentes do sistema alternado simulado:
  * **Potência Aparente ($VA$):** $S = \frac{P}{FP}$ (onde $FP$ é o Fator de Potência gerado dinamicamente).
  * **Potência Reativa ($var$):** $Q = \sqrt{S^2 - P^2}$.

---

## 📁 Estrutura do Projeto

O repositório está organizado da seguinte forma:

* `simulador.py`: Arquivo principal contendo a função `main()` que orquestra o laço de repetição e o tempo de execução.
* `funcoes.py`: Concentra a lógica do menu interativo, o motor de cálculo das grandezas elétricas e a formatação do relatório final.
* `gerar_porcentagem_energia.py`: Algoritmo baseado em pesos probabilísticos (`random.choices`) que define o estado da nave (*NORMAL*, *ATENÇÃO*, *CRÍTICO*, *URGENTE*) e varia o rendimento dos painéis.
* `.gitignore`: Arquivo de configuração para ignorar arquivos temporários e locais do ambiente de desenvolvimento (como pastas `.venv` ou `__pycache__`).
* `README.md`: Documentação oficial do projeto.

---

## 🛠️ Pré-requisitos e Tecnologias

Para rodar o simulador, você precisará apenas do ambiente Python instalado. Não há necessidade de instalar bibliotecas externas (pip), pois o projeto utiliza módulos nativos.

* **Python 3.13** (ou superior)
* Bibliotecas nativas:
  * `random` (para geração de estados e fatores de potência)
  * `math` (para cálculos de raiz quadrada e potências)
  * `time` (para controle do relógio de simulação e delays)

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/equipe31ccpj/AstroSME.git](https://github.com/equipe31ccpj/AstroSME.git)
    ```
2. Navegue até a pasta do projeto:
   ```bash
   cd AstroSME
    ```
3. Execute o arquivo principal do simulador:
   ```bash
   python simulador.py
    ```

## 👥 Autoria e Desenvolvedores
Este projeto foi desenvolvido para fins acadêmicos e experimentais pelos integrantes:

Pedro Henrique Neves — RM: 547382

Akin Alexandre — RM: 572773

Maria Eduarda Rocha — RM: 570554