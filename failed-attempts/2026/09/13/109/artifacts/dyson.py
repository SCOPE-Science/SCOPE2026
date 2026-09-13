import numpy as np

# Build linearization matrices
# L(z) = M0(z) + M1 s1 + M2 s2, size 4
# M0 = diag(-z,-1,-1,-1)
# M1 = E01+E10+E02
# M2 = E03+E20-E30
N=4
E = lambda i,j: np.eye(N,dtype=complex)[i,:][:,None]*np.eye(N,dtype=complex)[j,:][None,:]
# simpler
def Em(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; return M

M1 = Em(0,1)+Em(1,0)+Em(0,2)
M2 = Em(0,3)+Em(2,0)-Em(3,0)
print("M1=\n",M1)
print("M2=\n",M2)

def Bmats(z):
    M0 = np.diag(np.array([-z,-1,-1,-1],dtype=complex))
    M0s = M0.conj().T
    Z=np.zeros((N,N),dtype=complex)
    B0=np.block([[Z,M0],[M0s,Z]])
    B1=np.block([[Z,M1],[M1.T,Z]])  # M1 real so *=T
    B2=np.block([[Z,M2],[M2.T,Z]])
    return B0,B1,B2

def solve_dyson(z, eps=1e-3, maxit=5000, tol=1e-10):
    B0,B1,B2 = Bmats(z)
    d=8
    G = np.linalg.inv(B0 - 1j*eps*np.eye(d) - np.zeros((d,d)))
    # Actually initial: (B0 - i eps)^-1
    for it in range(maxit):
        eta = B1@G@B1 + B2@G@B2
        Gnew = np.linalg.inv(B0 - 1j*eps*np.eye(d) - eta)
        diff = np.max(np.abs(Gnew-G))
        G=Gnew
        if diff<tol:
            #print(f"converged {it} diff {diff}")
            break
    else:
        print(f"z={z} NOT converged diff={diff}")
    return G

# test at z=0
for z in [0, 1.0, 2.0, 3.0, 4.0, 0.5j, 1j, 0.5+0.5j]:
    G=solve_dyson(z,eps=1e-2)
    # extract top-left block? Brown regularizer: look at Im of something?
    # For support detection, look at density of H_z at 0: rho = (1/pi) Im tr G(i eps)? Actually spectral density at 0 = (1/pi) lim Im tr G?
    # tr Im G?
    rho = np.trace(G.imag)/8/np.pi
    # also look at G structure
    print(f"z={z} rho_H(0)={rho:.4f} G00={G[0,0]:.4f} G44={G[4,4]:.4f}")
