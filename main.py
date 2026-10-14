"""
2. Sorteador de Nomes sem Repetição (Foco em Sets)
Imagine que você fez um sorteio no Instagram e as pessoas comentaram várias vezes. Você precisa sortear um vencedor, mas cada pessoa só pode ter uma "chance" (nome único).
Como funciona: O programa pede para o usuário digitar vários nomes (ou recebe uma lista grande com nomes repetidos). Antes de sortear, o programa remove as duplicatas.
O que você vai praticar: Conversão de Listas para Sets (conjuntos não aceitam valores repetidos), uso da biblioteca nativa random (usando random.choice()).
Toque para o GitHub: No Readme, explique como o uso do set() resolveu o problema de duplicatas em uma única linha de código, mostrando que você entende de otimização básica.
"""

sorteador_nome = {}

while True:
    menu_options = input("Digite uma opção do menu:\n1 - Adicionar um nome\n2 - Remover um nome\n3 - Limpar lista de nomes\n4 - Ver Lista completa\n5 - Download (.pdf) [em andamento]\n6 - Sair\n: ").strip()
    
    match menu_options:
        case "1":
            while True:
                nome_participantes = input("Digite os nomes dos participantes, e 'sair' para fechar o programa: ")
                if nome_participantes.lower() in ("sair", "cancelar", "s", "não"):
                    break
                
                nome_participantes = nome_participantes.capitalize()

        case "6":
            break