#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

notas = []
for i in range(1,5):
    nota = float(input(f"digite a nota {i}:  "))
    notas.append(nota)

print("as notas são: ",notas)
print("a média das notas é:", sum(notas) / len(notas))