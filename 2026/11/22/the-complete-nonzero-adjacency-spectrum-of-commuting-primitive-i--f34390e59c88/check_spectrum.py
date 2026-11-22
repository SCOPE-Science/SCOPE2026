"""Independent finite-prime checks of the point-hyperplane antiflag adjacency spectrum.

Usage: python check_spectrum.py.  Requires Python 3 and NumPy.
The theorem itself applies to prime-power fields; this checker tests prime fields.
"""
from itertools import product
import math
import numpy as np


def projective_representatives(n, q):
    reps = []
    for x in product(range(q), repeat=n):
        if not any(x):
            continue
        first = next(a for a in x if a)
        inv = pow(first, -1, q)
        y = tuple(inv * a % q for a in x)
        if y not in reps:
            reps.append(y)
    return reps


def adjacency(n, q):
    points = projective_representatives(n, q)
    incidence = np.array([[sum(a*b for a,b in zip(p,h)) % q == 0
                           for h in points] for p in points], dtype=bool)
    verts = [(p,h) for p in range(len(points)) for h in range(len(points))
             if not incidence[p,h]]
    count = len(verts)
    A = np.empty((count, count), dtype=np.float64)
    for i, (p,h) in enumerate(verts):
        for j, (r,k) in enumerate(verts):
            A[i,j] = 1.0 if incidence[p,k] and incidence[r,h] else 0.0
    assert np.array_equal(A, A.T)
    assert np.all(np.diag(A) == 0)
    return A


def expected(n, q):
    t = (q**(n-1)-1)//(q-1)
    s = (q**(n-2)-1)//(q-1)
    v = (q**n-1)//(q-1)
    g = q**(n-2)
    beta = q**(n-3)
    k = g*t
    alpha = q**(3*(n-2)/2)
    m_beta = q**3*t*s//(q+1)
    assert m_beta*(q+1) == q**3*t*s
    m_plus = (q-2)*t*v//2
    assert 2*m_plus == (q-2)*t*v
    m_minus = q*(q-1)*t*v//(2*(q+1))
    assert 2*(q+1)*m_minus == q*(q-1)*t*v
    entries = [(float(-alpha), v-1), (-float(g), m_minus),
               (float(beta), m_beta), (float(g), m_plus),
               (float(alpha), v-1), (float(k), 1)]
    return sorted((value, mult) for value, mult in entries if mult)


def check(n, q):
    A = adjacency(n,q)
    exp = expected(n,q)
    assert sum(mult for _, mult in exp) == A.shape[0]
    vals = np.linalg.eigvalsh(A)
    model = np.array([val for val, mult in exp for _ in range(mult)])
    assert vals.shape == model.shape
    max_err = float(np.max(np.abs(vals-model)))
    assert np.allclose(vals,model,atol=3e-7,rtol=0), (n,q,max_err)
    assert np.all(A.sum(axis=1) == expected_degree(n,q))
    print(f'PASS n={n} q={q} vertices={A.shape[0]} '
          f'max_abs_eigenvalue_error={max_err:.3e} '
          f'nonzero_eigenvalues={len(exp)}')


def expected_degree(n,q):
    return q**(n-2)*(q**(n-1)-1)//(q-1)


if __name__ == '__main__':
    for n,q in [(4,2),(4,3),(5,2)]:
        check(n,q)
    print('PASS all three tested graph spectra and degree sequences')
