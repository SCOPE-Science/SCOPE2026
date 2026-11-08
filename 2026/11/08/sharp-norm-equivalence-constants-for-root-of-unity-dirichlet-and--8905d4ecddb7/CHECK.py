"""Finite, reproducible checks of an exact two-norm comparison theorem.

These checks are consistency tests, not substitutes for the infinite-dimensional
Jacobi spectral proof supplied in RESULT.md.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import eigh


def gram_plus(m, degree):
    """Direct coefficient calculation from (I-S*^m)f+ = (I+S*^m)f."""
    n = degree + 1
    h = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    plus = []
    for j in range(n):
        col = [0] * n
        col[j] = 1
        for k in range(j - m, -1, -m):
            col[k] = 2
        plus.append(col)
    for i in range(n):
        for j in range(n):
            h[i][j] += sum(plus[i][k] * plus[j][k] for k in range(n))
    return h


def gram_dirichlet(m, degree):
    """Average local difference quotient Gram over the m-th roots of unity."""
    n = degree + 1
    return [[Fraction(int(i == j)) +
             (Fraction(min(i, j)) if (i-j) % m == 0 else Fraction(0))
             for j in range(n)] for i in range(n)]


def form_from_tails(m, r, t):
    h = 2 * abs(t[0])**2 + 4 * sum(abs(v)**2 for v in t[1:])
    diffs = [t[i] - (t[i+1] if i+1 < len(t) else 0) for i in range(len(t))]
    d = r * abs(t[0])**2 + m * sum(abs(v)**2 for v in t[1:]) + sum(abs(v)**2 for v in diffs)
    return h, d


def bounds(m):
    lower = (m + 2 - math.sqrt(m*m + 4)) / 4
    upper = 1.25 if m == 1 else (m + 2 + math.sqrt((m-2)**2+4)) / 4
    return lower, upper


def section_matrices(m, r, n):
    h = np.diag([2.0] + [4.0]*(n-1))
    d = np.diag([float(r+1)] + [float(m+2)]*(n-1))
    for j in range(n-1):
        d[j,j+1] = d[j+1,j] = -1.0
    return d, h


def run():
    checks=0
    for m in range(1,11):
        low, high = bounds(m)
        for d in range(0,17):
            h=gram_plus(m,d)
            q=gram_dirichlet(m,d)
            for i in range(d+1):
                for j in range(d+1):
                    expected=(4*min(i//m,j//m)+2 if i%m==j%m else 0)
                    assert h[i][j] == expected
                    expected_d=Fraction(int(i==j))+(Fraction(min(i,j)) if (i-j)%m==0 else Fraction(0))
                    assert q[i][j] == expected_d
                    checks+=2
        for r in range(m):
            for n in (4, 12, 40, 90):
                dmat,hmat=section_matrices(m,r,n)
                lam=eigh(dmat,hmat,eigvals_only=True)
                assert lam[0]>low-1e-9 and lam[-1]<high+1e-9
                checks+=2
                v=np.array([complex(math.cos(j+1), math.sin(2*j+1)) for j in range(n)])
                h_form,d_form=form_from_tails(m,r,v)
                assert abs((v.conj()@hmat@v).real-h_form)<1e-8
                assert abs((v.conj()@dmat@v).real-d_form)<1e-8
                checks+=2
        qlow=(math.sqrt(m*m+4)-m)/2
        l=(1-qlow)/2
        assert abs(l-low)<1e-12
        checks+=1
        if m>=3:
            qhigh=((m-2)-math.sqrt((m-2)**2+4))/2
            assert -1<qhigh<0
            assert abs((m-qhigh)/2-high)<1e-12
            checks+=2
        # Check a finite truncation of the positive outlier eigenvector.
        n=120
        t=np.array([qlow**j for j in range(n)])
        h,d=form_from_tails(m,0,t)
        assert abs(d/h-low)<1e-7
        checks+=1
    print('PASS:',checks,'exact/finite consistency checks')

if __name__=='__main__':
    run()
