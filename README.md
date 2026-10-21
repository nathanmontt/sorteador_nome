# Sorteador de Nomes sem Repetição (CLI)

Um programa de terminal desenvolvido em Python para realizar sorteios justos.

O sistema recebe uma lista de nomes e garante que cada pessoa tenha apenas uma chance de ganhar, independentemente de quantas vezes o nome dela tenha sido inserido. 

## Funcionalidades

- **Adição de participantes:** o usuário pode digitar vários nomes para participarem do sorteio, com validação inteligente que impede entradas vazias ou contendo números.
- **Filtro anti-spam (Remoção de Duplicatas):** o programa adiciona os nomes diretamente em um `set()`, ignorando automaticamente qualquer entrada repetida.
- **Visualização da lista:** exibe todos os participantes cadastrados e devidamente enumerados.
- **Sorteador imparcial:** escolhe um vencedor de forma totalmente aleatória utilizando o módulo nativo `random`.

## _Feats_ Futuras

- [x] **Sortear múltiplos nomes de uma vez:** melhorar a lógica para permitir múltiplos ganhadores diferentes em um único sorteio (1º, 2º e 3º lugar, por exemplo).
- [ ] **Reiniciar torneio:** adicionar uma opção no menu que guarda a lista original de participantes e permite reconstruir o set quando quiser começar novamente.
- [ ] **Remover participante:** permitir a exclusão de um nome específico antes de o sorteio iniciar.
- [x] **Mostrar simples estatísticas:** permitir a amostragem de estatísticas simples, como o total de participantes, a quantidade de nomes restantes e de vencedores, um percentual já sorteado, entre outras.

## Pré-requisitos

Para rodar este projeto, você precisa ter o **Python 3.10 ou superior** instalado no seu computador, pois o código utiliza a estrutura moderna de controle de fluxo `match/case`.

## Como clonar e executar para uso próprio

Se você quiser testar este projeto na sua máquina, siga os passos abaixo:

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório executando o comando:
   ```bash
   git clone https://github.com/nathanmontt/sorteador_nome.git
3. Entre na pasta do projeto que acabou de ser baixado
    ```bash
    python sorteador_nome.py