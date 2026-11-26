"""Reproduce finite-projective-incidence negative-type spectral checks.

Uses exact integer arithmetic for the decisive dimension-five cutoff
and finite-field incidence/distance reconstruction for small geometries.
This is a supplement to the all-dimension proof, not an exhaustive check.
"""
from fractions import Fraction
from math import isqrt, sqrt
import numpy as np

# Exact bracketing of rational powers: lo <= base**(num/den) < hi.
def root_bounds(base, num, den, scale=10**8):
    assert num >= 0 and den > 0
    left, right = scale, base * scale + 1
    target = base ** num * scale ** den
    while right - left > 1:
        mid = (left + right) // 2
        if mid ** den <= target:
            left = mid
        else:
            right = mid
    return Fraction(left, scale), Fraction(right, scale)

def square_root_bounds(n, scale=10**8):
    k = isqrt(n*scale*scale)
    return Fraction(k,scale),Fraction(k+1,scale)

def gamma_bounds_binary(d, num, den):
    b2 = root_bounds(2,num,den)
    b3 = root_bounds(3,num,den)
    v = 2**(d+1)-1; k=2**d-1; m=2**d
    return ((v-1)*b2[0]-k-m*b3[1],
            (v-1)*b2[1]-k-m*b3[0])

def transverse_bounds_binary(d,num,den):
    b2 = root_bounds(2,num,den)
    b3 = root_bounds(3,num,den)
    z=2**(d-1)
    s0,s1=square_root_bounds(z)
    return (s0*(b3[0]-1)-b2[1],s1*(b3[1]-1)-b2[0])

# Analytic finitely many base cases, with strict exact-rational margins.
for d,p in ((5,(1,5)),(6,(1,16)),(7,(1,32))):
    glo,ghi=gamma_bounds_binary(d,*p)
    tlo,thi=transverse_bounds_binary(d,*p)
    assert glo > 0, (d,glo)
    assert thi < 0, (d,thi)
    print('rigorous witness',d,p,'gamma>',float(glo),'transverse<',float(thi))
for d,lo,hi in ((3,(482,1000),(483,1000)),(4,(335,1000),(336,1000))):
    assert transverse_bounds_binary(d,*lo)[1] < 0, (d,lo)
    assert transverse_bounds_binary(d,*hi)[0] > 0, (d,hi)
    # gamma upper, based on monotone 2^p and 3^p over the bracket.
    a = root_bounds(2,*hi)[1]
    b = root_bounds(3,*lo)[0]
    v=2**(d+1)-1;k=2**d-1;m=2**d
    upper=(v-1)*a-k-m*b
    assert upper < 0, (d,upper)
    print('rigorous first mode',d,'gamma(s)<',float(upper))


def projective_vectors(dim,q):
    from itertools import product
    canon={}
    for v in product(range(q),repeat=dim):
        if not any(v): continue
        lead=next(x for x in v if x)
        w=tuple((x*pow(lead,-1,q))%q for x in v)
        canon[w]=None
    return sorted(canon)

def incidence(dim,q):
    pts=projective_vectors(dim,q)
    n=len(pts)
    B=np.array([[(sum(x*y for x,y in zip(p,h))%q==0) for h in pts] for p in pts],dtype=int)
    assert np.all(B.sum(0)==(q**(dim-1)-1)//(q-1))
    assert np.all(B.sum(1)==(q**(dim-1)-1)//(q-1))
    return B

def distance_matrix(B):
    v=len(B); N=2*v
    adj=np.zeros((N,N),dtype=int)
    adj[:v,v:]=B;adj[v:,:v]=B.T
    dist=np.full((N,N),N+1,dtype=int)
    for u in range(N):
        dist[u,u]=0
        queue=[u]
        for i in queue:
            for j in np.flatnonzero(adj[i]):
                if dist[u,j]==N+1:
                    dist[u,j]=dist[u,i]+1;queue.append(int(j))
    assert np.max(dist)==3
    assert np.all(dist==dist.T)
    return dist

def predicted_eigenvalues(v,k,lam,p):
    a=2**p;b=3**p;s=sqrt(k-lam)
    return sorted([-a+s*(b-1)]*(v-1)+[-a-s*(b-1)]*(v-1)+[(v-1)*a-k-(v-k)*b])

def test_geometry(dim,q):
    B=incidence(dim,q)
    v=len(B);k=int(B.sum(1)[0]); lam=int((B@B.T)[0,1])
    assert np.all(B@B.T == (k-lam)*np.eye(v,dtype=int)+lam*np.ones((v,v),dtype=int))
    D=distance_matrix(B)
    N=2*v
    basis=np.zeros((N,N-1)); basis[:N-1,:]=np.eye(N-1);basis[-1,:]=-1
    # Orthonormal basis for the zero-sum hyperplane.
    Q,_=np.linalg.qr(basis)
    for p in (0,.05,.14,.25,.37,.55,1):
        power=D.astype(float)**p;np.fill_diagonal(power,0)
        reduced=Q.T@power@Q
        got=np.linalg.eigvalsh(reduced)
        expected=predicted_eigenvalues(v,k,lam,p)
        err=np.max(np.abs(got-expected))
        assert err<2e-8,(dim,q,p,err)
    print('finite geometry verified',q,dim,'v',v,'k',k,'lambda',lam)

for d,q in ((2,2),(3,2),(4,2),(5,2),(2,3),(3,3)):
    test_geometry(d+1,q)
print('ALL CHECKS PASS')
