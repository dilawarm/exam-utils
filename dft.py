import numpy as np
import sympy

def createDFTMatrix(n):
    w = sympy.cos(-(2*sympy.pi)/n) + 1j*sympy.sin(-(2*sympy.pi/n))
    dftMatrix = [[None for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            dftMatrix[i][j] = w**(cnt*j)
        cnt += 1
    
    return np.asarray(dftMatrix, dtype=np.complex)

if __name__ == "__main__":
    n = int(input("Antall elementer i vektoren: "))
    print("Elementene i vektoren:")
    x = []
    for _ in range(n):
        x.append(int(input()))
    
    x = np.asarray(x, dtype=np.complex)
    dftMatrix = createDFTMatrix(n)

    dft = np.asarray(1/sympy.sqrt(n)*dftMatrix.dot(x), dtype=np.complex)

    print(f"DFT(x) = {dft}")