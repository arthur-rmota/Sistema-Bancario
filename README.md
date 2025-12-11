
# Sistema Bancário - Controle Financeiro

Este é um **Sistema Bancário Simples** desenvolvido em Python, com funcionalidades básicas de controle financeiro, como depósitos, saques, consulta de saldo, cadastro de novas contas e transferências. O sistema permite gerenciar diferentes tipos de contas, visualizar o movimento diário e realizar operações de forma organizada e segura.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário depositar valores em uma conta existente.
2. **Saque**: Permite ao usuário realizar saques, desde que haja saldo suficiente na conta.
3. **Tipos de Conta**: Exibe a lista de contas existentes, com seus respectivos tipos (Conta Corrente, Conta Poupança, Conta Salário).
4. **Movimento Diário**: Exibe todos os depósitos, saques e transferências realizadas.
5. **Saldo das Contas**: Exibe o saldo atual de todas as contas cadastradas.
6. **Cadastrar Nova Conta**: Permite cadastrar novas contas de diferentes tipos.
7. **Transferência entre Contas**: Realiza transferências entre duas contas válidas.
8. **Sair**: Encerra o sistema.

## Estrutura de Arquivos

- **BancoDeDados.txt**: Arquivo que armazena as informações das contas bancárias em formato JSON.
- **funcoesBanco.py**: Contém todas as funções principais do sistema (depósito, saque, cadastro, leitura de dados, validações, etc.).
- **main.py**: Arquivo principal que exibe o menu e gerencia as interações do usuário.

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/arthur-rmota/Sistema-Bancario.git
```

2. Acesse a pasta do projeto:

```bash
cd Sistema-Bancario
```

3. Execute o programa principal:

```bash
python main.py
```

4. Use o menu exibido no terminal para realizar as operações:

```
CONTROLE BANCÁRIO
Como podemos te ajudar hoje?
1- Depósito
2- Saque
3- Tipos de Conta
4- Movimento Diário
5- Saldo das Contas
6- Cadastrar Nova Conta
7- Transferência entre contas
8- Sair
```

## Explicação das Operações

### Depósito
- Informe o número da conta.
- Informe um valor válido maior que zero.
- O sistema registra a operação e atualiza o banco de dados.

### Saque
- Informe o número da conta.
- Informe o valor do saque.
- O sistema valida o saldo antes de concluir.

### Tipos de Conta
- Lista todas as contas cadastradas separadas por tipo.

### Movimento Diário
- Exibe todas as operações realizadas durante a execução do sistema.

### Saldo das Contas
- Mostra uma lista com o saldo atualizado de todas as contas.

### Cadastro de Conta
- Escolha entre Conta Corrente, Salário ou Poupança.
- Informe o nome do cliente.
- O sistema cria automaticamente o número da conta.

### Transferência entre Contas
- Informe a conta pagadora.
- Informe o valor.
- Informe a conta recebedora.
- O sistema valida saldo e registra a transação.

## Observações

- Todas as alterações de saldo são automaticamente salvas no arquivo `BancoDeDados.txt`.
- O sistema utiliza validação completa para evitar operações inválidas.
- O usuário pode acompanhar todas as operações realizadas no Movimento Diário.