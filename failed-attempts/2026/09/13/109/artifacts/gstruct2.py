import numpy as np
# Exact solution at z=0 via symmetry ansatz + verify; then closed-form rho(0).
# From gstruct-like print for corrected pencil, inspect pattern first.
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)-Em(3,2)
M2 = -Em(0,2)+Em(2,0)
M1s=M1.conj().T; M2s=M2.conj().T
def M0m(z):
    M=np.diag(np.array([-z,-1,-1,1],dtype=complex)); M[0,3]=1; return M
def solve(z,eps=2e-3):
    M0=M0m(z); Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0.conj().T,Z]])
    B1=np.block([[Z,M1],[M1s,Z]])
    B2=np.block([[Z,M2],[M2s,Z]])
    d=8
    G=np.linalg.inv(B0-1j*eps*np.eye(d))
    for it in range(30000):
        eta=B1@G@B1+B2@G@B2
        Gnew=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)
        if np.max(np.abs(Gnew-G))<1e-12: G=Gnew; break
        G=Gnew
    return G
np.set_printoptions(precision=4,suppress=True,linewidth=250)
G=solve(0.0)
print("Im G at z=0:"); print(G.imag)
print("Re G at z=0:"); print(G.real)
