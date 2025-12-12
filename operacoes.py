import funcoesBanco as fb
import json

def verificarSaque(conta,mov_diario,contas):
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
            
def verificarDeposito(conta, mov,contas):
    if conta is None:
            fb.mensagemErro("Digite uma conta válida e tente novamente")
    else: 
        deposito = fb.novoDeposito(conta[0],conta[1])
        mov.append(deposito)
        fb.atualizarBancoDados(contas)
        print("\nOperação Realizada com sucesso")
        
def verificarParada(opcao):
    if opcao == False:
        fb.mensagemErro("Insira uma opção Válida")
    elif opcao == 8:
        print('Até logo!')
        return False
    
def verificarTipoDeConta(num):
    if num > 3 or num < 1:
        return False
    else: 
        return True
    
def verificarTransferencia(transferencia, mov,contas):
    if transferencia is None:
        fb.mensagemErro(f'Saldo indisponível')
    else:
        mov.append(transferencia)
        fb.atualizarBancoDados(contas)
        print('\nOperação Realizada com sucesso!')

def writeBanco(novoUsuario):
    with open('BancoDeDados.txt', 'a', encoding='UTF-8') as banco: 
        banco.write(json.dumps(novoUsuario) + "\n") # o json.dumps converte o dicionário retornado da função para o formato JSON (com aspas duplas "")
        print(f'Usuáro Cadastrado, Seja Bem Vindo(a) {novoUsuario['cliente']}, O número da sua conta é: {novoUsuario['num']} ')