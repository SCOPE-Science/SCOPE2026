"""Independent GF(4) verification of upper-triangular multiplication-form ranks.

Usage: python3 triangular_gf4_checker.py. Field is GF(2)[t]/(t^2+t+1).
"""
from itertools import product
from random import Random

def add(a,b): return a^b

def mul(a,b):
    s=0
    while b:
        if b&1: s^=a
        b>>=1
        a<<=1
        if a&4: a^=7
    return s

def inv(a):
    if a==0: raise ValueError('division by zero')
    return next(v for v in (1,2,3) if mul(a,v)==1)

def rank(M):
    if not M:return 0
    M=[r[:] for r in M]
    h,w=len(M),len(M[0]); piv=0
    for j in range(w):
        i=next((k for k in range(piv,h) if M[k][j]),None)
        if i is None:continue
        M[piv],M[i]=M[i],M[piv]
        z=inv(M[piv][j]);M[piv]=[mul(z,a) for a in M[piv]]
        for k in range(piv+1,h):
            a=M[k][j]
            if a:M[k]=[add(M[k][l],mul(a,M[piv][l])) for l in range(w)]
        piv+=1
        if piv==h:break
    return piv

def rank_direct(n,A):
    es=[(i,j) for i in range(n) for j in range(i,n)]
    gram=[[A[i][l] if j==k else 0 for k,l in es] for i,j in es]
    return rank(gram)

def rank_blocks(n,A):
    return sum(rank([[A[i][l] for l in range(j,n)] for i in range(j+1)]) for j in range(n))

def expect(n,q):
    m=(n+1)//2
    gl=1
    for i in range(m):gl*=q**m-q**i
    free=q**(m*(m-1))
    if n%2:return free*gl
    glprev=1
    for i in range(m-1):glprev*=q**(m-1)-q**i
    gauss=(q**m-1)//(q-1)
    rank_m1=gauss**2*glprev
    return free*(gl*q**(2*m)+rank_m1*(q**m-q**(m-1))**2)

for n in (2,3):
    es=[(i,j) for i in range(n) for j in range(i,n)]
    hits=0
    for vals in product(range(4),repeat=len(es)):
        a=[[0]*n for _ in range(n)]
        for (i,j),v in zip(es,vals):a[i][j]=v
        r=rank_direct(n,a)
        assert r==rank_blocks(n,a)
        hits+=(r==(n+1)**2//4)
    assert hits==expect(n,4)
    print('GF4_COMPLETE n=%s total=%s maximal=%s expected=%s PASS'%(n,4**len(es),hits,expect(n,4)))

rnd=Random(1729)
n=4
for t in range(5000):
    a=[[rnd.randrange(4) if j>=i else 0 for j in range(n)] for i in range(n)]
    r=rank_direct(n,a)
    assert r==rank_blocks(n,a)
print('GF4_RANDOM n=4 samples=5000 gram_block_identity PASS')
print('GF4_ADDITIONAL_CHECKS_PASS')
