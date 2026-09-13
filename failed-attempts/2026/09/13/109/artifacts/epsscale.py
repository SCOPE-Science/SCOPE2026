import numpy as np
# Stability check of Dyson: eps-scaling at key points, and larger grid incl negative x and y edge
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)+Em(0,2)
M2 = Em(0,3)+Em(2,0)-Em(3,0)
M1T=M1.T; M2T=M2.T
def solve_dyson(z, eps=1e-3, maxit=20000, tol=1e-11):
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
        diff = np.max(np.abs(Gnew-G))
        G=Gnew
        if diff<tol:
            break
    return G,(it,diff)

# eps scaling at representative points
for z in [0.0, 3.0, 3.4, 0.3j, 0.4, 1.5+0.3j]:
    print(f"z={z}")
    for eps in [8e-3,4e-3,2e-3,1e-3,5e-4]:
        G,(it,diff)=solve_dyson(z,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        print(f"  eps={eps:.4f} rho={rho:.5f} it={it} diff={diff:.1e} G00_im={G[0,0].imag:.4f}")
# negative x symmetry
print("symmetry check")
for x in [1.0,2.0,3.0]:
    for eps in [2e-3]:
        Ga,_=solve_dyson(x,eps=eps); Gb,_=solve_dyson(-x,eps=eps)
        print(x, np.trace(Ga.imag)/8/np.pi, np.trace(Gb.imag)/8/np.pi)
