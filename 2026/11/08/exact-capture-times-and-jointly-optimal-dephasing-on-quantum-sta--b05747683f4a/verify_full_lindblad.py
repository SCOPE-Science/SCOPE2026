"""Direct full-density-matrix Liouvillian cross-check on finite star networks.
Requires numpy and scipy. Constructs the (m+1)^2 generator without reducing by symmetry.
"""
import numpy as np
from scipy.linalg import solve


def quantum_lifetime(m, j, gamma, kappa, initial):
    n = m + 1
    h = np.zeros((n,n), dtype=complex)
    for z in range(1, n):
        h[0,z] = h[z,0] = j
    eye = np.eye(n)
    sink = np.zeros((n,n), dtype=complex); sink[0,0] = kappa
    gen = -1j*(np.kron(eye,h)-np.kron(h.T,eye))
    gen -= (np.kron(eye,sink)+np.kron(sink.T,eye))/2
    for z in range(n):
        pr = np.zeros((n,n), dtype=complex); pr[z,z] = 1
        gen += gamma*(np.kron(pr.T,pr)-0.5*(np.kron(eye,pr)+np.kron(pr.T,eye)))
    rho = np.zeros((n,n), dtype=complex); rho[initial,initial] = 1
    integrated = solve(-gen, rho.reshape(-1,order='F')).reshape((n,n),order='F')
    assert np.max(np.abs(integrated-integrated.conjugate().T)) < 1e-9
    return np.trace(integrated).real


def main():
    nchecked=0
    for m in (2,3,4,6,9):
        for j, gamma, kappa in ((1.3,0.2,0.7),(0.8,1.5,4.1),(-2.1,3.4,1.2)):
            leaf = quantum_lifetime(m,j,gamma,kappa,1)
            theoretical=(m+1)/kappa+(m-1)/gamma+(gamma+kappa/2)/(2*j*j)
            assert abs(leaf-theoretical)<1e-8, (leaf,theoretical)
            hub=quantum_lifetime(m,j,gamma,kappa,0)
            assert abs(hub-(m+1)/kappa)<1e-8,(hub,m,kappa)
            nchecked += 2
    print('FULL_LINDBLAD_OK',nchecked,'initial-state/parameter cases')

if __name__ == '__main__':
    main()
