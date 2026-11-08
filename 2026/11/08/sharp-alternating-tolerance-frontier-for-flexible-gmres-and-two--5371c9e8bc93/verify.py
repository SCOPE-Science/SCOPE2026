"""Reproducible finite checks for the alternating inner-tolerance FGMRES theorem.

Requires Python 3 and NumPy. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np


def continuants(a, b, m):
    d = [F(1), F(1)]  # D_{-1}, D_0
    for j in range(1, m + 1):
        mu = a if j % 2 else b
        d.append(d[-1] - mu * mu * d[-2])
    return d


def construct(a, b, steps):
    """Build worst-case FGMRES iterations with A=I and invertible variable maps."""
    n = steps + 2
    e = np.eye(n)
    v = e[:, 0].copy()
    V = [v]
    W = []
    ratios = []
    for j in range(1, steps + 1):
        mu = float(a if j % 2 else b)
        proj = np.zeros(n)
        if W:
            ww = np.column_stack(W)
            proj = ww @ np.linalg.lstsq(ww, v, rcond=None)[0]
        u = v - proj
        q = np.linalg.norm(u)
        if mu >= q - 1e-13:
            # Choose collinear direction. This can stop with nonzero residual.
            w = proj
            assert np.linalg.norm(v - w) <= mu + 1e-12
            assert np.dot(v, w) > 1e-12
            return ratios, j, q
        e_j = e[:, j]
        assert max(abs(np.dot(e_j, vi)) for vi in V) < 1e-10
        w = proj + (q*q - mu*mu)/(q*q)*u + (mu*sqrt(q*q-mu*mu)/q)*e_j
        assert np.isclose(np.linalg.norm(v-w), mu, atol=1e-11)
        assert abs(np.dot(v-w, w)) < 1e-10
        assert np.dot(v, w) > 0
        W.append(w)
        mat = np.column_stack(W)
        least = np.linalg.lstsq(mat, V[0], rcond=None)[0]
        r = V[0] - mat @ least
        ratios.append(float(np.linalg.norm(r)))
        # Orthogonal Arnoldi extension.
        vnext = w - sum(np.dot(w,vi)*vi for vi in V)
        norm = np.linalg.norm(vnext)
        assert norm > 1e-13
        v = vnext/norm
        V.append(v)
    return ratios, None, None


def main():
    # Period-two determinant reduction, exactly over rational numbers.
    count = 0
    for a in [F(1, 10), F(1, 4), F(2, 5), F(3, 5), F(4, 5)]:
        for b in [F(1, 10), F(1, 5), F(2, 5), F(3, 5), F(4, 5)]:
            d = continuants(a, b, 30)
            E0, E1 = F(1), 1-a*a-b*b
            assert d[3] == E1
            for k in range(1, 15):
                if k >= 2:
                    assert d[2*k+1] == E1*d[2*k-1] - a*a*b*b*d[2*k-3]
                assert d[2*k] == d[2*k+1] + b*b*d[2*k-1]
                count += 1
            if a+b == 1:
                for k in range(0, 15):
                    assert d[2*k+1] == (k+1)*(a*b)**k
                    count += 1
            if a+b < 1:
                assert all(t > 0 for t in d)
    trials = 0
    for a, b in [(0.8,0.2), (0.6,0.3), (0.4,0.6), (0.8,0.4), (0.6,0.6), (0.25,0.75)]:
        r, stalled, q = construct(a,b,10)
        d = continuants(F(str(a)), F(str(b)), 10)
        for j, val in enumerate(r,1):
            numerator = float(F(str(a))**((j+1)//2)*F(str(b))**(j//2))
            predicted = numerator / sqrt(float(d[j]))
            assert np.isclose(val, predicted, rtol=2e-10, atol=2e-10), (a,b,j,val,predicted)
            trials += 1
        if a+b>1:
            assert stalled is not None
        else:
            assert stalled is None
    assert abs((0.8*0.4/sqrt(1-0.8**2))-8/15)<1e-12
    print(f'VERIFY_OK {count} rational continuant identities; {trials} sharp FGMRES residuals; finite breakdown tests')

if __name__ == '__main__': main()
