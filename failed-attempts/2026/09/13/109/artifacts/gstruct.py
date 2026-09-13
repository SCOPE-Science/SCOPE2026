import numpy as np, itertools
# Inspect fixed-point structure to find symmetry reduction: print G at z=1.0 real
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)+Em(0,2)
M2 = Em(0,3)+Em(2,0)-Em(3,0)
M1T=M1.T; M2T=M2.T
def solve_dyson_full(z, eps=2e-3, maxit=20000, tol=1e-12):
    M0 = np.diag(np.array([-z,-1,-1,-1],dtype=complex))
    M0s = M0.conj().T
    Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0s,Z]])
    B1=np.block([[Z,M1],[M1T,Z]])
    B2=np.block([[Z,M2],[M2T,Z]])
    d=8
    G = np.linalg.inv(B0 - 1j*eps*np.eye(d))
    for it in range(maxit):
        eta = B1@G@B1 + B2@G@B2
        Gnew = np.linalg.inv(B0 - 1j*eps*np.eye(d) - eta)
        if np.max(np.abs(Gnew-G))<tol:
            G=Gnew; break
        G=Gnew
    return G
np.set_printoptions(precision=4,suppress=True,linewidth=200)
for z in [0.0, 1.5, 0.2j]:
    G=solve_dyson_full(z)
    print(f"===== z={z} =====")
    print("Im G="); print(G.imag)
    print("Re G="); print(G.real)
