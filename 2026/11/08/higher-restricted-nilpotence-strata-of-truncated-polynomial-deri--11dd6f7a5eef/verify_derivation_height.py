#!/usr/bin/env python3
"""Direct finite-field tests for truncated-polynomial restricted-nilpotent derivations."""
from itertools import product
from collections import Counter


def field(q):
    if q == 2:
        return (lambda a,b:a^b), (lambda a,b:a&b)
    if q == 4:
        def multiply(a,b):
            z=0
            for j in range(2):
                if b & (1<<j):z ^= a<<j
            while z.bit_length()>2:
                z ^= 0b111 << (z.bit_length()-3)
            return z
        return (lambda a,b:a^b),multiply
    raise ValueError('Only GF(2) and GF(4) test fields are implemented.')


def product_mats(A,B,add,mul):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
    return C


def matrix_power(A,h,add,mul):
    n=len(A)
    X=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    while h:
        if h&1:X=product_mats(X,A,add,mul)
        A=product_mats(A,A,add,mul)
        h//=2
    return X


def rank(A,q,add,mul):
    M=[row[:] for row in A]; n=len(M); r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if M[i][j]),None)
        if pivot is None:continue
        M[pivot],M[r]=M[r],M[pivot]
        inverse=next(k for k in range(1,q) if mul(k,M[r][j])==1)
        M[r]=[mul(inverse,z) for z in M[r]]
        for i in range(r+1,n):
            if M[i][j]:
                v=M[i][j]
                for k in range(j,n):M[i][k]=add(M[i][k],mul(v,M[r][k]))
        r+=1
    return r


def formula(n,q,s):
    m=n//2
    c=(m+s-1)//s
    C=[]
    for r in range(m+1):
        v=q**r
        for h in range(max(m-r,c),m):
            v+=(q-1)*q**(m-h-1+min(r,(s-1)*h))
        C.append(v)
    return [C[0]]+[C[i]-C[i-1] for i in range(1,m+1)]


def val(C):
    return next((i for i,x in enumerate(C) if x),len(C))


def check(n,q,s):
    add,mul=field(q); m=n//2
    cnt=Counter(); geom=Counter()
    for f in product(range(q),repeat=n):
        if n%2 and f[0]:continue
        M=[[0]*n for _ in range(n)]
        for j in range(1,n,2):
            for a in range(n-j+1):M[j-1+a][j]=f[a]
        Z=matrix_power(M,s,add,mul)
        if any(any(row) for row in Z):continue
        r=rank(M,q,add,mul)
        cnt[r]+=1
        if n%2:
            P=tuple(f[2*j+2] for j in range(m))
        else:
            P=tuple(f[2*j] for j in range(m))
        Q=tuple(f[2*j+1] for j in range(m))
        a,b=val(P),val(Q)
        if min(a,b)!=m-r:raise AssertionError(('rank valuation',n,q,s,f,r,a,b))
        if s*b<m or a+(s-1)*b<m:raise AssertionError(('valuation criterion',n,q,s,f,a,b))
        geom[b]+=1
    expected=formula(n,q,s)
    seen=[cnt[r] for r in range(m+1)]
    if seen!=expected:raise AssertionError((n,q,s,seen,expected))
    return f'n={n:2d},q={q},height={s:2d},count={sum(seen):7d},rank_counts={seen}'

def component_check(m,s):
    c=(m+s-1)//s; d=(m+s-2)//(s-1)
    dims=[2*m-h-max(0,m-(s-1)*h) for h in range(c,d+1)]
    actual=0
    for bits in range(1<<(2*m)):
        P=tuple((bits>>i)&1 for i in range(m))
        Q=tuple((bits>>(m+i))&1 for i in range(m))
        a,b=val(P),val(Q)
        membership=any(a>=max(0,m-(s-1)*h) and b>=h for h in range(c,d+1))
        criterion=(a+(s-1)*b>=m and s*b>=m)
        if membership!=criterion:raise AssertionError(('geometric-cover',m,s,bits))
        actual+=criterion
    expected=sum(formula(2*m,2,s))
    if actual!=expected:raise AssertionError(('geometric-count',m,s,actual,expected))
    return f'geometry m={m},height={s},components={len(dims)},dimensions={dims},points_GF2={actual}'

if __name__=='__main__':
    cases=[(n,q,s) for q,nmax in [(2,11),(4,6)] for n in range(2,nmax+1) for s in (2,4,8,16)]
    for case in cases:print(check(*case))
    for m in range(1,9):
        for s in (4,8):print(component_check(m,s))
    print('DERIVATION_RESTRICTED_HEIGHT_DIRECT_MATRIX_CHECKS_OK')
