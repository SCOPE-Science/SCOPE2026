import numpy as np
# High-resolution real-axis scan to locate edges and check for interior gaps (corrected pencil)
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)-Em(3,2)
M2 = -Em(0,2)+Em(2,0)
M1s=M1.conj().T; M2s=M2.conj().T
def M0m(z):
    M=np.diag(np.array([-z,-1,-1,1],dtype=complex)); M[0,3]=1; return M
def solve_dyson(z, eps=2e-3, maxit=60000, tol=1e-11):
    M0=M0m(z); Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0.conj().T,Z]])
    B1=np.block([[Z,M1],[M1s,Z]])
    B2=np.block([[Z,M2],[M2s,Z]])
    d=8
    G=np.linalg.inv(B0-1j*eps*np.eye(d))
    for it in range(maxit):
        eta=B1@G@B1+B2@G@B2
        Gnew=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)
        diff=np.max(np.abs(Gnew-G)); G=Gnew
        if diff<tol: break
    return G,(it,diff)
import numpy as np
for eps in [2e-3,1e-3]:
    print(f"eps={eps} positive axis")
    xs=np.linspace(0,3.8,20)
    for x in xs:
        G,_=solve_dyson(x,eps=eps)
        print(f"{x:.3f} {np.trace(G.imag)/8/np.pi:.5f}")
    print(f"eps={eps} negative axis")
    for x in xs:
        G,_=solve_dyson(-x,eps=eps)
        print(f"{-x:.3f} {np.trace(G.imag)/8/np.pi:.5f}")
