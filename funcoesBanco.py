import json

def mensagemErro(msg):
    print(f'\n [ERRO] {msg}')

def leituraInicial():
    with open('BancoDeDados.txt', 'r') as dados:    
        BancoDeDados = []
        for linha in dados:
            elemento = linha.strip('\n')
            BancoDeDados.append(json.loads(elemento))  #json.loads = converte o "elemento" para algum objeto em python
        
    return BancoDeDados

def opcoesMenu(option): 
    if option not in range(1,9):
        return False
    else: 
        return option

def retornarDados(conta, listaContas, valor=0):
    validador = False
    for elemento in range(len(listaContas)):
        if conta == listaContas[elemento]["num"]: 
            validador = True
            return  [listaContas[elemento], valor]
    if validador == False: 
        return None
    
def novoDeposito(dadosConta, valor):
    dadosConta["Saldo"] += valor
    return [dadosConta["num"], valor]
    
def novoSaque(dadosConta, valor):
    if (dadosConta["Saldo"] - valor) < 0:
        return None
    else: 
        dadosConta["Saldo"] -= valor
        return [dadosConta["num"], -valor]
    
def novaTransferencia(contaPagador, valorPago, contaRecebedor):
    if (contaPagador["Saldo"] - valorPago) < 0:
        return None
    else:
        contaPagador["Saldo"] -= valorPago
        contaRecebedor["Saldo"] += valorPago
        return f"Transferencia:({contaPagador['num']}, {-valorPago}) => ({contaRecebedor['num']}, +{valorPago})"

def criarLista(listaContas):
    listaGeral = []
    for elemento in listaContas: 
        item = elemento['num'].split("-")
        if item[1] == 'C':
            listaGeral.append([elemento["num"], "Corrente"])
        elif item[1] == 'P':
            listaGeral.append([elemento["num"], "Poupança"])
        elif item[1] == 'S':
            listaGeral.append([elemento["num"], "Salário"])
    return listaGeral

def movDiario(lista): 
    cont = 1
    for elemento in lista: 
        if type(elemento) is str:
            print(f'Transação {cont} => {elemento}')
            cont +=1
        elif type(elemento) is list:
            if elemento[1] > 0:
                print(f'Transação {cont} => Conta: {elemento[0]}; Valor Depositado: {elemento[1]}')
                cont +=1
            elif elemento[1] < 0: 
                print(f'Transação {cont} => Conta: {elemento[0]}; Valor Sacado: {abs(elemento[1])}')
                cont +=1
            
def saldoContas(dados):
    for elemento in dados:
        print(f'A conta: {elemento["num"]} possui saldo de {(elemento["Saldo"]):.2f}R$')
        
def analisarContasDisponiveis(tipo):
    contador = 0 
    with open('BancoDeDados.txt', 'r') as dados:
        for elemento in dados:
            if json.loads(elemento)['num'][5] == tipo:
                contador +=1
    return contador
            
def cadastro(tipoConta, cliente): 
    novoUsuario = {}
    if tipoConta == 1:
        numConta = analisarContasDisponiveis('C')+1
        novoUsuario['num'] = f'100{numConta}-C'
    elif tipoConta == 2: 
        numConta = analisarContasDisponiveis('S')+1
        novoUsuario['num'] = f'100{numConta}-S'
    elif tipoConta == 3:
        numConta = analisarContasDisponiveis('P')+1
        novoUsuario['num'] = f'100{numConta}-P'

    novoUsuario['cliente'] = cliente
    novoUsuario['Saldo'] = 0
    
    return novoUsuario

def verificarTipoDeConta(num):
    if num > 3 or num < 1:
        return False
    else: 
        return True
    
def atualizarBancoDados(contas):
    with open ('BancoDeDados.txt', 'w') as dado:
        for item in contas:
            dado.write(json.dumps(item) + "\n")
    
def lerEntrada(msg):
    while True: 
        try:
            valor = float(input(msg).replace(",",".") )
            if valor <= 0:
                mensagemErro("Digite um valor maior que ZERO")
            else:
                return valor
        except ValueError: 
            mensagemErro("digite um número")
            continue
        
def dadosOperacao(contas,txt):
    cod = input('Insira o número da conta:')
    valor = lerEntrada(f'Insira o valor do {txt}')
    conta = retornarDados(cod,contas, valor)

    return conta

def dadosOperacaoTransferencia(contas):
    codPagador = input('Insira o número da conta do Pagador')
    valorPago = lerEntrada('Insira o Valor a ser pago')
    contaPagador = retornarDados(codPagador, contas, valorPago)
    
    codRecebedor = input('Insira o número da conta do Recebedor')
    contaRecebedor = retornarDados(codRecebedor, contas)
        
    return novaTransferencia(contaPagador[0], valorPago, contaRecebedor[0])