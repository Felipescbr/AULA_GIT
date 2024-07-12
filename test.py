
print("Valores possíveis -> Max: 600, Min: 10")
print("\n")

valor = int(input("Coloque o valor que deseja sacar: "))

notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

if(valor >= 10 and valor <=600):
    while valor >= 100:
        valor -= 100
        notas100 +=1
    
    while valor >= 50:
        valor -= 50
        notas50 += 1

    while valor >= 10:
        valor -= 10
        notas10 += 1

    while valor >= 5:
        valor -= 5
        notas5 += 1

    while valor >= 1:
        valor -= 1
        notas1 += 1

    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5: {notas5}")
    print(f"Notas de 1: {notas1}")
    

else:
    print("Coloque um valor válido!!")