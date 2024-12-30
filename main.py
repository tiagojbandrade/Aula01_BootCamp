CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu Nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite seu Salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite seu Bonus: "))

# 4) Calcule o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprima cálculo do KPI para o usuário
print(f"O usuario: {nome_usuario} possui o bonus: {valor_bonus}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?