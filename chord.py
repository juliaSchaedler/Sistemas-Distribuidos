class Nodo:
    def __init__(self, id, next, nextNo, head, tail, ativo, dado):
        self.id = id
        self.next = next
        self.nextNo = nextNo
        self.head = head
        self.tail = tail
        self.ativo = ativo
        self.dado = dado

def criaNodo(id, next, ativo):
    nodo = Nodo(id, next, None, None, None, ativo, "")
    return nodo

def insereProximoNodo(id, next, ativo):
    nodo = Nodo(id, next, None, None, None, ativo, "")
    return nodo

def iniciaChord(k):
    nodo = criaNodo(0, None, 0)
    aux = nodo
    for i in range(k, -1, -1):
        nodo = insereProximoNodo(i, nodo, 0)
    aux.next = nodo
    return aux

def percorreChord(nodo):
    aux = nodo.next
    while aux != nodo:
        print(" ", aux.id, end="")
        aux = aux.next

def ativarNo(nodo, i):
    aux = nodo.next
    while aux != nodo:
        if aux.id == i:
            aux.ativo = 1
        aux = aux.next

def verificarAtivos(nodo):
    aux = nodo.next
    while aux != nodo:
        if aux.ativo == 1:
            print("\nnodo[{}]: ativo".format(aux.id))
        aux = aux.next

#Função que retorna uma lista encadeada com os nõs ativos no chord, 
# onde aux pega o proximo nodo do nodo inicial. Entra num loop até chegar 
# no aux novamente, verificando se aux tá ativo e armazenando o valor no aux3, 
# e o proximo nodo no aux2. Entra em outro loop para percorrer os nodos 
# a partir do aux2, verificando se este está ativo e o conecta no 'nextNo' 
# do aux3, att o aux3 para apontar para o aux2. Segue até fechar o ciclo.
def conectaNos(nodo): 
    aux = nodo.next 
    aux2 = None
    aux3 = None
    while aux != nodo:
        if aux.ativo == 1:
            aux3 = aux
            aux2 = aux.next
            break
        aux = aux.next
    while aux2 != aux:
        if aux2.ativo == 1:
            aux3.nextNo = aux2
            aux3 = aux2
        aux2 = aux2.next
    aux3.nextNo = aux

#verifica e imprime as conexões entre os nodos ativos no chord. Começa a verificação 
# com o primeiro nodo, se ele tá ativo, passa para o próximo até voltar nele.
def verificaConexao(nodo):
    aux = nodo.next
    aux2 = None
    while aux != nodo:
        if aux.ativo == 1:
            break
        aux = aux.next
    if aux.ativo == 0:
        print("\nnenhum nodo ativo\n")
    else:
        aux2 = aux.nextNo
        print("\nnodo[{}] Proximo nodo [{}]".format(aux.id, aux.nextNo.id))
        while aux2 != aux:
            print("\nnodo[{}] Proximo nodo [{}]".format(aux2.id, aux2.nextNo.id))
            aux2 = aux2.nextNo

#Organiza os índices dos nodos ativos no chord, iniciando a partir do próximo 
# nodo do inicial. Dentro do loop, que vai até chegar no nodo inicial, 
# verifica se os nós estão ativos, att o head deles para apontar para próx ativo.
def agruparIndices(nodo):
    aux = nodo.next
    aux2 = None
    aux3 = None
    while aux != nodo:
        if aux.ativo == 1:
            break
        aux = aux.next
    aux3 = aux
    aux2 = aux.nextNo
    while aux2 != aux:
        aux3.nextNo.head = aux3.next
        aux3 = aux3.nextNo
        aux2 = aux2.nextNo
    aux2.head = aux3.next

#verifica e imprime os índices e as heads dos nodos ativos, iniciando no nodo inicial, 
# passando para um loop até o inicial, imprimindo o id e a head associada a tal nodo.
def verificaIndices(nodo):
    aux = nodo.nextNo
    while aux != nodo:
        print("\nnodo[{}]: ativo head: [{}]".format(aux.id, aux.head.id))
        aux = aux.nextNo
    print("\nnodo[{}]: ativo head: [{}]".format(aux.id, aux.head.id))

def retornaAtivo(nodo):
    aux = nodo.next
    while aux != nodo:
        if aux.ativo == 1:
            return aux
        aux = aux.next

