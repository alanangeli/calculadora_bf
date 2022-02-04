nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


#import.math


while True:
    print("Digite o número de acordo com seu sexo")
    print(" 1 - Homem")
    print(" 2 - Mulher")
    sexo = input("Sexo: ")
    if not sexo.isnumeric():
        print("Digite apenas números! 1 para Homem ou 2 para Mulher!")
        continue
    else:
        sexo = int(sexo)
        print()
        break

while True:
    peso = input("Digite seu peso em kg: ")
    if not peso.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        print()
        break

while True:
    altura = input("Digite sua altura em centímetros: ")
    if not altura.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        print()
        break

while True:
    cintura = input("De barriga vazia, em jejum, murche a barriga e meçado umbigo, em centímetros: ")
    if not cintura.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        print()
        break

while sexo == 2:
    quadril = input("Quadril: ")
    if not quadril.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        quadril = float(quadril)
        print()
        break



while True:
    pescoço = input("Meça o pecoço acima do trapézio: ")
    if not pescoço.isnumeric():
        print("Digite apenas números!")
        continue
    else:
        print()
        import math
        altura = float(altura)
        cintura = float(cintura)
        pescoço = float(pescoço)
        peso = float(peso)

        if sexo == 1:
            bfh = 495 / (1.0324 - 0.19077 * math.log10(cintura - pescoço) + 0.15456 * math.log10(altura)) - 450
            print("Seu percentual de gordura é de: ", "{:.1f}".format(bfh), "%")
            massa_gordura = bfh * peso
            massa_gordura = int(massa_gordura)
            massa_gordura_kg = massa_gordura / 100

            massa_muscular = peso - massa_gordura_kg
            massa_muscular = int(massa_muscular)
            massa_muscular_kg = massa_muscular
            print(massa_gordura_kg)
            print("Sua massa de gordura corporal é de: ", "{:.1f}".format(massa_gordura_kg), "kg")
            print("Sua massa muscular é de: ", "{:.1f}".format(massa_muscular), "kg")

        else:
            bfm = 495 / (1.29579 - 0.35004 * math.log10(cintura + quadril - pescoço) + 0.22100 * math.log10(altura)) - 450
            print("Seu percentual de gordura é de: ", "{:.1f}".format(bfm), "%")
            massa_gordura = bfm * peso
            massa_gordura = int(massa_gordura)
            massa_gordura_kg = massa_gordura / 100

            massa_muscular = peso - massa_gordura_kg
            massa_muscular = int(massa_muscular)
            massa_muscular_kg = massa_muscular
            print(massa_gordura_kg)
            print("Sua massa de gordura corporal é de: ", "{:.1f}".format(massa_gordura_kg), "kg")
            print("Sua massa muscular é de: ", "{:.1f}".format(massa_muscular), "kg")


        break







