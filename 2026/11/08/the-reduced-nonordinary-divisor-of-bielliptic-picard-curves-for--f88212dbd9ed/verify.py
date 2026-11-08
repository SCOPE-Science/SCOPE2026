#!/usr/bin/env python3
"""Finite characteristic spot checks for a symbolic Picard-family theorem.
Uses only Python's standard library; finite examples are not the infinite proof.
"""
from math import comb


def coefficient(N, K, p):
    """Polynomial [T^K](T^2+a*T+1)^N, low-to-high powers of a modulo p."""
    out = [0] * (K+1)
    for j in range(K//2+1):
        t = K-2*j
        if j+t <= N:
            out[t] = comb(N,j)*comb(N-j,t) % p
    return out


def scale(a,c,p): return [(v*c)%p for v in a]
def multiply(a,b,p):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return r

def sub(a,b,p):
    return [((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))]

def power_quadratic(m,p):
    v=[1]
    for _ in range(m): v=multiply(v,[(-4)%p,0,1],p)
    return v

def trim(f):
    while f and f[-1]==0: f.pop()
    return f

def modpoly(a,b,p):
    a=trim(a[:]);b=trim(b[:]);assert b
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        x=a[-1]*inv%p;k=len(a)-len(b)
        for j,v in enumerate(b): a[j+k]=(a[j+k]-x*v)%p
        trim(a)
    return a

def gcd(a,b,p):
    while b: a,b=b,modpoly(a,b,p)
    if not a:return []
    return trim(scale(a,pow(a[-1],-1,p),p))

def differential(a,p): return [i*a[i]%p for i in range(1,len(a))]

def check(p):
    assert p>3 and p%6==1
    m=(p-1)//6
    b=coefficient(2*m,m,p)
    s=power_quadratic(m,p)
    A=coefficient(4*m,2*m,p)
    C=coefficient(4*m,3*m,p)
    z=scale(s,comb(4*m,2*m)%p,p)
    w=scale(multiply(s,b,p),comb(4*m,m)*pow(comb(2*m,m),-1,p)%p,p)
    assert trim(A)==trim(z), ('first factorization',p)
    assert trim(C)==trim(w), ('second factorization',p)
    assert b[-1]==comb(2*m,m)%p and b[-1]!=0
    assert gcd(b,differential(b,p),p)==[1],('squarefree',p)
    assert sum(b[i]*(2**i) for i in range(len(b)))%p == comb(4*m,m)%p
    assert sum(b[i]*((-2)**i) for i in range(len(b)))%p == ((-1)**m*comb(4*m,m))%p
    # Direct plane-cohomology coefficient matrix from F^(p-1).
    basis=((2,1,1),(1,2,1),(1,1,2))
    direct=[]
    for i in range(3):
        row=[]
        for j in range(3):
            X,Y,Z=(p*basis[i][h]-basis[j][h] for h in range(3))
            if Y%3 or X%2 or X<0 or Y<0:
                row.append([]);continue
            k=Y//3;N=p-1-k
            if k<0 or N<0 or X//2>2*N:
                row.append([]);continue
            c=coefficient(N,X//2,p)
            row.append(trim(scale(c,comb(p-1,k)*(-1)**N%p,p)))
        direct.append(row)
    assert all(not direct[i][j] for i in range(3) for j in range(3) if i!=j)
    assert direct[0][0]==trim(A) and direct[1][1]==trim(b) and direct[2][2]==trim(C)
    return m

if __name__=='__main__':
    primes=[7,13,19,31,37,43,61,67,73,79,97,103,109,127,139]
    for p in primes:
        m=check(p)
        print('verified',p,'m',m)
    print('VERIFY_BIELLIPTIC_PICARD_OK',len(primes),'primes')
