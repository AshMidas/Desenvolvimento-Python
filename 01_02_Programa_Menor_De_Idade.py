
Sua_Idade = int(input("Sua idade: "))
Seu_Nome = input("Seu_Nome: ")

Adulto = 18
Dif = Sua_Idade - Adulto

if Sua_Idade >= Adulto and Dif >= 2:
    print(Seu_Nome + " " + "Você tem mais de 18 anos, você e adulto faz: " + str(Dif) + " anos!")
elif Sua_Idade >= Adulto and Dif == 1:
    print(Seu_Nome + " " + "Você tem mais de 18 anos, você e adulto faz: " + str(Dif) + " ano!")
elif Sua_Idade >= Adulto and Dif == 0:
    print(Seu_Nome + " " + "Você tem exatamente 18 anos!")
elif Sua_Idade < Adulto and Dif <= -2:
    print(Seu_Nome + " " + "Você não tem 18 anos! faltam: " + str(Dif*-1) + " anos para completar 18 anos!")
elif Sua_Idade < Adulto and Dif == -1:
    print(Seu_Nome + " " + "Você não tem 18 anos! falta apenas: " + str(Dif*-1) + " ano para completar 18 anos!")
