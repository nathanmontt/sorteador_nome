"""
2. Sorteador de Nomes sem Repetição (Foco em Sets)
Imagine que você fez um sorteio no Instagram e as pessoas comentaram várias vezes. Você precisa sortear um vencedor, mas cada pessoa só pode ter uma "chance" (nome único).
Como funciona: O programa pede para o usuário digitar vários nomes (ou recebe uma lista grande com nomes repetidos). Antes de sortear, o programa remove as duplicatas.
O que você vai praticar: Conversão de Listas para Sets (conjuntos não aceitam valores repetidos), uso da biblioteca nativa random (usando random.choice()).
Toque para o GitHub: No Readme, explique como o uso do set() resolveu o problema de duplicatas em uma única linha de código, mostrando que você entende de otimização básica.
"""
import random

sorteador_nome_set = set()

while True:
    menu_options = input("1 pra adicionar, 2 pra mostrar, 3 pra pegar um nome, 4 pra sair: ")
    match menu_options:
        case "1":
            while True:
                name = input("nome, e 'q' pra sair: ")
                if (any(caractere.isdigit() for caractere in name)):
                    print("Inválido. Digite um nome")
                    continue
                if name in ("q", "Q"):
                    break

                sorteador_nome_set.add(name)
        case "2":
            for nome in sorteador_nome_set:
                print(nome)

        case "4":
            break

        case _:
            print("Opção não encontrada")