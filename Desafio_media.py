# Programa para calcular a média da FIAP excluindo a nota da menor prova:

p1_1 = float(input("Digite a nota da Prova 1 do 1º Semestre:"))
p2_1 = float(input("Digite a nota da Prova 2 do 1º Semestre:"))
p3_1 = float(input("Digite a nota da Prova 3 do 1º Semestre:"))
s1_1 = float(input("Digite a nota da Sprint 1 do 1º Semestre:"))
s2_1 = float(input("Digite a nota da Sprint 2 do 1º Semestre:"))
gs_1 = float(input("Digite a nota da Global Solution do 1º Semestre:"))

if p1_1 < p2_1 and p1_1 < p3_1:
    menor_nota = p1_1
if p2_1 < p1_1 and p2_1 < p3_1:
    menor_nota = p2_1
if p3_1 < p1_1 and p3_1 < p2_1:
    menor_nota = p3_1
somas_p = (p1_1 + p2_1 + p3_1 - menor_nota)
media_1 = (((somas_p + s1_1 + s2_1)/4) * 0.4) + (gs_1 * 0.6)

p1_2 = float(input("Digite a nota da Prova 1 do 2º Semestre:"))
p2_2 = float(input("Digite a nota da Prova 2 do 2º Semestre:"))
p3_2 = float(input("Digite a nota da Prova 3 do 2º Semestre:"))
s1_2 = float(input("Digite a nota da Sprint 1 do 2º Semestre:"))
s2_2 = float(input("Digite a nota da Sprint 2 do 2º Semestre:"))
gs_2 = float(input("Digite a nota da Global Solution do 2º Semestre:"))

if p1_2 < p2_2 and p1_2 < p3_2:
    menor_nota = p1_2
if p2_2 < p1_2 and p2_2 < p3_2:
    menor_nota = p2_2
if p3_2 < p1_2 and p3_2 < p2_2:
    menor_nota = p3_2
somas_p = (p1_2 + p2_2 + p3_2 - menor_nota)
media_2 = (((somas_p + s1_2 + s2_2)/4) * 0.4) + (gs_2 * 0.6)

media_final = (media_1 * 0.4) + (media_2 * 0.6)

freq_final = int(input("Entre com a sua frequência nas aulas em porcentagem:"))

if media_final >= 6 and freq_final >= 75:
    print(f"Sua Média Final é {media_final:.2f}. e você está APROVADO")
else:
    print(f"Sua Média Final é {media_final:.2f}. e você está REPROVADO")
