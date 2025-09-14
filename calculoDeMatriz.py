import math
import numpy as np

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

def matriz_transformacao(R, t):
    T = np.eye(4)
    T[0:3, 0:3] = R
    T[0:3, 3] = t
    return T
def imprimir_matriz(nome, M, casas=3):
    print(f"\n{nome}:")
    for linha in M:
        print("  [", "  ".join(f"{float(v): .{casas}f}" for v in linha), "]")

theta = math.radians(30)
Rz = rotacao_z(theta)

B_P = np.array([0, 2, 0])             
A_P = Rz.dot(B_P)                     

imprimir_matriz("Matriz de rotação Rz(30°)", Rz)
print("\nPonto em B:", B_P)
print("Ponto em A:", [round(float(x), 3) for x in A_P])

T = matriz_transformacao(Rz, [10, 5, 0])   

B_P_h = np.array([3, 7, 0, 1])             
A_P_h = T.dot(B_P_h)                      

imprimir_matriz("Matriz de transformação:", T)
print("\nPonto homogêneo em B:", B_P_h)
print("Ponto homogêneo em A:", [round(float(x), 3) for x in A_P_h])
