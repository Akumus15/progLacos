'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
'''

varialvel_b = int(input("Me diga um número que será a sua base: "))
varialvel_e = int(input("Me diga um número que será o seu expoente da sua potência: "))

cont = 1
acumulador = 1

while(cont <= varialvel_e):
    acumulador = acumulador * varialvel_b
    cont = cont + 1
print(f"O valor da potência é {acumulador}")