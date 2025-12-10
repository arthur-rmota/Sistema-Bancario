import funcoesBanco as fb
import json 

contas = fb.leituraInicial()
mov_diario = []

while True: 
    opcao = fb.opcoesMenu()
    if opcao == 7:
        print('Até logo!')
        break
    elif opcao == 1: #deposito
        cod = input('Insira o número da conta:')
        valor = float(input('Insira o valor do Depósito'))
        conta = fb.retornarDados(cod,contas)
        mov_diario.append(fb.novoDeposito(conta,valor))
        fb.atualizarBancoDados(contas)
    elif opcao == 2: #saque
        cod = input('Insira o número da conta')
        valor = float(input('Insira o valor do Saque'))
        conta = fb.retornarDados(cod,contas)
        mov_diario.append(fb.novoSaque(conta, valor))
        fb.atualizarBancoDados(contas)
    elif opcao == 3: #tipos de conta
        lista = fb.criarLista(contas)
        for elemento in lista: 
            print(f'Conta {elemento[0]}, tipo de conta: {elemento[1]}')
    elif opcao == 4: #movimentos diários
        fb.movDiario(mov_diario)
    elif opcao == 5: #saldo das contas
        fb.saldoContas(contas)
    elif opcao == 6: #cadastro de novos usuários
        conta = int(input("Digite o Tipo da conta a ser cadastrada\n1- Conta Corrente  |  2- Conta Salário  |  3- Conta Poupança\n"))
        
        if fb.verificarTipoDeConta(conta) is True:
            cliente = input("Digite o Nome Completo do Cliente\n")
        else:
           print("ERRO, Insira uma das opções corretas e Tente novamente")  

        novoUsuario = fb.cadastro(conta, cliente)

        with open('BancoDeDados.txt', 'a', encoding='UTF-8') as banco: 
            banco.write(json.dumps(novoUsuario) + "\n") # o json.dumps converte o dicionário retornado da função para o formato JSON (com aspas duplas "")
            print(f'Usuáro Cadastrado, Seja Bem Vindo(a) {cliente}, O número da sua conta é: {novoUsuario['num']} ')  