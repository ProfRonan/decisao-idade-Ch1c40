idade = input("Digite um numero: ")
idade = int(idade)

if idade < 0:
    print("impossível!")

elif idade < 18:
    print("não precisa se alistar.")
    
elif idade > 18 and idade < 65:
    print("Não esqueça de votar na próxima eleição.")
    
elif idade > 65:
    print("Vá descansar.")
    
else:
    print("eita!")
