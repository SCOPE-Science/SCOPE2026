"""Exact characteristic-two matrix certificates for one-diagonal-edge rook dynamics.
Pure Python; no third-party dependencies. Binary matrix rows are Python integers.
"""
from itertools import product

def adjacency(m,n):
    N=m*n
    rows=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if i//n==j//n or i%n==j%n or (i==0 and j==n+1):
                rows[i]^=1<<j
                rows[j]^=1<<i
    return tuple(rows)

def rank(rows):
    pivots={}
    for z in rows:
        while z:
            p=z.bit_length()-1
            if p in pivots: z^=pivots[p]
            else: pivots[p]=z; break
    return len(pivots)

def multiply(A,B):
    out=[]
    for z in A:
        y=0
        while z:
            bit=z & -z
            y^=B[bit.bit_length()-1]
            z-=bit
        out.append(y)
    return tuple(out)

def identity(N):
    return tuple(1<<i for i in range(N))

def xor(*matrices):
    return tuple(__import__('functools').reduce(int.__xor__, v, 0) for v in zip(*matrices))

def evalpoly(A,terms):
    I=identity(len(A))
    P=[I]
    for k in range(max(terms)):
        P.append(multiply(P[-1],A))
    return xor(*(P[i] for i in terms))

def nullity(M):
    return len(M)-rank(M)

# Rows of three primary annihilating polynomials evaluated on the update.
polys={'zero':(1,), 'one':(0,1), 'seven':(0,1,3)}
# Jordan blocks (polynomial, chain length, copies); seven denotes z^3+z+1.
profiles={
(2,2): [('zero',1,2),('one',2,1)],
(2,3): [('seven',2,1)],
(2,4): [('zero',3,2),('one',2,1)],
(3,3): [('zero',1,3),('one',4,1),('one',2,1)],
(3,4): [('zero',1,4),('one',2,1),('seven',2,1)],
(4,4): [('zero',1,4),('zero',2,2),('zero',3,2),('one',2,1)],
}
for dims,blocks in profiles.items():
    m,n=dims;A=adjacency(m,n);N=m*n
    assert sum((3 if p=='seven' else 1)*length*copies for p,length,copies in blocks)==N
    for p,terms in polys.items():
        B=evalpoly(A,terms)
        Bk=identity(N)
        for k in range(1,5):
            Bk=multiply(Bk,B)
            expected=sum((3 if p=='seven' else 1)*copies*min(k,length) for p0,length,copies in blocks if p0==p)
            actual=nullity(Bk)
            assert actual==expected,(dims,p,k,actual,expected)
    print('core',m,n,'dimension',N,'elementary_divisors',blocks,'OK')

# Rank and exact map identities at sizes beyond the six cores.
for m in range(2,12):
 for n in range(2,12):
    A=adjacency(m,n);N=m*n
    P=[identity(N)]
    for k in range(1,19):P.append(multiply(P[-1],A))
    ranks=[rank(P[k]) for k in range(4)]
    if m%2==0 and n%2==0:
        wanted=[N,m+n,4,2] if m*n>4 else [4,2,2,2]
        assert P[5]==P[3]
    elif m%2 and n%2:
        wanted=[N,m+n,m+n,m+n]
        assert P[5]==P[1]
    else:
        e=m if m%2==0 else n
        o=n if m%2==0 else m
        wanted=[N,e+o+1,e+4,e+4]
        assert P[16]==P[2]
    assert ranks==wanted,(m,n,ranks,wanted)
print('all 100 size pairs 2..11: rank filtrations and exact map identities OK')

def predicted_blocks(m,n):
    if m%2==0 and n%2==0:
        if m==n==2:return [('zero',1,2),('one',2,1)]
        return [('zero',3,2),('zero',2,m+n-6),('zero',1,(m-2)*(n-2)),('one',2,1)]
    if m%2 and n%2:
        return [('zero',1,m*n-m-n),('one',4,1),('one',2,1),('one',1,m+n-6)]
    e=m if m%2==0 else n
    o=n if m%2==0 else m
    return [('zero',1,(e-2)*(o-1)),('zero',2,o-3),('one',2,1 if e>=4 else 0),('one',1,max(e-4,0)),('seven',2,1)]

for m in range(2,12):
 for n in range(2,12):
    A=adjacency(m,n);N=m*n;blocks=predicted_blocks(m,n)
    assert sum((3 if p=='seven' else 1)*l*v for p,l,v in blocks)==N
    for p,terms in polys.items():
        B=evalpoly(A,terms)
        P=identity(N)
        for k in range(1,5):
            P=multiply(P,B)
            want=sum((3 if p=='seven' else 1)*v*min(k,l) for p0,l,v in blocks if p0==p)
            assert nullity(P)==want,(m,n,p,k,nullity(P),want)
print('all 100 size pairs 2..11: polynomial-primary Jordan checks OK')
