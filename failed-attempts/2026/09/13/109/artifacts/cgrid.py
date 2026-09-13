import numpy as np
from fractions import Fraction
# Corrected Dyson: full 2D grid + eps scaling at delicate points + negative-x check
import sys
sys.path.insert(0,"output/artifacts")
# inline (avoid import side effects)
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)-Em(3,2)
M2 = -Em(0,2)+Em(2,0)
M1s=M1.conj().T; M2s=M2.conj().T
def M0m(z):
    M=np.diag(np.array([-z,-1,-1,1],dtype=complex)); M[0,3]=1; return M
def solve_dyson(z, eps=2e-3, maxit=40000, tol=1e-11):
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

eps=2e-3
xs=[0,0.5,1.0,1.5,2.0,2.5,3.0,3.2,3.4,3.6]
ys=[0,0.1,0.2,0.3,0.4,0.6]
print("grid eps=",eps,"(rows y, cols x)")
print("xs=",xs)
for y in ys:
    row=[]
    for x in xs:
        G,_=solve_dyson(x+1j*y,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        row.append(f"{rho:.4f}")
    print(f"y={y:.1f}: "+" ".join(row))
print("negative-x symmetry (corrected pencil need not be symmetric):")
for x in [0.5,1.0,2.0,3.0]:
    a,_=solve_dyson(x,eps=eps); b,_=solve_dyson(-x,eps=eps)
    print(x, f"{np.trace(a.imag)/8/np.pi:.5f}", f"{np.trace(b.imag)/8/np.pi:.5f}")
print("eps-scaling at selected off-real points:")
for z in [1.5+0.2j, 2.0+0.2j, 0.5+0.3j, 3.0+0.1j, 3.2]:
    print(f"z={z}")
    for eps in [8e-3,4e-3,2e-3,1e-3]:
        G,(it,diff)=solve_dyson(z,eps=eps)
        print(f"  eps={eps} rho={np.trace(G.imag)/8/np.pi:.5f} it={it}")
