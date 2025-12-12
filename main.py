import funcoesBanco as fb
import json 
import verificacoes as vf

contas = fb.leituraInicial()
mov_diario = []

while True: 
    option = fb.funcaoInicial()
    opcao = fb.opcoesMenu(option)
    
    if vf.verificarParada(opcao) is False:
        break
    
    elif opcao == 1: #deposito
        conta = fb.dadosOperacao(contas, "depósito")
        vf.verificarDeposito(conta, mov_diario, contas)
        
    elif opcao == 2: #saque
        conta = fb.dadosOperacao(contas, "saque")
        vf.verificarSaque(conta, mov_diario, contas)
        
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