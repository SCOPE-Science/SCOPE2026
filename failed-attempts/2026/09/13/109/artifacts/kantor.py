import numpy as np
# Kantorovich-style certificate: at computed fixed point G*, bound contraction of map
# F(G) = (B0 - i eps - B1 G B1 - B2 G B2)^{-1} on ball. Use operator norm (spectral) bounds.
# DF[H] = F * (B1 H B1 + B2 H B2) * F, so ||DF|| <= ||F||^2 (||B1||^2+||B2||^2) in spectral norm.
# If q<1, unique fixed point in ball and residual bounds distance. Also Im G lower bound persists in ball.
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
def cert(z,eps=2e-3):
    B0,B1,B2=mats(z)
    d=8
    G=np.linalg.inv(B0-1j*eps*np.eye(d))
    for it in range(30000):
        eta=B1@G@B1+B2@G@B2
        Gnew=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)
        if np.max(np.abs(Gnew-G))<1e-12: G=Gnew; break
        G=Gnew
    F=G
    nF=np.linalg.norm(F,2)
    nB1=np.linalg.norm(B1,2); nB2=np.linalg.norm(B2,2)
    q=nF**2*(nB1**2+nB2**2)
    # residual
    eta=B1@G@B1+B2@G@B2
    R=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)-G
    res=np.linalg.norm(R,2)
    rho=np.trace(G.imag)/8/np.pi
    lam_min=np.min(np.linalg.eigvalsh(G.imag))
    print(f"z={z}: rho={rho:.5f} lammin(ImG)={lam_min:.5f} ||F||={nF:.3f} ||B1||={nB1:.3f} ||B2||={nB2:.3f} q={q:.3f} res={res:.1e}")
for z in [0.0,1.0,2.0,3.0,3.2,1.5+0.2j]:
    cert(z)
