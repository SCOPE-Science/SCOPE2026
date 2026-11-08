"""Numerical independent operator-frame checks for sparse multi-window Gabor tomography.

Requires Python 3 and NumPy. All results are supplementary finite checks.
"""
import numpy as np


def design_windows(N, p=0.5, phi=np.pi/4, random_phases=False):
    m = N // 2
    windows = []
    for d in range(1, m + 1):
        h = np.zeros(N, dtype=complex)
        if N % 2 == 0 and d == m:
            h[0], h[d] = np.sqrt(p), np.sqrt(1-p) * np.exp(1j * phi)
        else:
            phase = 0.37 * d if random_phases else 0.0
            h[0], h[d] = 1 / np.sqrt(2), np.exp(1j * phase) / np.sqrt(2)
        windows.append(h)
    return windows


def measurement_gram(N, windows):
    # Independent direct real Hilbert-Schmidt orthonormal basis of Hermitian matrices.
    basis = []
    for j in range(N):
        h = np.zeros((N, N), complex)
        h[j, j] = 1.0
        basis.append(h)
    for j in range(N):
        for k in range(j+1, N):
            h = np.zeros((N, N), complex)
            h[j, k] = h[k, j] = 1/np.sqrt(2)
            basis.append(h)
            h = np.zeros((N, N), complex)
            h[j, k], h[k, j] = 1j/np.sqrt(2), -1j/np.sqrt(2)
            basis.append(h)
    # Each projector is rank-one; vectorize basis and projector to compute trace.
    B = np.stack([x.T.reshape(-1) for x in basis], axis=1)
    rows = []
    sites = np.arange(N)
    for g in windows:
        for s in range(N):
            rolled = np.roll(g,s)
            for k in range(N):
                v = rolled * np.exp(2j*np.pi*k*sites/N)
                P = np.outer(v, v.conj())
                rows.append(np.real(P.reshape(-1) @ B))
    Y = np.array(rows)
    return np.linalg.eigvalsh(Y.T@Y)


def expected_spectrum(N,p=0.5,phi=np.pi/4):
    m=N//2
    if N%2:
        return np.sort(np.array([N*m]+[N*(N-2)/4]*(N-1)+[N/4]*(N*(N-1))))
    return np.sort(np.array(
        [N*m] + [N*m/2]*(m-1)
        + [N*((m-1)/2+(2*p-1)**2)]*m
        + [N/4]*(N*(N-2))
        + [4*N*p*(1-p)*np.cos(phi)**2]*m
        + [4*N*p*(1-p)*np.sin(phi)**2]*m
    ))


def main():
    cases=0
    for N in range(3,11):
        parameters=[(0.5,np.pi/4,False), (0.5,np.pi/3,True)]
        if N%2==0:
            parameters += [(0.25,np.pi/4,True), (0.15,np.pi/4,False)]
        for p,phi,random_phases in parameters:
            eig=measurement_gram(N,design_windows(N,p,phi,random_phases))
            pred=expected_spectrum(N,p,phi)
            assert eig.shape==pred.shape==(N*N,)
            assert np.allclose(eig,pred,rtol=1e-9,atol=2e-9), (N,p,phi,np.max(abs(eig-pred)))
            assert abs(eig[-1]-N*(N//2)) < 1e-8
            cases+=1
        good=measurement_gram(N,design_windows(N))
        assert abs(good[0]-N/4)<1e-8
        assert abs(good[-1]/good[0]-4*(N//2))<1e-8
        cases+=1
    print('CHECKS_PASS: direct_operator_frame_spectra',cases,'dimensions',list(range(3,11)))

if __name__ == '__main__':
    main()
