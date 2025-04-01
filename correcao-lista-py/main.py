'''
#3
senha_cadastrada = 1234
senha_fornecida = int(input("Qual é a senha?\n->"))

if senha_fornecida == senha_cadastrada:
    print("Acesso permitido")
else:
    print("Acesso negado!")

senha_cadastrada = "1234"
senha_fornecida = input("Qual é a senha?\n->"))

if senha_fornecida == senha_cadastrada:
    print("Acesso permitido")
else:
    print("Acesso negado!")
'''

'''
#4
quantidade = int(input("Diga a quantidade de maças: "))
valor = 0.25
if quantidade < 12:
    valor = 0.3
total = quantidade*valor
print(f"Você gastará R${total:.2f} em {quantidade} maçãs, à R${valor} por maçãs.")
'''

'''
#6
genero = input("Diga masculino ou feminino:")
altura = float(input("Diga sua altura:"))
if genero == 'masculino':
    peso = (72.7*altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print(f"O peso ideal para {genero} de altura {altura} é {peso:;2f}")    
'''

'''
#7e8

lados = int(input("Quantos lados tem sua figura?\n->"))
medida = int(input("Qual é a medida do lado?\n->"))
if lados <3:
    print("Não é um polígono!!!")
elif lados == 3:
    perimetro = lados*medida
    print(f"É um triângulo de perímetro {perimetro}")
elif lados == 4:
    perimetro = lados * medida
    print(f"É um quadrado de perímetro {perimetro}")
elif lados == 5:
    perimetro = lados * medida
    print(f"É um pentágono de perímetro {perimetro}")


lados = int(input("Quantos lados tem sua figura?\n->"))
if lados < 3:
        print("Não é um polígono!!!")
    elif lados == 5:
        print("Poligono nao identificado")
else:
        medida = int(input("Qual é a medida do lado?\n->"))
        perimetro = lados*medida
        if lados == 3:
            forma = 'triangulo'
    elif lados == 4:
        forma = 'quadrado'
    else:
        forma = 'pentágono'
    print(f"É um {forma} de perímetro {perimetro}")
'''

'''
#10
a = int(input("Diga o primeiro lado:"))
b = int(input("Diga o segundo lado:"))
c = int(input("Diga o terceiro lado:"))

if a == b and a == c:
    print("Equilátero")
elif a == b or a == c or c == b:
    print("Isósceles")
else:
    print("Escaleno")
'''

'''
#11
a = int(input("Diga o primeiro angulo:"))
b = int(input("Diga o segundo angulo:"))
c = int(input("Diga o terceiro angulo:"))
if a+b+c == 190:

    if a == 90 or b == 90 or c == 90 :
        print("Triangulo reto")
    elif a > 90 or b > 90 or c > 90 :
        print("Triangulo obtuso")
else:
        print("Triangulo agudo")
else:
        print("Não é um triangulo)        
        
'''

'''
#9
a = int(input("Diga o primeiro numero:"))
b = int(input("Diga o segundo numero:"))
c = int(input("Diga o terceiro numero:"))

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)


a = int(input("Diga o primeiro numero:"))
b = int(input("Diga o segundo numero:"))
c = int(input("Diga o terceiro numero:"))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior) 
'''

'''
#5

a = 2
b = 3
aux = a
a = b
b = aux




a = int(input("Diga o primeiro numero:"))
b = int(input("Diga o segundo numero:"))
c = int(input("Diga o terceiro numero:"))

if a>b and a>c:
    aux = a
    a = c
    c = aux
elif b>c:
    aux = c
    c = b
    b = aux

if a > b:
    aux = a
    a = b
    b = aux

    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    print(maior)

    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    print(menor)
meio = a + b + c - menor - maior
print(menor,?,maior)
'''

num = 777

print(777//10)
print(777//100)
a = num - 100 * 100
a = n
print(a)