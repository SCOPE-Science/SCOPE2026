#!/usr/bin/env python3
"""Direct finite-field checks for idempotent Lie endomorphisms of Heisenberg algebras.

The enumerated matrices satisfy the ORIGINAL Lie homomorphism and idempotence
identities. Counts by rank and alternating radical invariant are compared
with a separately evaluated closed formula.
"""
from fractions import Fraction
from collections import Counter
from itertools import product

def gr(n,k,q):
    if k<0 or k>n:return 0
    a=Fraction(1)
    for i in range(k): a*=Fraction(q**n-q**i,q**k-q**i)
    assert a.denominator==1
    return int(a)

def gl(n,q):
    out=1
    for i in range(n):out*=q**n-q**i
    return out

def sp(s,q):
    out=q**(s*s)
    for i in range(1,s+1):out*=q**(2*i)-1
    return out

def isotropic(n,r,q):
    f=Fraction(1)
    for i in range(r):f*=Fraction(q**(2*n-i)-q**i,q**r-q**i)
    assert f.denominator==1
    return int(f)

def expected(n,q):
    out=Counter({(0,0):1, (2*n+1,-1):1})
    for r in range(1,n+1):
        for s in range(r//2+1):
            x=isotropic(n,r,q)*gr(r,2*s,q)*Fraction(gl(2*s,q),sp(s,q))*q**(r*(r+1)//2+2*r*(n-r)+r)
            assert x.denominator==1
            out[(r,2*s)]=int(x)
    return out

def matmul(a,b,p):
    h=len(a); t=len(b); w=len(b[0]);
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(t))%p for j in range(w)) for i in range(h))

def rank(a,p):
    a=[list(row) for row in a]; h=len(a); w=len(a[0]) if h else 0; r=0
    for c in range(w):
        piv=next((i for i in range(r,h) if a[i][c]%p),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        v=pow(a[r][c],-1,p)
        a[r]=[(z*v)%p for z in a[r]]
        for i in range(h):
            if i!=r and a[i][c]%p:
                v=a[i][c]
                a[i]=[(a[i][j]-v*a[r][j])%p for j in range(w)]
        r+=1
        if r==h:break
    return r

def alternating(n,p):
    m=2*n; a=[[0]*m for _ in range(m)]
    for i in range(n):
        a[i][n+i]=1
        a[n+i][i]=-1%p
    return tuple(tuple(x) for x in a)

def transpose(a):return tuple(zip(*a))

def validate_one(n,p,full_census=False):
    m=2*n
    J=alternating(n,p)
    vcols=[tuple(1 if i==j else 0 for i in range(m+1)) for j in range(m+1)]
    def brackets(u,v):
        return (sum(u[i]*J[i][j]*v[j] for i in range(m) for j in range(m))%p)
    observed=Counter()
    matrices=0
    for a in product(range(p),repeat=m*m):
        B=tuple(tuple(a[i*m+j] for j in range(m)) for i in range(m))
        B2=matmul(B,B,p)
        if B2!=B:continue
        if any(matmul(transpose(B),matmul(J,B,p),p)[i][j] for i in range(m) for j in range(m)):
            continue
        r=rank(B,p)
        s=rank(matmul(B,matmul(J,transpose(B),p),p),p)
        matrices+=1
        for f in product(range(p),repeat=m):
            if any(sum(f[j]*B[j][i] for j in range(m))%p != f[i] for i in range(m)):
                continue
            # Full (m+1)x(m+1) matrix with P(z)=0.
            P=tuple(tuple(B[i][j] for j in range(m))+(0,) for i in range(m))+(tuple(f)+(0,),)
            assert matmul(P,P,p)==P
            assert all(brackets(tuple(P[i][j] for i in range(m))+ (0,),tuple(P[i][k] for i in range(m))+(0,))==0 for j in range(m) for k in range(m))
            assert all(P[i][m]==0 for i in range(m+1))
            observed[(r,s)]+=1
    observed[(m+1,-1)]+=1 # identity map; check its bracket and idempotence.
    ident=tuple(tuple(int(i==j) for j in range(m+1)) for i in range(m+1))
    assert matmul(ident,ident,p)==ident
    assert all(brackets(vcols[i],vcols[j])==brackets(vcols[i],vcols[j]) for i in range(m+1) for j in range(m+1))
    ex=expected(n,p)
    assert observed==ex,(n,p,observed,ex)
    print(f'n={n} q={p} idempotent_quotient_matrices={matrices} distribution={dict(sorted(observed.items()))} total={sum(observed.values())} PASS')
    return observed

def direct_all_3x3(p):
    n=1; J=alternating(n,p);m=3; obs=Counter()
    for a in product(range(p),repeat=9):
        P=tuple(tuple(a[i*3+j] for j in range(3)) for i in range(3))
        if matmul(P,P,p)!=P:continue
        # Original Lie identity checked for all pairs of basis elements.
        def bracket(x,y): return (x[0]*y[1]-x[1]*y[0])%p
        valid=True
        for i in range(3):
            for j in range(3):
                c=bracket(tuple(int(h==i) for h in range(3)),tuple(int(h==j) for h in range(3)))
                left=tuple((c*P[h][2])%p for h in range(3))
                col_i=tuple(P[h][i] for h in range(3));col_j=tuple(P[h][j] for h in range(3))
                right=(0,0,bracket(col_i,col_j))
                if left!=right:valid=False;break
            if not valid:break
        if not valid:continue
        rr=rank(P,p)
        if rr==3:obs[(3,-1)]+=1
        elif rr==0:obs[(0,0)]+=1
        elif rr==1:obs[(1,0)]+=1
        else:raise AssertionError((p,rr,P))
    assert obs==expected(1,p),(p,obs,expected(1,p))
    print(f'FULL 3x3 brute field={p} distribution={dict(sorted(obs.items()))} PASS')

if __name__=='__main__':
    for p in (2,3):direct_all_3x3(p)
    for n,p in ((1,2),(1,3),(2,2)):
        validate_one(n,p)
    print('HEISENBERG_IDEMPOTENT_RETRACTION_ORBIT_COUNTS_OK')
