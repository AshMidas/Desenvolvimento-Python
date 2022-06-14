Nota_Primeira_Materia = int(input("Qual a nota da primeira materia? "))
Nota_Segunda_Materia  = int(input("Qual a nota da segunda materia? "))
Nota_Terceira_Materia = int(input("Qual a nota da terceira materia? "))
Nota_Quarta_Materia   = int(input("Qual a nota da quarta materia? "))

Media = ( Nota_Primeira_Materia + Nota_Segunda_Materia + Nota_Terceira_Materia + Nota_Quarta_Materia ) / 4



if Media >= 6:
    print("Muito bem sua média é de: " + str(Media) + " você está aprovado!")
else:
    print("Sua média foi de: " + str(Media) + " infelizmente não está aprovado!")

