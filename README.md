# Sistema Bancário - Controle Financeiro

Este é um **Sistema Bancário Simples** desenvolvido em Python, com funcionalidades básicas de controle financeiro, como depósitos, saques, consulta de saldo, e cadastro de novas contas. O sistema permite gerenciar diferentes tipos de contas, visualizar o movimento diário e realizar operações de forma eficiente.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário depositar valores em uma conta existente.
2. **Saque**: Permite ao usuário realizar saques, desde que haja saldo suficiente na conta.
3. **Tipos de Conta**: Exibe a lista de contas existentes, com seus respectivos tipos (Conta Corrente, Conta Poupança, Conta Salário).
4. **Movimento Diário**: Exibe todos os depósitos e saques realizados.
5. **Saldo das Contas**: Exibe o saldo atual de todas as contas cadastradas.
6. **Cadastrar Nova Conta**: Permite cadastrar novas contas de diferentes tipos (Conta Corrente, Conta Salário, Conta Poupança).

## Estrutura de Arquivos

- **BancoDeDados.txt**: Arquivo que armazena as informações das contas bancárias em formato JSON.
- **funcoesBanco.py**: Contém as funções principais do sistema, como `leituraInicial()`, `novoSaque()`, `novoDeposito()`, entre outras.
- **main.py**: Arquivo principal que gerencia o menu e interações com o usuário.

## Requisitos

- Python 3.x
- Bibliotecas padrão do Python (sem necessidade de bibliotecas externas)

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/arthur-rmota/Sistema-Bancario.git
