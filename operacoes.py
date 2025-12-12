import funcoesBanco as fb

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

def criarTipo():
    return int(input("Digite o Tipo da conta a ser cadastrada\n1- Conta Corrente  |  2- Conta Salário  |  3- Conta Poupança\n"))
    
def verificarTipoDeConta(num):
    if num > 3 or num < 1:
        return False
    else: 
        return True