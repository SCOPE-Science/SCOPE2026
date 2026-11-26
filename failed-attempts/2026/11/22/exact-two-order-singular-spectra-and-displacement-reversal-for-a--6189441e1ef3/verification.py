"""Finite diagnostics for affine Fock composition cross-products.

Requires NumPy. Finite sections illustrate the theorem but do not prove the
infinite-dimensional singular-value formulas.
"""
import math
import random
import numpy as np


def composition_matrix(a, b, cutoff):
    """Analytic Fock basis e_n(z) = z**n/sqrt(n!)."""
    out = np.zeros((cutoff, cutoff), dtype=np.complex128)
    for n in range(cutoff):
        for k in range(n + 1):
            logc = (math.lgamma(n + 1) - math.lgamma(k + 1)) / 2
            logc -= math.lgamma(n - k + 1)
            out[k, n] = a**k * b**(n-k) * math.exp(logc)
    return out


def constants(a, b, c, d):
    q = a * c.conjugate()
    delta = 1.0 - abs(q)**2
    LP = (b * d.conjugate()).real + abs(b*c)**2 / 2
    LP += abs(a*d.conjugate() + q*(b*c.conjugate()).conjugate())**2 / (2*delta)
    LR = abs(b)**2/2 + abs(d.conjugate() + q*b.conjugate())**2/(2*delta)
    quadratic = ((1-abs(c)**2)*abs(b)**2 + (1-abs(a)**2)*abs(d)**2
                 - 2*((1-q.conjugate())*b*d.conjugate()).real)/(2*delta)
    return q, LP, LR, quadratic


def run():
    rng = random.Random(20261115)
    assertions = 0
    examples = [(0.4, 0.2, 0.7, 0.3),
                (0.4+0.2j, 0.5-0.2j, 0.6-0.2j, 0.3+0.25j),
                (0.5, 1, 0.5, 2),
                (0.9, 0.5, 0, 1),
                (0.5, 0, 0.7, 0.4),
                (0.5, 1+0.3j, 0.5, 1+0.3j)]
    for a,b,c,d in examples:
        q, LP, LR, Q = constants(a,b,c,d)
        assert abs(LR-LP-Q) < 1e-11
        assertions += 1
        mat_a,mat_c=composition_matrix(a,b,80),composition_matrix(c,d,80)
        P=mat_a @ mat_c.conj().T
        R=mat_c.conj().T @ mat_a
        for matrix, logconstant in ((P,LP),(R,LR)):
            sv = np.linalg.svd(matrix,compute_uv=False)
            for n in range(5):
                prediction = math.exp(logconstant)*abs(q)**n
                assert abs(sv[n]-prediction) < 1e-8 * max(1.0,prediction), (a,b,c,d,n,sv[n],prediction)
                assertions += 1
    for _ in range(100):
        a=(rng.random()-0.5)*1.2 + 1j*(rng.random()-0.5)*1.2
        c=(rng.random()-0.5)*1.2 + 1j*(rng.random()-0.5)*1.2
        b=(rng.random()-0.5)*2 + 1j*(rng.random()-0.5)*2
        d=(rng.random()-0.5)*2 + 1j*(rng.random()-0.5)*2
        _, LP, LR, Q=constants(a,b,c,d)
        assert abs(LR-LP-Q) < 1e-11
        assertions += 1
    print(f'PASS: {assertions} finite coefficient/SVD/quadratic assertions')

if __name__=='__main__':
    run()
