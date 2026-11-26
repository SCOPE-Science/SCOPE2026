"""Exact checks for record/excedance dependence identities.

Uses Python's integer and Fraction arithmetic. Exhaustive checks are finite
corroboration; the unrestricted identities follow from the proofs in RESULT.md.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial


def threshold_kernel(n, i, j, t):
    if i == 1 or t == 0 or t == n:
        return F(0)
    delta = F(t, n) - F(comb(t, i), comb(n, i)) if t >= i else F(t,n)
    if j < i:
        return -delta / (i * (i-1))
    if j == i:
        return delta / i
    return F(0)


def co_global(n):
    B = sum((F(1, comb(n-1,j)) for j in range(n)),F(0))
    return (n+1-2*B)/(2*n)


def fast_cov_from_permutations(n):
    N = factorial(n)
    sumsR=[0]*(n+1)
    sumsT=[[0]*(n+1) for _ in range(n+1)]
    sumsRT=[[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    sum_record=0;sum_exc=0;sum_product=0
    for p in permutations(range(1,n+1)):
        R=[False]+[p[i-1]==max(p[:i]) for i in range(1,n+1)]
        T=[[False]*(n+1)]+[[False]+[p[j-1]>t for t in range(1,n+1)] for j in range(1,n+1)]
        rc=sum(R)
        ex=sum(p[j-1]>j for j in range(1,n+1))
        sum_record+=rc;sum_exc+=ex;sum_product+=rc*ex
        for i in range(1,n+1):
            sumsR[i]+=R[i]
        for j in range(1,n+1):
            for t in range(1,n+1):
                v=T[j][t]; sumsT[j][t]+=v
                if v:
                    for i in range(1,n+1):
                        sumsRT[i][j][t]+=R[i]
    checks=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for t in range(1,n+1):
                actual=F(sumsRT[i][j][t],N)-F(sumsR[i]*sumsT[j][t],N*N)
                expected=threshold_kernel(n,i,j,t)
                assert actual==expected,(n,i,j,t,actual,expected)
                checks+=1
    actual=F(sum_product,N)-F(sum_record*sum_exc,N*N)
    expected=co_global(n)
    assert actual==expected,(n,actual,expected)
    checks+=1
    for j in range(1,n):
        actual=sum((threshold_kernel(n,i,j,j) for i in range(1,n+1)),F(0))
        expected=F(j,n*n)-F(1,j*comb(n,j))
        assert actual==expected,(n,j,actual,expected)
        checks+=1
    return checks


def extra_checks():
    checks=0
    for m in range(1,400):
        B=sum((F(1,comb(m,j)) for j in range(m+1)),F(0))
        Bnext=sum((F(1,comb(m+1,j)) for j in range(m+2)),F(0))
        assert Bnext==2+F(m+2,2*(m+1))*(B-2)+F(1,m+1)
        checks+=1
    for n in range(2,400):
        cov=co_global(n)
        assert (cov<0 if n<=4 else cov>0)
        checks+=1
        if n<399:
            assert co_global(n+1)>cov
            checks+=1
    return checks


if __name__=='__main__':
    total=0
    for n in range(2,9):
        k=fast_cov_from_permutations(n)
        total+=k
        print(f'n={n}: {k} exact enumerative comparisons')
    total+=extra_checks()
    print('PASS:',total,'exact checks')
