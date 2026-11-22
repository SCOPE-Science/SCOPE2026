"""Reproduce exact color-resolved palindrome covariance and eigenspaces.

Only Python 3 standard library required.  Finite checks supplement the proof.
"""
from itertools import product
from fractions import Fraction as F
from math import sqrt, isclose

def kernel(q):
    pairs = [(a, b) for a in range(q) for b in range(q) if a != b]
    M = []
    for i, (a, b) in enumerate(pairs):
        M.append([F(i == j, q**3) + F(2 * (a == e and b == c), q**4)
                  + F(2 * (a == c), q**5) - F(5, q**6)
                  for j, (c, e) in enumerate(pairs)])
    return pairs, M

def matvec(M, x):
    return [sum((v * w for v, w in zip(row, x)), F(0)) for row in M]

def enumerate_covariance(q, n):
    pairs, M = kernel(q)
    d = len(pairs)
    lookup = {p: i for i, p in enumerate(pairs)}
    sums = [0] * d
    mixed = [[0] * d for _ in range(d)]
    for w in product(range(q), repeat=n):
        c = [0] * d
        for i in range(n):
            a, b, z = w[i], w[(i + 1) % n], w[(i + 2) % n]
            if a == z and a != b:
                c[lookup[a, b]] += 1
        for i in range(d):
            sums[i] += c[i]
            for j in range(d):
                mixed[i][j] += c[i] * c[j]
    sample_size = q**n
    for i in range(d):
        assert F(sums[i], sample_size) == F(n, q**3)
        for j in range(d):
            assert F(mixed[i][j], sample_size) - F(sums[i] * sums[j], sample_size**2) == n * M[i][j]
    return d * d + d

def eigen_checks(q):
    pairs, M = kernel(q)
    index = {p: i for i, p in enumerate(pairs)}
    d = len(pairs)
    c = F(q*q-q+3, q**5)
    s = F(q+2, q**4)
    a = F(q-2, q**4)
    assert matvec(M, [1]*d) == [c]*d
    # Antisymmetric circulation on a 3-cycle: the opposite orientation has minus sign.
    v = [0]*d
    for i,j in [(0,1),(1,2),(2,0)]:
        v[index[i,j]] += 1
        v[index[j,i]] -= 1
    assert matvec(M,v) == [a*z for z in v]
    if q>=4:
        v = [0]*d
        for i,j,z in [(0,1,1),(1,2,-1),(2,3,1),(0,3,-1)]:
            v[index[i,j]]=v[index[j,i]]=z
        assert matvec(M,v) == [s*z for z in v]
    # Entire two-copy standard module, checked using its derived 2-by-2 action.
    A = F(1,q**3)
    B = F(2,q**4)
    D = F(2,q**5)
    for k in range(q-1):
        u=[F(int(i==k)-int(i==q-1)) for i in range(q)]
        for is_row in [True, False]:
            x=[u[i] if is_row else u[j] for i,j in pairs]
            if is_row:
                predicted=[(A+D*(q-1))*u[i] + B*u[j] for i,j in pairs]
            else:
                predicted=[(B-D)*u[i] + A*u[j] for i,j in pairs]
            assert matvec(M,x)==predicted
    mult_s=q*(q-3)//2
    mult_a=(q-1)*(q-2)//2
    assert 1+2*(q-1)+mult_s+mult_a==d
    discr=(q-1)*(5*q-1)
    lp=(q*q+q-1+sqrt(discr))/q**5
    lm=(q*q+q-1-sqrt(discr))/q**5
    assert lp>float(s) if q>=4 else lp>float(c)
    assert float(s)>float(c) if q>=4 else True
    assert float(c)>lm>float(a)>0
    assert isclose(lp/float(a), (q*q+q-1+sqrt(discr))/(q*(q-2)),rel_tol=1e-12)
    # Trace and Frobenius moments of predicted complete spectral decomposition.
    pred_trace=lp*(q-1)+lm*(q-1)+float(s)*mult_s+float(a)*mult_a+float(c)
    actual_trace=sum(float(M[i][i]) for i in range(d))
    assert isclose(pred_trace,actual_trace,rel_tol=1e-12)
    pred_sq=(lp*lp+lm*lm)*(q-1)+float(s*s)*mult_s+float(a*a)*mult_a+float(c*c)
    actual_sq=sum(float(z*z) for row in M for z in row)
    assert isclose(pred_sq,actual_sq,rel_tol=1e-12)
    return 5 + 2*(q-1)

if __name__ == '__main__':
    count=0
    for q,n in [(3,5),(3,6),(3,7),(4,5),(4,6)]:
        count+=enumerate_covariance(q,n)
    for q in [3,4,5,6,8,12]:
        count+=eigen_checks(q)
    print(f'PASS: {count} independently indexed covariance/mean and spectral checks.')
