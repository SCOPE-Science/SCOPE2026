import numpy as np
# CORRECTED linearization:
# L = M0 + M1 s1 + M2 s2, 4x4, non-selfadjoint:
# M0: diag(-z,-1,-1,1) + E03 (i.e. (0,3)=1)
# M1: E01+E10 - E32
# M2: -E02 + E20
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)-Em(3,2)
M2 = -Em(0,2)+Em(2,0)
def M0m(z):
    M=np.diag(np.array([-z,-1,-1,1],dtype=complex)); M[0,3]=1; return M
# verify Schur numerically with random scalars (commuting test): Schur should equal -z+s1^2-s2^2+s1s2
rng=np.random.default_rng(0)
for t in range(5):
    s1,s2=rng.normal(),rng.normal(); z=rng.normal()
    L=M0m(z)+M1*s1+M2*s2
    A=L[0,0]; B=L[0,1:]; C=L[1:,0]; D=L[1:,1:]
    S=A-B@np.linalg.inv(D)@C
    target=-z+s1**2-s2**2+s1*s2
    print(S, target, abs(S-target))
# Hermitization: H = [[0,L],[L*,0]], Dyson with B0,B1,B2 where Bi=[[0,Mi],[Mi*,0]]
def Bmats(z):
    M0=M0m(z)
    Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0.conj().T,Z]])
    B1=np.block([[Z,M1],[M1.conj().T,Z]])
    B2=np.block([[Z,M2],[M2.conj().T,Z]])
    return B0,B1,B2
def solve_dyson(z, eps=2e-3, maxit=30000, tol=1e-11):
    B0,B1,B2=Bmats(z)
    d=8
    G=np.linalg.inv(B0-1j*eps*np.eye(d))
    for it in range(maxit):
        eta=B1@G@B1+B2@G@B2
        Gnew=np.linalg.inv(B0-1j*eps*np.eye(d)-eta)
        diff=np.max(np.abs(Gnew-G)); G=Gnew
        if diff<tol: break
    return G,(it,diff)
print("=== corrected Dyson scan ===")
for eps in [8e-3,4e-3,2e-3,1e-3]:
    print(f"--- eps={eps} ---")
    for x in [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]:
        G,(it,diff)=solve_dyson(x,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        print(f"x={x:.1f} rho={rho:.5f} it={it}")
    print("imag:")
    for y in [0,0.2,0.4,0.6,1.0]:
        G,(it,diff)=solve_dyson(1j*y,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        print(f"y={y:.1f} rho={rho:.5f} it={it}")
