"""Recompute multiplication Jordan-power ranks in F_q[x,y]/(x^2,y^n).

Uses direct polynomial multiplication and finite-field Gaussian elimination,
independently of the DVR invariant-factor proof. Standard library only.
"""
from itertools import product
from collections import Counter


def field_mul(a,b,q):
    if q != 4: return a*b % q
    r=0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                r ^= (1 << (i+j)) if i+j < 2 else 3
    return r


def field_add(a,b,q):
    return a^b if q == 4 else (a+b) % q


def field_neg(a,q):
    return a if q == 4 else (-a) % q


def gauss_rank(mat,q):
    a=[row[:] for row in mat]
    nr=len(a); nc=len(a[0]); r=0
    for j in range(nc):
        pivot=next((i for i in range(r,nr) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=next(v for v in range(1,q) if field_mul(a[r][j],v,q)==1)
        a[r]=[field_mul(v,inv,q) for v in a[r]]
        for i in range(nr):
            if i!=r and a[i][j]:
                fac=a[i][j]
                a[i]=[field_add(a[i][k],field_neg(field_mul(fac,a[r][k],q),q),q)
                      for k in range(nc)]
        r+=1
        if r == nr: break
    return r


def matrix_product(A,B,q):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:
                        C[i][j]=field_add(C[i][j],field_mul(A[i][k],B[k][j],q),q)
    return C


def predicted_rank(n,p,a,b,k):
    if k == 0: return 2*n
    if k % p == 0: return 2*max(0,n-k*a)
    c=min(a,b)
    s=(k-1)*a+c
    t=(k+1)*a-c
    return max(0,n-s)+max(0,n-t)


def valuation(coeff):
    return next((i for i,c in enumerate(coeff) if c),len(coeff))


def check(q,n):
    p=2 if q==4 else q
    counts=Counter(); strong=0; total=0
    for ft in product(range(q),repeat=n-1):
        f=(0,)+ft
        a=valuation(f)
        for g in product(range(q),repeat=n):
            b=valuation(g)
            mat=[[0]*(2*n) for _ in range(2*n)]
            for i in range(n):
                for j in range(n-i):
                    mat[i+j][i]=f[j]
                    mat[n+i+j][n+i]=f[j]
                    mat[n+i+j][i]=g[j]
            power=[[int(i==j) for j in range(2*n)] for i in range(2*n)]
            ranks=[2*n]
            for k in range(1,n+3):
                power=matrix_product(power,mat,q)
                observed=gauss_rank(power,q)
                expected=predicted_rank(n,p,a,b,k)
                assert observed==expected,(q,n,f,g,k,observed,expected)
                ranks.append(observed)
            multiplicities=tuple(ranks[k-1]-2*ranks[k]+ranks[k+1]
                                 for k in range(1,n+2))
            assert all(m >= 0 for m in multiplicities)
            assert sum((k+1)*m for k,m in enumerate(multiplicities))==2*n
            counts[multiplicities]+=1
            if multiplicities[n] == 1 and multiplicities[n-2] == 1 and sum(multiplicities)==2:
                strong+=1
            total+=1
    assert total == q**(2*n-1)
    predicted_strong = (q-1)**2*q**(2*n-3) if n%p else 0
    assert strong == predicted_strong,(q,n,strong,predicted_strong)
    assert sum(counts.values()) == total
    print('PASS q=%d n=%d elements=%d types=%d SLJT=%d' % (q,n,total,len(counts),strong))


if __name__ == '__main__':
    for q,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),
                (4,2),(4,3),(5,2),(5,3)]:
        check(q,n)
    print('ALL_TWO_VARIABLE_JORDAN_CHECKS_PASSED')
