import random
def cria_matriz(m,n):
    matriz=[]
    for i in range(m):
        linha=[]
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
    return matriz

def adiciona_matriz2(coluna, linha, escolha, matriz2):
    matriz2[linha][coluna]=escolha
    return matriz2


                     
def colocar_bomba(matriz,qtd):
    l=0
    while l<qtd:
        i=random.randint(0,len(matriz)-1)
        j=random.randint(0,len(matriz[0])-1)
        if matriz[i][j]!="B":
            matriz[i][j]=="B"
            l+=1
    return matriz


def desenha(matriz, matriz2):
    linhas=len(matriz)
    colunas=len(matriz[0])
    print('    ', end='')
    for j in range(colunas):
        print('(0:>3d)'.format(j),end=' ')
    print()

    print('    ',end='')
    for j in range(colunas):
        print('----', end='')  
    print('-')
    
    for i in range(linhas):
        print('(0:>3d)'.format(i), end = ' ')
        for j in range (colunas):
            if matriz2[i][j]==0:
                print('| # ', end='')
            elif matriz2[i][j]==1:
                print('|', matriz[i][j],end = '')
            else:
                print('| @ ', end = '')
        print ('|')
        print('     ', end='')
        for j in range (colunas):
            print('----', end='')
        print('-')
        




def numeros(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            ac=0
            if matriz[i][j]!='B':
                if j> 0 and i>0 and matriz[i-1][j-1]=="B":
                    ac+=1
                if i>0 and matriz[i-1][j]=="B":
                    ac+=1
                if i>0 and j<(len(matriz[0]) -1) and matriz[i-1][j+1]=="B":
                    ac+=1
                if j>0 and matriz[i][j-1]=="B":
                    ac+=1
                if j<(len(matriz[0]) -1) and matriz[i][j+1]=="B": 
                    ac+=1
                if i<(len(matriz) -1) and j>0 and matriz[i+1][j-1]=="B": 
                   ac+=1
                if i< (len(matriz) -1) and matriz[i+1][j]=="B": 
                   ac+=1
                if i<(len(matriz) -1) and j<(len(matriz[0]) -1)=="B": 
                   ac+=1
                matriz[i][j]=ac

    print(matriz)
    return matriz


def vencer(matriz,matriz2,qtd):
    cont_b=0
    cont_a=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]=="B":
                if matriz2[i][j]==2:
                    cont_b+=1
                elif matriz[i][j]==1:
                    con_a+=1
    if cont_b== qtd or cont_a==(len(matriz)* len(matriz[0])) - qtd:
        return True
    return False


















def main():
    opcao=0
    while opcao < 1 or opcao > 3:
        opcao=int(input("Dificuldade:\n1 Fácil\n2 Médio\n3 Difícil"))
    if opcao==1:
        matriz=cria_matriz(10,10)
        matriz= colocar_bomba(matriz,3)
        matriz2=cria_matriz(10,10)
    elif opcao==2:
        matriz=cria_matriz(16,16)
        matriz=colocar_bomba(matriz,30)
        matriz2=cria_matriz(16,16)
    else:
        matriz=cria_matriz(16,30)
        matriz=colocar_bomba(m,99)
        matriz2=cria_matriz(16,30)
    m= numeros(matriz)
    print("vamos jogar")
    desenha(matriz,matriz2)
    coluna=0
    linha=0
    cont_b=0
    cont_a=0
    if opcao==1:
        qtd=3
    elif opcao==2:
        qtd=30
    else:
        qtd=99
    while True:
        linha=int(input("linha:"))
        coluna=int(input("coluna:"))
        escolha=int(input("opção\n1 - abrir\n2 - marcar"))
        matriz2=adiciona_matriz2(coluna,linha,escolha,matriz2)
        if matriz[linha][coluna]=="B" and escolha !=2:
            print("game over")
            desenha(matriz,matriz2)
            print("jogar novamente?")
            a= int(input("\n1 - Sim\n2 - Não"))
            if a ==1:
                main()
            else:
                break
        else:
            desenha(matriz,matriz2)
            if vencer(matriz,matriz2,qtd):
                print("Parabéns, voce venceu!")
                print("jogar novamente?")
                b=int(input("\n1 - Sim\n2 - Não"))
                if b==1:
                    main()
                else:
                    break

main()







            
