"""
2. Sorteador de Nomes sem Repetição (Foco em Sets)
Imagine que você fez um sorteio no Instagram e as pessoas comentaram várias vezes. Você precisa sortear um vencedor, mas cada pessoa só pode ter uma "chance" (nome único).
Como funciona: O programa pede para o usuário digitar vários nomes (ou recebe uma lista grande com nomes repetidos). Antes de sortear, o programa remove as duplicatas.
O que você vai praticar: Conversão de Listas para Sets (conjuntos não aceitam valores repetidos), uso da biblioteca nativa random (usando random.choice()).
Toque para o GitHub: No Readme, explique como o uso do set() resolveu o problema de duplicatas em uma única linha de código, mostrando que você entende de otimização básica.
"""
import random

original_sorteador_nome_set = set()
# secondary_sorteador_nome_set = set()
temp_var = []
cont = 1
print("SORTEADOR DE NOMES PARA EVENTOS!")

while True:
    menu_options = input("Digite:\n1 - Adicionar\n2 - Visualizar\n3 - Sortear nomes\n4 - Estatísticas\n5 - Sair\n: ")
    match menu_options:
        case "1":
            while True:
                name = input("Digite um nome, ou 'Q' para sair: ").strip().capitalize()
                if (any(caractere.isdigit() for caractere in name)) or not name:
                    print("Inválido. Digite um nome")
                    continue

                if name.lower() in ("q", "sair", "cancelar"):
                    break

                original_sorteador_nome_set.add(name)

        case "2":
            if not original_sorteador_nome_set:
                print("Sem nomes, adicione um.")
            else:
                for nome in original_sorteador_nome_set:
                    print(f"{cont} - {nome}")
                    cont += 1
                cont = 1
            print()

        case "3":
            if not original_sorteador_nome_set:
                print("Sorteador vazio. Adicione um nome\n")
            else:
                name_list = list(original_sorteador_nome_set)
                # temp_var = random.choice(name_list)

                winners_quantity = int(input("Quantos vencedores quer que apareçam: "))

                if winners_quantity > len(name_list) or winners_quantity <= 0:
                    print("Escolha uma quantidade de vencedores correta.")
                    continue

                for each_winner in range (0, winners_quantity):
                    temp_var = random.choice(name_list)
                    print(f"Parabéns, {temp_var}, você foi sorteado(a)!\nAguarde o contato da equipe para o envio do prêmio!\n")
                    
                    original_sorteador_nome_set.remove(temp_var)
                
        case "4":
            break

        case "5":
            print("Agradecemos a preferência\nUm ótimo dia!")
            break

        case _:
            print("Opção não encontrada")