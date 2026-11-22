"""Independent Fourier-collocation checks for asymmetric flashing sine diffusion.

Run: python CHECK.py
Requires: numpy; sympy is optional (symbolic checks are native arithmetic).
Finite-grid checks support, but do not replace, the perturbative proof.
"""
import math
import numpy as np


def predicted_coefficient(q, r, D=1.0, k=1.0):
    a = D*k*k
    z = r/a
    return q/(2*a)*(-q+(1-q)*(z-1)/(z+1)**2)


def collocation(eps, q, r, D=1.0, k=1.0, N=64):
    assert 0 < q < 1 and r > 0 and D > 0 and k > 0 and N % 2 == 0
    grid = 2*math.pi*np.arange(N)/(N*k)
    basis = np.fft.fft(np.eye(N), axis=0)
    wavenumbers = np.fft.fftfreq(N, d=1/N)*k
    derivative = np.fft.ifft(1j*wavenumbers[:, None]*basis, axis=0).real
    laplacian = np.fft.ifft(-(wavenumbers**2)[:, None]*basis, axis=0).real
    switch = r*np.array([[-q, 1-q], [q, -(1-q)]])
    # Backward generator on two on/off states, ordered (off,on).
    backward = (np.kron(np.eye(2), D*laplacian) +
                np.kron(np.diag([0.0, eps]), np.diag(np.sin(k*grid))@derivative) +
                np.kron(switch.T, np.eye(N)))
    # Stationary state probabilities are discrete masses, summing to 1.
    matrix = backward.T.copy()
    rhs = np.zeros(2*N)
    matrix[0, :] = 1.0
    rhs[0] = 1.0
    stationary = np.linalg.solve(matrix, rhs)
    forcing = np.r_[np.zeros(N), eps*np.sin(k*grid)]
    mean_drift = np.dot(stationary, forcing)
    forcing = forcing - mean_drift
    matrix = -backward.copy()
    matrix[0, :] = stationary
    forcing[0] = 0.0
    corrector = np.linalg.solve(matrix, forcing).reshape(2, N)
    dx_corrector = (derivative@corrector.T).T
    jump = (corrector[1] - corrector[0])**2
    weights = stationary.reshape(2,N)
    effective_diffusivity = (D*np.sum(weights*(1+dx_corrector)**2)
        +r/2*np.sum((q*weights[0]+(1-q)*weights[1])*jump))
    return effective_diffusivity, mean_drift


def check():
    cases = [(0.05,3), (0.05,10), (0.05,0.3), (0.2,3), (1/9,3), (0.5,3)]
    comparisons = 0
    for q,r in cases:
        prev_error = None
        for e in [0.10,0.05,0.025]:
            empirical, drift = collocation(e, q, r)
            coefficient = predicted_coefficient(q, r)
            error = abs((empirical-1)/e**2-coefficient)
            # Fourth-order remainder entails e**2 errors after division.
            assert error < 0.0003, (q,r,e,error)
            assert abs(drift) < 1e-10
            if prev_error is not None and abs(coefficient)>1e-8:
                assert error < prev_error/3.3 + 2e-8, (q,r,e,error,prev_error)
            prev_error = error
            comparisons += 1
    for q in (0.03,0.05,0.1):
        roots = [(1-3*q+sign*math.sqrt((1-q)*(1-9*q)))/(2*q) for sign in (-1,1)]
        assert roots[0] < 3 < roots[1]
        assert predicted_coefficient(q,roots[0]) == 0 or abs(predicted_coefficient(q,roots[0]))<2e-16
        assert predicted_coefficient(q,3)>0
        assert predicted_coefficient(q,roots[1]) == 0 or abs(predicted_coefficient(q,roots[1]))<2e-16
        comparisons += 3
    for q in (0.12,0.2,0.5):
        for r in (.01,.3,1,3,10,100):
            assert predicted_coefficient(q,r)<0
            comparisons += 1
    print('PASS:', comparisons, 'independent numerical and algebraic cases')


if __name__ == '__main__':
    check()
