import numpy as np
# Better certificate: stability operator L = I - C where C[H]=F*(B1 H B1+B2 H B2)*F restricted to Hermitian matrices.
# Compute spectral radius of C numerically (16x16? 8x8 Hermitian = 64 real dims). If rho(C)<1, fixed point is stable/isolated.
# Also compute derivative w.r.t. z to propagate lower bounds along spine.
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)-Em(3,2)
M2 = -Em(0,2)+Em(2,0)
M1s=M1.conj().T; M2s=M2.conj().T
def M0m(z):
    M=np.diag(np.array([-z,-1,-1,1],dtype=complex)); M[0,3]=1; return M
def mats(z):
    M0=M0m(z); Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0.conj().T,Z]])
    B1=np.block([[Z,M1],[M1s,Z]])
    B2=np.block([[Z,M2],[M2s,Z]])
    return B0,B1,B2
def solve(z,eps=2e-3):
    B0,B1,B2=mats(z); d=8
    G=np.linalg.inv(B0-1j*eps*np.eye(d))
    for it in range(30000):
        eta=B1@G@B1+B2@G@B2
        Gnew=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)
        if np.max(np.abs(Gnew-G))<1e-12: G=Gnew; break
        G=Gnew
    return G,(B0,B1,B2)
def stab_radius(z,eps=2e-3):
    G,(B0,B1,B2)=solve(z,eps)
    d=8
    # Hermitian basis E_k (64)
    basis=[]
    for i in range(d):
        E=np.zeros((d,d),dtype=complex); E[i,i]=1; basis.append(E)
    for i in range(d):
        for j in range(i+1,d):
            E=np.zeros((d,d),dtype=complex); E[i,j]=E[j,i]=1/np.sqrt(2); basis.append(E)
            F=np.zeros((d,d),dtype=complex); F[i,j]=1j/np.sqrt(2); F[j,i]=-1j/np.sqrt(2); basis.append(F)
    m=len(basis)
    C=np.zeros((m,m),dtype=complex)
    for a,Ea in enumerate(basis):
        T=G@(B1@Ea@B1+B2@Ea@B2)@G
        # project onto Hermitian basis (Frobenius inner product)
        for b,Eb in enumerate(basis):
            C[b,a]=np.trace(Eb.conj().T@T)
    ev=np.linalg.eigvals(C)
    r=np.max(np.abs(ev))
    rho=np.trace(G.imag)/8/np.pi
    return r,rho,ev
for z in [0.0,1.0,2.0,3.0,3.2]:
    r,rho,ev=stab_radius(z)
    print(f"z={z}: rho={rho:.5f} stab_radius={r:.4f}")
