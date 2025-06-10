print("CALCULO DA DISTANCIA DE LEVENSTEIN! \n")

# Primeiro par
p1 = "casa"
p2 = "casa"

# Diferença entre p1 e p2 = 0 distância
print(f"A distancia entre '{p1}' e '{p2}' é {distance(p1, p2)}")


# Segundo par
p3 = "livro"
p4 = "livros"

# Diferença entre p3 e p4 = 1 distância
print(f"A distancia entre '{p3}' e '{p4}' é {distance(p3, p4)}")


# Terceiro par
p5 = "gato"
p6 = "pato"

# Diferença entre p5 e p6 = 1 distância
print(f"A distancia entre '{p5}' e '{p6}' é {distance(p5, p6)}")


# Quarto par
p7 = "barco"
p8 = "bloco"

# Diferença entre p7 e p8 = 2 distância
print(f"A distancia entre '{p7}' e '{p8}' é {distance(p7, p8)}")


# Quinto par
p9 = "azul"
p10 = "vermelho"

# Diferença entre p9 e p10 = 7 distância
print(f"A distancia entre '{p9}' e '{p10}' é {distance(p9, p10)}")
