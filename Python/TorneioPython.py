# #A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

raio = float(input())
n = 3.14159
area = n * raio**2

print(f"A={area:.4f}")

# #B Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

# Saída
# Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade seguido pelo valor correspondente à soma de A e B. Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

A = int(input())
B = int(input())
SOMA = A + B

print(f"SOMA = {SOMA}")

# #C Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

# Saída
# Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

A = int(input())
B = int(input())

PROD = A * B

print(f"PROD = {PROD}")

# #D Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

# Entrada
# O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

# Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

A = float(input())
B = float(input())
C = float(input())

MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10

print(f"MEDIA = {MEDIA:.1f}")

# #E Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

# Entrada
# O arquivo de entrada contém 4 valores inteiros.

# Saída
# Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A * B - C * D)

print(f"DIFERENCA = {DIFERENCA}")

# #F Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

# Entrada
# O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

nome = (input())
salarioFixo = float(input())
totalVendas = float(input())

result = salarioFixo + (totalVendas * 0.15)

print(f"TOTAL = R$ {result:.2f}")

# #G Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.

# Saída
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

R = float(input())
pi = 3.14159

volume = (4/3) * pi * R**3

print(f"VOLUME = {volume:.3f}")

# #H Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

# Entrada
# O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

# Saída
# Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

X = int(input())
Y = float(input())

total = X / Y

print(f"{total:.3f} km/l")

# #I Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

# Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

# Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

# Entrada
# O arquivo de entrada contém um número inteiro.

# Saída
# Imprima o tempo necessário seguido da mensagem "minutos".

distancia = int(input())

calculo = distancia * 2

print(f"{calculo} minutos")

# #J Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

# Entrada
# O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h).

# Saída
# Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

tempo = int(input())
vel = int(input())
calculo = ((tempo * vel) / 12)

print(f"{calculo:.3f}")
