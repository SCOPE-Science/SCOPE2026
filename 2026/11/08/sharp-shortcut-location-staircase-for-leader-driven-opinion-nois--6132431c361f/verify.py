"""Exact independent checks for leader-to-path shortcut placement.
Execute: python3 verify.py
Uses only the Python 3 standard library.
"""
from fractions import Fraction as F


def inverse_exact(a):
    m = len(a)
    z = [[F(a[i][j]) for j in range(m)] + [F(int(i == j)) for j in range(m)] for i in range(m)]
    for k in range(m):
        p = next(i for i in range(k, m) if z[i][k])
        z[k], z[p] = z[p], z[k]
        v = z[k][k]
        z[k] = [x / v for x in z[k]]
        for i in range(m):
            if i != k:
                v = z[i][k]
                z[i] = [x - v*y for x,y in zip(z[i], z[k])]
    return [r[m:] for r in z]


def L_ground(n, j=None, w=F(0)):
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for a in range(n):
        L[a][a] += (1 if a == n-1 else 2)
        if a:
            L[a][a-1] -= 1
        if a < n-1:
            L[a][a+1] -= 1
    if j is not None:
        L[j-1][j-1] += w
    return L


def improvement(n, j, w):
    # Independently implement direct summation rather than the cubic polynomial.
    S = sum(min(i,j)**2 for i in range(1,n+1))
    return F(w)*S/(1+F(w)*j)


def difference_sign_formula(n,j,w):
    return F((n-j)*(2*j+1)) + F(w)*F(j*(j+1)*(6*n-8*j-1),6)


def threshold(n,j):
    return F(6*(n-j)*(2*j+1),j*(j+1)*(8*j+1-6*n))


def approx_opt(n, w):
    options = [(improvement(n,j,w),j) for j in range(2,n+1)]
    best = max(i for i,j in options)
    return [j for i,j in options if i == best]


def check():
    checks=0
    # Verify exact inverse of the grounded path independently, not using inverse formula in inversion.
    for n in range(3,18):
        g = inverse_exact(L_ground(n))
        for i in range(1,n+1):
            for k in range(1,n+1):
                assert g[i-1][k-1] == min(i,k)
                checks+=1
        for j in range(2,n+1):
            for w in [F(1,9),F(1),F(13,2)]:
                inv = inverse_exact(L_ground(n,j,w))
                direct_delta = F(n*(n+1),2)-sum(inv[i][i] for i in range(n))
                assert direct_delta == improvement(n,j,w),(n,j,w,direct_delta,improvement(n,j,w))
                checks+=1
    for n in range(3,151):
        j0 = (6*n-1+7)//8  # ceiling of (6n-1)/8
        assert j0 >= 2 and j0<=n
        Ts = [threshold(n,j) for j in range(j0,n)]
        assert all(t>0 for t in Ts)
        assert all(Ts[i]>Ts[i+1] for i in range(len(Ts)-1))
        for w in [F(1,100),F(1,7),F(1),F(9),F(100)]:
            opt = approx_opt(n,w)
            assert len(opt) <= 2 and (len(opt)==1 or opt[1]==opt[0]+1)
            assert j0<=opt[0]<=n
            for j in range(2,n):
                num = difference_sign_formula(n,j,w)
                d = improvement(n,j+1,w)-improvement(n,j,w)
                assert (d>0)-(d<0)==(num>0)-(num<0),(n,j,w,d,num)
                checks += 1
        for j in range(j0,n):
            w=threshold(n,j)
            assert improvement(n,j,w)==improvement(n,j+1,w)
            opt=approx_opt(n,w)
            assert opt==[j,j+1],(n,j,opt)
            checks += 1
    # Exact limit check for macroscopic 75% via large-n positive fixed conductance.
    for n in [100,500,2000]:
        j=approx_opt(n,F(1))[0]
        assert abs(F(j,n)-F(3,4))<F(3,n)
        base=F(n*(n+1),2)
        residual=base-improvement(n,j,F(1))
        assert abs(residual/base-F(1,4))<F(4,n)
        checks += 2
    print(f'PASS: {checks} exact inverse, rank-one, phase, and limiting checks')

if __name__=='__main__': check()
