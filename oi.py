file = open('listinha.txt', 'r')

f = file.readlines()

lista=[]
listacerta = []

for linha in f:
    lista.append(linha.strip())

print(lista)

total = len(lista)

flag = False


## a b c d [ab](0) = {ab} | [bc] (1) = {acb} | [cd]()


'''for nome in range(total):
    if nome == total-1:
        print('sexu')
    print(f'opcao{nome}: {lista[nome]}')'''

def organiza():
    flag = False
    for nome in range(total):
        if nome != total-1:
            opc = input(f'{lista[nome]}(0) ou {lista[nome+1]}(1)?')
            if opc == '0':
                if listacerta.count(lista[nome]) == False:
                    listacerta.append(lista[nome])
            else:
                listacerta.append(lista[nome+1])
                flag = True
            if listacerta.count(lista[nome]) == False:
                listacerta.append(lista[nome])
        else:
            opc = input(f'{lista[-2]}(0) ou {lista[-1]}(1)?')
            if opc == '0':
                listacerta.append(lista[nome])
            else:
                listacerta.insert(len(listacerta)-2, lista[-1])


    print('=======================================================')
    print(listacerta)
    return flag
    
def organiza2():
    flag = False
    for nome in range(total):
        if nome != total-1:
            opc = input(f'{listacerta[nome]}(0) ou {listacerta[nome+1]}(1)?')
            if opc == '0':
                pass
            else:
                aux = listacerta[nome]
                listacerta[nome] = listacerta[nome+1]
                listacerta[nome+1] = aux
                flag = True
        else:
            opc = input(f'{listacerta[-2]}(0) ou {listacerta[-1]}(1)?')
            if opc == '0':
                pass
            else:
                aux = listacerta[-2]
                listacerta[-2] = listacerta[-1]
                listacerta[-1] = aux


    print('=======================================================')
    print(listacerta)
    if flag == True:
        organiza2()


fla = organiza()
if fla == True:
        organiza2()

g = open('listinhacerta.txt', 'w')
for item in range(total):
    g.write(listacerta[item] + '\n')
    
g.close()



