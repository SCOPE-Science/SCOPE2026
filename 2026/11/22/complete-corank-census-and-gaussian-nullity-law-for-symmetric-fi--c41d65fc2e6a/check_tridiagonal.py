"""Recompute finite-field symmetric tridiagonal nullity frequencies independently.

No external packages. Includes GF(4)=GF(2)[u]/(u^2+u+1).
"""
from itertools import product
from collections import Counter


def operations(q):
    if q == 4:
        add = lambda x, y: x ^ y
        def mul(a,b):
            v=0
            if b & 1: v ^= a
            if b & 2: v ^= a << 1
            if v & 8: v ^= (0b1110)
            if v & 4: v ^= (0b111)
            return v
        neg=lambda a:a
        return add, mul, neg
    assert q in (2,3,5,7), q
    return (lambda a,b:(a+b)%q,lambda a,b:(a*b)%q,lambda a:(-a)%q)


def matrix_nullity(q,diag,edge):
    add,mul,neg=operations(q)
    n=len(diag)
    a=[[0]*n for _ in range(n)]
    for i,x in enumerate(diag):a[i][i]=x
    for i,b in enumerate(edge):a[i][i+1]=b;a[i+1][i]=b
    r=0
    for c in range(n):
        k=next((k for k in range(r,n) if a[k][c]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        inv=next(v for v in range(1,q) if mul(a[r][c],v)==1)
        for j in range(c,n):a[r][j]=mul(a[r][j],inv)
        for k in range(r+1,n):
            v=a[k][c]
            if v:
                for j in range(c,n):a[k][j]=add(a[k][j],neg(mul(v,a[r][j])))
        r+=1
    return n-r


def predicted(q,n):
    if n==0:return (1,)
    if n==1:return (q-1,1)
    last2=[1];last1=[q-1,1]
    for d in range(2,n+1):
        c=[0]*(d+1)
        for i,v in enumerate(last1):
            c[i]+=q*(q-1)*v
            c[i+1]+=v
        for i,v in enumerate(last2): c[i]+=q*q*(q-1)*v
        if d==2:
            # The rational numerator has the additional correction for z^2,
            # which is q(q-1), not q^2(q-1).
            c[0]-=q*(q-1)*(q-1)
        last2,last1=last1,c
    return tuple(last1)


def main():
    cases=[(2,n) for n in range(1,7)]+[(3,n) for n in range(1,5)]+[(4,n) for n in range(1,4)]+[(5,n) for n in range(1,4)]+[(7,n) for n in range(1,3)]
    total=0
    for q,n in cases:
        hist=Counter()
        for coords in product(range(q),repeat=2*n-1):
            diag=coords[:n];edges=coords[n:]
            hist[matrix_nullity(q,diag,edges)]+=1
        actual=tuple(hist[i] for i in range(n+1))
        calc=predicted(q,n)
        assert actual==calc,(q,n,actual,calc)
        assert sum(actual)==q**(2*n-1)
        total+=sum(actual)
        print(f'q={q}, n={n}, count={sum(actual)}, histogram={actual}, PASS')
    print(f'ALL {len(cases)} CASES PASSED, {total} MATRICES VERIFIED')


if __name__=='__main__':main()
