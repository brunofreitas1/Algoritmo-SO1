import time
import os

# Cores ANSI
CORES = [
    '\033[91m',  # Vermelho
    '\033[92m',  # Verde
    '\033[93m',  # Amarelo
    '\033[94m',  # Azul
    '\033[95m',  # Magenta
    '\033[96m',  # Ciano
]
RESET = '\033[0m'

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def round_robin(processos, quantum, animar=False):
    tempo_atual = 0
    fila = processos.copy()
    historico = []
    tempos_espera = {p['nome']: 0 for p in processos}
    tempos_turnaround = {p['nome']: 0 for p in processos}
    tempo_restante = {p['nome']: p['tempo_execucao'] for p in processos}
    
    print("\nSimulando escalonamento...\n")
    if animar:
        time.sleep(1)
    
    while fila:
        processo = fila.pop(0)
        nome = processo['nome']
        tempo_exec = min(quantum, tempo_restante[nome])
        
        historico.append((nome, tempo_atual, tempo_atual + tempo_exec))
        
        for t in range(tempo_exec):
            if animar:
                limpar_console()
                print(f"Executando: {nome}")
                mostrar_grafico(historico, tempo_atual + t + 1, processos)
                time.sleep(0.5)
        
        tempo_atual += tempo_exec
        tempo_restante[nome] -= tempo_exec
        
        if tempo_restante[nome] > 0:
            fila.append(processo)
        else:
            tempos_turnaround[nome] = tempo_atual

    # Calcular tempo de espera
    for nome in tempos_espera.keys():
        tempos_espera[nome] = tempos_turnaround[nome] - next(p['tempo_execucao'] for p in processos if p['nome'] == nome)
    
    # Mostrar resultado final
    limpar_console()
    mostrar_grafico(historico, tempo_atual, processos)
    
    print("\nResultados finais:")
    print(f"{'Processo':<10}{'Espera':<10}{'Turnaround':<10}")
    for nome in tempos_espera.keys():
        print(f"{nome:<10}{tempos_espera[nome]:<10}{tempos_turnaround[nome]:<10}")
    
    media_espera = sum(tempos_espera.values()) / len(tempos_espera)
    print(f"\nTempo médio de espera: {media_espera:.2f}")
    print(f"Tempo total de processador: {tempo_atual}")

def mostrar_grafico(historico, tempo_final, processos):
    nomes = [p['nome'] for p in processos]
    mapa = {nome: [" " for _ in range(tempo_final)] for nome in nomes}
    
    for idx, (nome, inicio, fim) in enumerate(historico):
        cor = CORES[idx % len(CORES)]
        for t in range(inicio, min(fim, tempo_final)):
            mapa[nome][t] = f"{cor}■{RESET}"

    for nome in nomes:
        linha = f"{nome:<4}| " + "".join(mapa[nome])
        print(linha)

def ler_processos():
    processos = []
    n = int(input("Digite a quantidade de processos: "))
    for i in range(n):
        nome = input(f"Nome do processo {i+1}: ").strip()
        tempo_execucao = int(input(f"Tempo de execução do {nome}: "))
        processos.append({"nome": nome, "tempo_execucao": tempo_execucao})
    return processos

def main():
    print("Escalonamento Round Robin - Simulador\n")
    processos = ler_processos()
    quantum = int(input("\nDigite o valor do Quantum: "))
    animar = input("Deseja simular animação da execução? (s/n): ").lower() == 's'
    
    round_robin(processos, quantum, animar)

if __name__ == "__main__":
    main()
