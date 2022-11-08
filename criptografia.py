alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "1","2","3","4","5","6","7","8","9","0","é","É","è","È","ó","Ó"," ","@",".",",",":","-","_","!","?"]
array = []
arrayDescripto = []
texto1 = input("Digite o texto que deseja criptografar: ")
chave = int(input("Digite a chave: "))

numCaracteres = len(texto1)

# For que criptografa o texto
for i in texto1:
  for l in alfabeto:
    if i == l:
      posLetraAlf = alfabeto.index(l)
      posNova = posLetraAlf + chave
      if posNova < len(alfabeto):
        array.append(alfabeto[posNova])
      else:
        posNova2 = posNova - len(alfabeto)
        array.append(alfabeto[posNova2])

# Concatenando todas as letras do array
array2 = "".join(array)

# for que descriptografa o texto
for i in array2:
  for l in alfabeto:
    if i == l:
      posLetraAlf = alfabeto.index(l)
      posNova = posLetraAlf - chave
      arrayDescripto.append(alfabeto[posNova])

# Concatenando todas as letras do array
array2Descripto = "".join(arrayDescripto)

print("\n***********************************")
print("Chave escolhida: " + str(chave) + "\n")
print("Texto criptografado: " + array2)
print("Texto descriptografado: " + array2Descripto)
print("***********************************")