import numpy as np
N=4
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M
M1 = Em(0,1)+Em(1,0)+Em(0,2)
M2 = Em(0,3)+Em(2,0)-Em(3,0)
M1T = M1.T
M2T = M2.T
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
    return G, (it,diff)

if __name__=="__main__":
    # coarse 2D grid
    xs = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.2,3.4,3.6]
    ys = [0,0.1,0.2,0.3,0.4,0.6,0.8]
    eps=2e-3
    print("grid eps=",eps)
    for y in ys:
        row=[]
        for x in xs:
            G,info=solve_dyson(x+1j*y,eps=eps)
            rho=np.trace(G.imag)/8/np.pi
            row.append(f"{rho:.4f}")
        print(f"y={y:.1f}: "+" ".join(row))
    print("xs=",xs)
