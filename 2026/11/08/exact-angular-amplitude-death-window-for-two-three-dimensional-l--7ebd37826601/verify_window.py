"""Exact rational cross-checks for a two-vector three-dimensional oscillator stability boundary.

Uses Python standard library only. A finite check is not a proof for all parameters.
"""
from fractions import Fraction as F
from itertools import product


def det(a):
    """Exact Gaussian-elimination determinant over fractions."""
    b = [list(map(F, r)) for r in a]
    d = F(1)
    n = len(b)
    for j in range(n):
        k = next((i for i in range(j, n) if b[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            b[j], b[k] = b[k], b[j]
            d = -d
        pivot = b[j][j]
        d *= pivot
        for i in range(j + 1, n):
            q = b[i][j] / pivot
            for m in range(j + 1, n):
                b[i][m] -= q * b[j][m]
            b[i][j] = 0
    return d


def check_case(K, omega, sin_half, cos_half):
    assert sin_half**2 + cos_half**2 == 1
    h = K / 2
    wc = omega * cos_half
    ws = omega * sin_half
    w1 = [[F(0), -wc, F(0)], [wc, F(0), -ws], [F(0), ws, F(0)]]
    w2 = [[F(0), -wc, F(0)], [wc, F(0), ws], [F(0), -ws, F(0)]]
    m = [[F(0) for _ in range(6)] for _ in range(6)]
    for i in range(3):
        for j in range(3):
            m[i][j] = w1[i][j] + (1 - h if i == j else 0)
            m[i + 3][j + 3] = w2[i][j] + (1 - h if i == j else 0)
        m[i][i + 3] = h
        m[i + 3][i] = h
    # Seven exact evaluations determine a monic degree-six characteristic polynomial.
    for lam in [-3, -2, -1, 0, 1, 2, 3]:
        z = F(lam) - 1
        u, v = sin_half**2, cos_half**2
        p_minus = z**3 + 2*h*z*z + omega**2*z + 2*h*omega**2*v
        p_plus = z**3 + 4*h*z*z + (4*h*h+omega**2)*z + 2*h*omega**2*u
        lhs = det([[(F(lam) if i == j else F(0)) - m[i][j] for j in range(6)] for i in range(6)])
        assert lhs == p_minus * p_plus, (K,omega,u,lam,lhs,p_minus*p_plus)
    # Independent direct Routh-Hurwitz comparisons for both cubic factors.
    u,v = sin_half**2,cos_half**2
    a = 2*h-3; b = 3-4*h+omega**2; c = 2*h-1+(2*h*v-1)*omega**2
    A = 4*h-3; B = 4*h*h-8*h+3+omega**2; C = -(2*h-1)**2+(2*h*u-1)*omega**2
    routh = a>0 and b>0 and c>0 and a*b>c and A>0 and B>0 and C>0 and A*B>C
    ang = K>3 and (K*u-2)*omega**2>2*(K-2)**2 and (K*v-1)*omega**2>1-K
    assert routh == ang, (K,omega,u,routh,ang)
    if K>3 and omega**2>2*K-3:
        L = F(2,K) * (1+(K-2)**2/omega**2)
        U = (K-1)/K * (1+1/omega**2)
        assert ang == (L<u<U)
    return 8


def main():
    rational_angles = [(F(0),F(1)),(F(1),F(0)),(F(3,5),F(4,5)),(F(4,5),F(3,5)),
                       (F(5,13),F(12,13)),(F(12,13),F(5,13)),(F(8,17),F(15,17)),(F(15,17),F(8,17))]
    count=0
    for k in [F(2),F(3),F(31,10),F(4),F(6),F(8),F(10),F(15)]:
        for w in [F(1),F(2),F(3),F(4),F(6),F(8),F(12),F(20)]:
            for s,c in rational_angles:
                count += check_case(k,w,s,c)
    print('PASS:',count,'exact rational checks (7 characteristic values and one Routh equivalence per case)')
    print('NOTE: finite parameter grid is supporting evidence; infinite claim uses analytic proof.')

if __name__=='__main__': main()
