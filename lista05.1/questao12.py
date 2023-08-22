'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
'''

num = int(input("Informe um número: "))
div = 0

if (num != -1):
    med = num
    maior = num
    menor = num

while (num != -1):
    num = int(input("Informe um número: "))

    if num != -1:
        med = med + num
    if num != -1:
        div = div + 1
    if maior < num and num != -1:
        maior = num
    if menor > num and num != -1:
        menor = num

print(f"O maior número é {maior} e o menor é {menor} e a média é de {med / div}")