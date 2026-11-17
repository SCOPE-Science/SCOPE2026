"""Supplementary high-precision principal-section eigenvalue checks.

Requires mpmath, numpy, scipy. Finite checks are not proofs of infinite limits.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from mpmath import mp


def largest_continuant(edges, precision=160):
    mp.dps = precision
    ed = np.asarray([float(x) for x in edges], dtype=float)
    n = len(ed) + 1
    guess = float(eigh_tridiagonal(np.zeros(n), ed, eigvals_only=True,
                                   select='i', select_range=(n-1, n-1))[0])
    def polynomial(z):
        p0, p1 = mp.mpf(1), z
        for edge in edges:
            p0, p1 = p1, z*p1 - edge*edge*p0
        return p1
    return mp.findroot(polynomial, (mp.mpf(guess)*(1-mp.mpf('1e-6')),
                                       mp.mpf(guess)*(1+mp.mpf('1e-6'))),
                       solver='secant', verify=True, maxsteps=90)


def normalized_green_data(eigenvalue, edges):
    length = len(edges)
    green = [mp.mpf(0)]*(length+1)
    green[length] = 1/eigenvalue
    for j in range(length-1, 0, -1):
        green[j] = 1/(eigenvalue - edges[j]**2*green[j+1])
    coordinates = [mp.mpf(1)]
    for j in range(1, length+1):
        coordinates.append(coordinates[-1]*edges[j-1]*green[j])
    root_norm = mp.sqrt(sum(x*x for x in coordinates))
    return green, 1/root_norm


def verify(q_str, s_str, t_str, indices, minimum):
    mp.dps = 170
    q, s, t = [mp.mpf(x) for x in (q_str, s_str, t_str)]
    coeff = [mp.mpf(1), s, mp.mpf(1), t]
    edges = [coeff[j % 4]*q**j/2 for j in range(65)]
    lam = largest_continuant(edges, 170)
    green, psi0 = normalized_green_data(lam, edges)
    product = mp.mpf(1)
    for j in range(1, len(edges)+1):
        product *= lam*green[j]
    constant = psi0*product
    assert constant > 0
    for N in indices:
        finite = largest_continuant(edges[:N], 170)
        gap = lam-finite
        assert gap > 0
        predicted = constant**2 * lam
        for j in range(N+1):
            predicted *= (edges[j]/lam)**2
        ratio = gap/predicted
        assert abs(ratio-1) < mp.mpf(minimum), (q_str,s_str,t_str,N,mp.nstr(ratio,12))
        assert abs((mp.log(gap)/(N*N))-mp.log(q)) < mp.mpf('1.5')
    print('PASS:', q_str, s_str, t_str, 'cases=', len(indices))

if __name__ == '__main__':
    verify('0.65', '1.4', '0.7', [12, 13, 15, 18, 20], '0.002')
    verify('0.82', '0.8', '1.6', [18, 20, 22, 24], '0.02')
    verify('0.5', '2.0', '1.0', [10, 12, 14, 18, 20], '0.005')
    print('PASS: all finite diagnostics; asymptotic proof is analytical.')