def desativarNo(nodo, i):
    aux = nodo.next
    while aux != nodo:
        if aux.id == i:
            aux.ativo = 0
        aux = aux.next



#insere um dado em um nodo especifico, com base em sua posicao. 
# Aux retorna o 1 primeiro nodo ativo, aux2 recebe este valor e aux3 ponto para o próximo. 
# A posicao é calculada pela funçao 'indicaposicao', e inicia um loop para verificar 
# se a posicao do dado está entre os índices do nodo atual e sua head. 
# Se estiver no intervalo, inicia um 2 loop onde verifica se o indice do nodo atual 
# é igual a posicao calculada. Se for igual, insere o dado. 
# O 3 loop é pra caso o indice do nodo seja igual na posicao, mas head diferente, 
# verificando se a posicao é igual a calculada. Se for, insere.
def insereDado(nodo, dado, k):
    aux = retornaAtivo(nodo)
    aux2 = aux
    aux3 = aux.nextNo
    pos = indicaPosicao(dado, k)
    while aux3 != aux:
        if pos > aux.id or pos < aux.head.id:
            aux = aux.nextNo
        else:
            aux2 = aux.head
            while aux2 != aux:
                if aux2.id == pos:
                    print("\n{} inserido no nodo {}".format(dado, pos))
                    aux2.dado = dado
                    return
                aux2 = aux2.next
    while aux2.head != aux2:
        if aux2.id == pos:
            print("\n{} inserido no nodo {}".format(dado, pos))
            aux2.dado = dado
            return
        aux2 = aux2.next

def indicaPosicao(dado, k):
    hash = 0
    for i in range(len(dado)):
        hash = 2.3 * hash + ord(dado[i])
    return int(hash) % k + 1



#Pesquisa e imprime um dado com base a posicao. 
# O Aux é o primeiro nodo ativo, aux2 recebe esse valor e aux3 o próximo valor. 
# Chama indicaPosicao para calcular a posicao. 
# Loop verifica se a posicao do dados está entre os inddices do nodo atual e a head. 
# Se tiver, entra outro loop para verificar o intervado, vendo se o indice é igual a
# posicao, se for, imprime. O 3 loop é pra quando a head é diferente, 
# mas o indice = posicao, verificando se o indice é igual a posicao, se for, imprime.
def pesquisaDado(nodo, dado, k):
    aux = retornaAtivo(nodo)
    aux2 = aux
    aux3 = aux.nextNo
    pos = indicaPosicao(dado, k)
    while aux3 != aux:
        if pos > aux3.id or pos < aux3.head.id:
            aux3 = aux3.nextNo
        else:
            aux2 = aux3.head
            while aux2 != aux3:
                if aux2.id == pos:
                    print("\nDADO ENCONTRADO: {} posicao: {} atraves do No: {}".format(aux2.dado, aux2.id, aux3.id))
                    return
                aux2 = aux2.next
    while aux2.head != aux2:
        if aux2.id == pos:
            print("\nDADO ENCONTRADO: {} posicao: {} atraves do No: {}".format(aux2.dado, aux2.id, aux3.id))
            return
        aux2 = aux2.next

#--------------------------------------------------------------- testes
nodo = iniciaChord(15)

percorreChord(nodo)

ativarNo(nodo, 1)
ativarNo(nodo, 6)
ativarNo(nodo, 11)
ativarNo(nodo, 13)

conectaNos(nodo)
agruparIndices(nodo)
verificaIndices(retornaAtivo(nodo))

ativarNo(nodo, 8)
conectaNos(nodo)
agruparIndices(nodo)

print("\n--------------------------\n")
verificaIndices(retornaAtivo(nodo))
desativarNo(nodo, 8)
conectaNos(nodo)
agruparIndices(nodo)



print("\n--------------------------\n")
verificaIndices(retornaAtivo(nodo))
insereDado(nodo, "filme", 15)

print("\n--------------------------\n")
verificaIndices(retornaAtivo(nodo))
insereDado(nodo, "filme 2", 8)

print("\n--------------------------\n")
pesquisaDado(nodo, "filme", 15)

print("\n--------------------------\n")
pesquisaDado(nodo, "filme", 8)

#print("teste")
