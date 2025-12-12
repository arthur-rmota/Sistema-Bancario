import funcoesBanco as fb
import json 
import operacoes as op

contas = fb.leituraInicial()
mov_diario = []

while True: 
    option = fb.funcaoInicial()
    opcao = fb.opcoesMenu(option)
    
    if op.verificarParada(opcao) is False:
        break
    
    elif opcao == 1: #deposito
        conta = fb.dadosOperacao(contas, "depósito")
        op.verificarDeposito(conta, mov_diario, contas)
        
    elif opcao == 2: #saque
        conta = fb.dadosOperacao(contas, "saque")
        op.verificarSaque(conta, mov_diario, contas)
        
    elif opcao == 3: #contas cadastradas
        lista = fb.criarLista(contas)
        fb.imprimirLista(lista)
            
    elif opcao == 4: #movimentos diários
        fb.movDiario(mov_diario)
        
    elif opcao == 5: #saldo das contas
        fb.saldoContas(contas)
        
    elif opcao == 6: #cadastro de novos usuários
        conta = fb.criarTipo()
        novoUsuario = fb.cadastrar(conta)
        
        with open('BancoDeDados.txt', 'a', encoding='UTF-8') as banco: 
            banco.write(json.dumps(novoUsuario) + "\n") # o json.dumps converte o dicionário retornado da função para o formato JSON (com aspas duplas "")
            print(f'Usuáro Cadastrado, Seja Bem Vindo(a) {novoUsuario['cliente']}, O número da sua conta é: {novoUsuario['num']} ')  

    elif opcao == 7: #transferência
        transferencia = fb.dadosOperacaoTransferencia(contas)
        
        if transferencia is None:
            fb.mensagemErro(f'Saldo indisponível')
        else:
            mov_diario.append(transferencia)
            fb.atualizarBancoDados(contas)
            print('\nOperação Realizada com sucesso!')