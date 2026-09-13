import numpy as np
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)+Em(0,2)
M2 = Em(0,3)+Em(2,0)-Em(3,0)
def Bmats(z):
    M0 = np.diag(np.array([-z,-1,-1,-1],dtype=complex))
    M0s = M0.conj().T
    Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0s,Z]])
    B1=np.block([[Z,M1],[M1.T,Z]])
    B2=np.block([[Z,M2],[M2.T,Z]])
    return B0,B1,B2
def solve_dyson(z, eps=1e-3, maxit=8000, tol=1e-12):
    B0,B1,B2 = Bmats(z)
    d=8
    G = np.linalg.inv(B0 - 1j*eps*np.eye(d))
    for it in range(maxit):
        eta = B1@G@B1 + B2@G@B2
        Gnew = np.linalg.inv(B0 - 1j*eps*np.eye(d) - eta)
        diff = np.max(np.abs(Gnew-G))
        G=Gnew
        if diff<tol:
            break
    else:
        print(f"z={z} NOT converged diff={diff}")
    return G

for eps in [1e-2, 3e-3, 1e-3]:
    print(f"=== eps={eps} ===")
    for x in [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]:
        G=solve_dyson(x,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        print(f"x={x:.1f} rho={rho:.5f}")
    print("--- imag axis z=iy ---")
    for y in [0,0.2,0.4,0.6,0.8,1.0,1.5,2.0]:
        G=solve_dyson(1j*y,eps=eps)
        rho=np.trace(G.imag)/8/np.pi
        print(f"y={y:.1f} rho={rho:.5f}")
