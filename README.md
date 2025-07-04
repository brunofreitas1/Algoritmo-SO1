# 🖥️ Simulador de Escalonamento Round Robin

Projeto desenvolvido para a disciplina de **Sistemas Operacionais** — 2025, como atividade prática sobre **Políticas de Escalonamento de Processos**.

## 📚 Descrição

Este simulador implementa a política **Round Robin** (Circular, preemptivo) em **Python**, simulando a execução de processos em um ambiente visual no terminal.

Funcionalidades:

- Inserção manual de processos e seus tempos de execução.
- Definição do valor de **Quantum**.
- Simulação visual da execução dos processos (com ou sem animação).
- Exibição colorida do gráfico de escalonamento.
- Cálculo dos principais tempos:
  - Tempo de espera de cada processo.
  - Tempo de turnaround de cada processo.
  - Tempo médio de espera.
  - Tempo total de uso do processador.

## 📋 Requisitos

- Python 3.7 ou superior
- Terminal compatível com ANSI colors (Windows, Linux, Mac).

## ⚙️ Como executar

Clone o projeto ou copie o código.

Execute no terminal:

```bash
python simulador_round_robin.py
```

Depois, basta seguir as instruções no console:

1. Informar a quantidade de processos.
2. Informar o nome e o tempo de execução de cada processo.
3. Informar o Quantum.
4. Escolher se deseja ver a simulação animada.

## 🎨 Demonstração

Exemplo de exibição no terminal:

```
P1  | ■■  ■■  ■■  
P2  |    ■■  ■■  ■■  ■■
P3  |        ■■  ■■
P4  |            ■■
P5  |              ■
```

Legenda:
- Cada **■** representa a execução de um processo durante uma unidade de tempo.
- Cores diferentes indicam processos diferentes.

---

## 📈 Melhorias Futuras

- Geração de gráfico de Gantt com `matplotlib`.
- Suporte para tempos de chegada diferentes.
- Versão web interativa usando Flask ou Django.

## 👨‍💻 Autor

Projeto desenvolvido por Bruno Brandão, Fernando Divino, Gabriel Timóteo e Gustavo Prado  
Disciplina: **Sistemas Operacionais** — **Análise e Desenvolvimento de Sistemas**  
Professor: **Sandro Roberto Armelin**  
Ano: **2025**

---

> "**A melhor maneira de aprender é colocar a mão na massa!**" 🚀

---

## 📎 Observação

Esta atividade será apresentada em seminário no dia **28/04/2025** conforme combinado na disciplina.
