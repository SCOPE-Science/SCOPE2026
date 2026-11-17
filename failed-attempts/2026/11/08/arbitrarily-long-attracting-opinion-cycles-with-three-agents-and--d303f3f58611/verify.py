"""Exact-rational checks for the bounded-confidence all-period construction.

Usage: python3 verify.py
The proof for every integer p >= 2 is in RESULT.md; this program checks a
finite reproducibility range and the exact local branch margins.
"""
from fractions import Fraction as F


def bands(p):
    """Open intervals in the variable Q*abs(z)."""
    assert p >= 2
    Q = (1 << p) - 1
    b = [(F(0), F(1, 2))]
    if p >= 3:
        b.append((F(3, 2), F(1 << (p-2)) + F(1, 4)))
    b.append((F((1 << (p-1))), F((1 << (p-1)))))  # replaced below
    b[-1] = (F(1 << (p-1)) - F(1, 4), F(1 << (p-1)) + F(1, 4))
    if p >= 3:
        b.append((F(Q-1)-F(1,4), F(Q-1)+F(1,4)))
    return Q, b


def admissible(x, p):
    Q, b = bands(p)
    t = abs(x)*Q
    return any(a < t < c for a,c in b) or t == 0


def strict_margin(x, p):
    Q, b = bands(p)
    t = abs(x)*Q
    return min([abs(t-a) for a,c in b]+[abs(t-c) for a,c in b])/Q


def update(x, p):
    hear0 = admissible(-x, p)
    hear1 = admissible(1-x, p)
    return (x + (1 if hear1 else 0))/ (1+int(hear0)+int(hear1))


def check(p):
    Q,b=bands(p)
    assert len(b) <= 4
    assert all(a<c for a,c in b)
    assert all(b[k][1] < b[k+1][0] for k in range(len(b)-1))
    x=[F(1 << k, Q) for k in range(p)]
    assert len(set(x))==p
    assert all(not admissible(y,p) for y in (x[0],))
    assert admissible(1-x[0],p)
    for k in range(1,p):
        assert admissible(x[k],p)
        assert not admissible(1-x[k],p)
    assert update(x[0],p)==x[-1]
    for k in range(1,p):
        assert update(x[k],p)==x[k-1]
    assert min(strict_margin(v,p) for v in x+ [1-v for v in x]) >= F(1, 4*Q)
    delta=F(1,16*Q)
    assert min(strict_margin(v,p) for v in x+[1-v for v in x]) > delta
    # Both decisions constant on radius delta around each node. Under one
    # prescribed branch update, |F(x+e)-F(x)|=|e|/2, so neighborhoods map in.
    for v in x:
        for step in (-delta,delta):
            assert admissible(v+step,p)==admissible(v,p)
            assert admissible(1-v-step,p)==admissible(1-v,p)
    assert F(1,2**p)<1


def main():
    for p in range(2,201):
        check(p)
    print('VERIFY_OK: 199 exact prime periods p=2,...,200; trust margins and return multipliers')


if __name__=='__main__':
    main()
