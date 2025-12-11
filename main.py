import funcoesBanco as fb
import json 

contas = fb.leituraInicial()
mov_diario = []

while True: 
    try:
        option = int(input('\nCONTROLE BANCÁRIO \n'
            'Como podemos te ajudar hoje? \n'
            '1- Depósito \n2- Saque\n3- Tipos de Conta \n4- Movimento Diário \n5- Saldo das Contas \n6- Cadastrar Nova Conta \n7- Transferência entre contas \n8- Sair \n'))
    except ValueError:
        fb.mensagemErro("Insira um Número válido")
        continue
    opcao = fb.opcoesMenu(option)
    if opcao == False:
        fb.mensagemErro("Insira uma opção Válida")
    elif opcao == 8:
        print('Até logo!')
        break
    elif opcao == 1: #deposito
        conta = fb.dadosOperacao(contas, "depósito")
        if conta is None:
            fb.mensagemErro("Digite uma conta válida e tente novamente")
        else: 
            deposito = fb.novoDeposito(conta[0],conta[1])
            mov_diario.append(deposito)
            fb.atualizarBancoDados(contas)
            print("\nOperação Realizada com sucesso")
        
    elif opcao == 2: #saque
        conta = fb.dadosOperacao(contas, "saque")
        if conta is None:
            fb.mensagemErro("Digite uma conta válida e tente novamente")
        else:
            saque = fb.novoSaque(conta[0], conta[1])
            if saque is not None:
                mov_diario.append(saque)
                fb.atualizarBancoDados(contas)
                print('\nOperação Realizada com sucesso!')
            else:
                print(f'\nSaldo Indisponível, O valor máximo para saque é de R${conta["Saldo"]:.2f}')
        
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
           fb.mensagemErro("Insira uma das opções corretas e Tente novamente")  

        novoUsuario = fb.cadastro(conta, cliente)

        with open('BancoDeDados.txt', 'a', encoding='UTF-8') as banco: 
            banco.write(json.dumps(novoUsuario) + "\n") # o json.dumps converte o dicionário retornado da função para o formato JSON (com aspas duplas "")
            print(f'Usuáro Cadastrado, Seja Bem Vindo(a) {cliente}, O número da sua conta é: {novoUsuario['num']} ')  

    elif opcao == 7: #transferência
        transferencia = fb.dadosOperacaoTransferencia(contas)
        
        if transferencia is None:
            fb.mensagemErro(f'Saldo indisponível')
        else:
            mov_diario.append(transferencia)
            fb.atualizarBancoDados(contas)
            print('\nOperação Realizada com sucesso!')