#!/usr/bin/env python3
"""Exact finite-characteristic plane-quartic Hasse--Witt coefficient checks.
All coefficients computed over F_p by integer binomial expansion; no imports beyond stdlib.
"""
from math import comb

TRIPLES = ((2,1,1),(1,2,1),(1,1,2))
PRIMES = (3,7,11,19,23,31,43,47,59,67,71,79)

def trim(a,p):
    while len(a)>1 and not (a[-1]%p):a.pop()
    return [x%p for x in a]

def prod(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c,p)

def derivative(a,p):return trim([(i*a[i])%p for i in range(1,len(a))] or [0],p)

def rem(a,b,p):
    a=trim(a[:],p);b=trim(b[:],p)
    while a!=[0] and len(a)>=len(b):
        q=a[-1]*pow(b[-1],-1,p)%p
        k=len(a)-len(b)
        for j,t in enumerate(b):a[j+k]=(a[j+k]-q*t)%p
        a=trim(a,p)
    return a

def gcd(a,b,p):
    while b!=[0]:a,b=b,rem(a,b,p)
    return [x*pow(a[-1],-1,p)%p for x in a]

def plane_coefficient(p,rows,cols):
    ex=tuple(p*a-b for a,b in zip(rows,cols))
    if min(ex)<0 or ex[1]%4: return [0]
    j=ex[1]//4; k=p-1-j
    if k<0: return [0]
    zneed=ex[2]-k; xneed=ex[0]-k
    if xneed+zneed!=2*k or xneed<0 or zneed<0:return [0]
    coeff=[0]*(k+1)
    factor=comb(p-1,j)*(-1)**(k+zneed)
    for a in range(k+1):
        b=zneed-a
        if 0<=b<=k:coeff[b]=(coeff[b]+factor*comb(k,a)*comb(k,b))%p
    return trim(coeff,p)

def H(p):
    m=(p-1)//2
    return [comb(m,i)**2%p for i in range(m+1)]

def pcheck(p):
    m=(p-1)//2
    h=H(p)
    mat=[[plane_coefficient(p,a,b) for b in TRIPLES]for a in TRIPLES]
    for i in range(3):
        for j in range(3):
            expect=[(comb(p-1,m)*x)%p for x in h] if i==j==1 else [0]
            assert mat[i][j]==expect,(p,i,j,mat[i][j],expect)
    assert h[0]==1 and h[-1]==1
    assert sum(h)%p !=0  # H(1) !=0
    assert gcd(h,derivative(h,p),p)==[1],(p,'non squarefree')
    # Exact hypergeometric Picard-Fuchs ODE in F_p[t].
    hp=derivative(h,p);hpp=derivative(hp,p)
    res=[0]*(len(h)+2)
    for i,x in enumerate(hpp):res[i+1]=(res[i+1]+x)%p;res[i+2]=(res[i+2]-x)%p
    for i,x in enumerate(hp):res[i]=(res[i]+x)%p;res[i+1]=(res[i+1]-2*x)%p
    for i,x in enumerate(h):res[i]=(res[i]-m*m*x)%p
    assert all(x%p==0 for x in res),(p,res)
    roots=[t for t in range(p) if t not in (0,1) and sum(x*pow(t,i,p) for i,x in enumerate(h))%p==0]
    return p,m,len(roots),roots

if __name__=='__main__':
    out=[pcheck(p) for p in PRIMES]
    print('VERIFY_M7_CARTIER_OK',len(out))
    print('prime,m,basefield_root_count,roots:',out)
