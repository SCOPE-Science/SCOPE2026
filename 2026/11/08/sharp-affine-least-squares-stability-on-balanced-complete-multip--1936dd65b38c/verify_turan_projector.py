"""Exact-rational finite checks for the sharp affine projection norm on balanced complete multipartite metric graphs.

Run: python verify_turan_projector.py
The finite checks corroborate the universal proof, not replace it.
"""
from fractions import Fraction as F


def invert(mat):
    n = len(mat)
    a = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(mat)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[pivot], a[j] = a[j], a[pivot]
        t = a[j][j]
        a[j] = [v / t for v in a[j]]
        for i in range(n):
            if i == j:
                continue
            t = a[i][j]
            if t:
                a[i] = [x - t * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def abs_integral_linear(a, b):
    a, b = F(a), F(b)
    if a * b >= 0:
        return (abs(a) + abs(b)) / 2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))


def target(r, s):
    t = 2*r-3
    return 2 + F(t*s-8*r+13, 3*t*(t*s+1))


def check_graph(r, s):
    v = r*s
    d = (r-1)*s
    edges = [(i, j) for i in range(v) for j in range(i+1, v)
             if i//s != j//s]
    # 6 times the exact nodal Gram matrix.
    g = [[2*d*int(i == j) + int(i//s != j//s)
          for j in range(v)] for i in range(v)]
    gi = invert(g)
    beta = F(1, 6*s*s*(r-1)*(2*r-3))
    # Independently inverted matrix must match the three-entry spectral inverse.
    for i in range(v):
        for j in range(v):
            predicted = (3*s*(2*r-3)+1)*beta if i == j else (
                beta if i//s == j//s else -2*beta)
            assert gi[i][j] == predicted, (r, s, i, j)
    vals=[]
    for i in range(v):
        row = F(0)
        for a,b in edges:
            row += abs_integral_linear(6*gi[i][a],6*gi[i][b])
        vals.append(row)
    assert all(x == target(r,s) for x in vals), (r,s,vals,target(r,s))
    # An edge interior has strictly smaller row norm; independently integrate
    # its reproducing kernel rather than invoking vertex convexity.
    e0,e1 = edges[0]
    for t in (F(1,4), F(1,2), F(3,4)):
        row=F(0)
        for a,b in edges:
            ca=6*((1-t)*gi[e0][a]+t*gi[e1][a])
            cb=6*((1-t)*gi[e0][b]+t*gi[e1][b])
            row += abs_integral_linear(ca,cb)
        assert row < target(r,s), (r,s,t,row,target(r,s))
    assert (target(r,s) > 2) == (s >= 4)
    assert (target(r,s) < 2) == (s <= 3)
    return len(edges)


def main():
    cases = [(3,s) for s in range(2,6)]+[(4,s) for s in range(2,5)]+[(5,s) for s in range(2,4)]+[(6,2)]
    count=0
    for r,s in cases:
        count+=check_graph(r,s)
    print('EXACT_DENSE_MASS_INVERSES_AND_KERNEL_INTEGRALS_OK',len(cases),count)
    for r in range(3,50):
        for s in range(2,90):
            assert target(r,s)<F(19,9)
            assert target(r,s+1)>target(r,s)
            assert (target(r,s)>2)==(s>=4)
            if s<=3:
                assert target(r+1,s)>target(r,s)
            else:
                assert target(r+1,s)<target(r,s)
    print('EXACT_THRESHOLD_MONOTONICITY_AND_ENVELOPE_OK',47*88)
    print('ALL_BALANCED_MULTIPARTITE_P1_CHECKS_OK')

if __name__ == '__main__':
    main()
