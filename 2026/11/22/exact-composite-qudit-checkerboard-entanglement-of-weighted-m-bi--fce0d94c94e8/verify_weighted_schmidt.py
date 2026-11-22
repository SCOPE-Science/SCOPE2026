"""Independent modular-image and Schmidt calculations for weighted Möbius ladders.

This does not use Smith-form routines or the cyclic-quotient derivation.
"""
from itertools import product
from math import gcd
import numpy as np

def B(n,w):
    N=2*n
    E=np.zeros((N,N),dtype=np.int64)
    for v in range(N):
        for u in ((v+1)%N,(v-1)%N): E[v,u]=1
        E[v,(v+n)%N]=w
    assert np.array_equal(E,E.T)
    return E[::2,1::2]

def rec(n,w):
    a,b=0,1
    for _ in range(n): a,b=b,-w*b-a
    an=a
    a,b=0,1
    for _ in range(n-1):a,b=b,-w*b-a
    g=gcd(abs(an),abs(a+1))
    C=np.array([[0,-1],[1,-w]],dtype=object)
    Q=np.linalg.matrix_power(C,n)-np.eye(2,dtype=object)
    det=int(Q[0,0]*Q[1,1]-Q[0,1]*Q[1,0])
    h=(abs(det)//g) if det else 0
    return g,h

def rank_count(n,d,w):
    g,h=rec(n,w)
    return (d**n)//(gcd(d,g)*gcd(d,h))

for n in (3,5,7):
    for w in (-3,-2,-1,0,1,2,3):
        for d in (2,3,4,6):
            if d**n>6000:continue
            P=B(n,w)
            im=set()
            for v in product(range(d),repeat=n):
                im.add(tuple((P@np.array(v,dtype=np.int64))%d))
            want=rank_count(n,d,w)
            assert len(im)==want,(n,w,d,len(im),want)
    print('modular images n',n,'PASS')
for n,d,w in [(3,2,-2),(3,3,-1),(3,4,2),(3,3,1),(3,4,-3)]:
    P=B(n,w)
    xs=list(product(range(d),repeat=n))
    X=np.asarray(xs,dtype=int)
    phase=X@P@X.T
    D=np.exp(2j*np.pi*(phase%d)/d)/d**n
    ev=np.linalg.svd(D,compute_uv=False)**2
    N=rank_count(n,d,w)
    assert np.count_nonzero(ev>1e-8)==N,(n,d,w,N,ev)
    assert np.max(abs(ev[:N]-1/N))<1e-9,(n,d,w,ev)
    print('full Schmidt',n,d,w,N,'PASS')
print('WEIGHTED_SCHMIDT_PASS')
