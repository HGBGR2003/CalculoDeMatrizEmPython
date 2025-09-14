import math
import numpy as np

# --- Matrizes de rotação ---
def rotacao_x(theta):
    return np.array([
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ])

def rotacao_y(theta):
    return np.array([
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ])

def rotacao_z(theta):
    return np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0, 0, 1]
    ])

# --- Transformação homogênea (4x4) ---
def matriz_transformacao(R, t):
    """
    R = matriz de rotação 3x3
    t = vetor de translação [tx, ty, tz]
    """
    T = np.eye(4)
    T[0:3, 0:3] = R
    T[0:3, 3] = t
    return T

# --- Impressão bonita ---
def imprimir_matriz(nome, M, casas=3):
    print(f"\n{nome}:")
    for linha in M:
        print("  [", "  ".join(f"{float(v): .{casas}f}" for v in linha), "]")

# =======================
# Exemplo 1: Rotação simples (30° em Z)
# =======================
theta = math.radians(30)
Rz = rotacao_z(theta)

B_P = np.array([0, 2, 0])              # Ponto em B
A_P = Rz.dot(B_P)                      # Transformação para A

imprimir_matriz("Matriz de rotação Rz(30°)", Rz)
print("\nPonto em B:", B_P)
print("Ponto em A:", [round(float(x), 3) for x in A_P])

# =======================
# Exemplo 2: Transformação homogênea (rotação + translação)
# =======================
T = matriz_transformacao(Rz, [10, 5, 0])   # 30° em Z + translação (10,5,0)

B_P_h = np.array([3, 7, 0, 1])             # Ponto homogêneo em B
A_P_h = T.dot(B_P_h)                       # Ponto em A (homogêneo)

imprimir_matriz("Matriz de transformação ^A T_B", T)
print("\nPonto homogêneo em B:", B_P_h)
print("Ponto homogêneo em A:", [round(float(x), 3) for x in A_P_h])
