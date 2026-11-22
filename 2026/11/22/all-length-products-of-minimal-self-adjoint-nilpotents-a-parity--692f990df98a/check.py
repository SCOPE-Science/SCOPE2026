"""Independent finite-field checks of matrix-product and polar adjacency assertions.
Run with python3 check.py (requires numpy)."""
import itertools, collections
import numpy as np

def data(q,r):
    n=2*r+1
    G=np.zeros((n,n),dtype=np.int64)
    for i in range(r): G[2*i,2*i+1]=G[2*i+1,2*i]=1
    G[-1,-1]=2
    L={}
    for v in itertools.product(range(q), repeat=n):
        if not any(v): continue
        v=np.array(v,dtype=np.int64)
        if (v@G@v)%q: continue
        first=next(int(x) for x in v if x)
        w=tuple((v*pow(first,-1,q))%q)
        L[w]=True
    reps=np.array(sorted(L),dtype=np.int64)
    A=((reps@G@reps.T)%q != 0).astype(np.int64)
    N=len(reps); K=q**(2*r-1); D=q**(2*r-2)
    assert N==(q**(2*r)-1)//(q-1)
    assert np.all(np.sum(A,axis=1)==K)
    assert np.array_equal(A@A,D*np.eye(N,dtype=np.int64)+D*(q-1)*np.ones((N,N),dtype=np.int64))
    for ell in range(1,6):
        P=np.linalg.matrix_power(A,ell)
        t=ell//2
        if ell%2==0: E=D**t*np.eye(N,dtype=np.int64)+(K**ell-D**t)//N*np.ones((N,N),dtype=np.int64)
        else: E=D**t*A+(K**ell-D**t*K)//N*np.ones((N,N),dtype=np.int64)
        assert np.array_equal(P,E)
    print('graph verified',q,r,N,K,'A^2=',D,'I+',D*(q-1),'J')
    return G,reps,A

for q,r in ((3,2),(5,2),(7,2),(3,3)):
    data(q,r)

# All 2- and 3-factor products of actual 5x5 matrices over F_3.
q=3;r=2
G,reps,A=data(q,r);N=len(reps);n=5
factors=[];labels=[]
for i,u in enumerate(reps):
    for a in range(1,q):
        factors.append((a*np.outer(u,u@G))%q)
        labels.append((i,a))
factors=np.array(factors,dtype=np.int64)
F=len(factors)
assert F==80
# Every ordered pair of factors, formed by ordinary dense matrix multiplication.
pair=(factors[:,None,:,:] @ factors[None,:,:,:])%q
hist2=collections.Counter(map(lambda v:tuple(v), pair.reshape(F*F,n*n)))
zero=(0,)*(n*n)
assert hist2[zero]==F*F-(q-1)**2*N*3**(2*r-1)
assert len(hist2)==1+(q-1)*N*3**(2*r-1)
assert set(hist2.values())=={q-1,hist2[zero]}
print('full pair matrix-product histogram',len(hist2),'zero=',hist2[zero])
# All ordered triples, by direct multiplication of these dense pair matrices.
hist3=collections.Counter()
for X in factors:
    triple=(pair @ X)%q
    hist3.update(map(lambda v:tuple(v),triple.reshape(F*F,n*n)))
assert hist3[zero]==F**3-(q-1)**3*N*3**(2*(2*r-1))
assert len(hist3)==1+(q-1)*N*N
assert collections.Counter(v for k,v in hist3.items() if k!=zero)=={108:80,72:3120}
print('full triple matrix-product histogram',len(hist3),'zero=',hist3[zero], 'nonzero multiplicity distribution=', {108:80,72:3120})
# Orthogonal endpoint types: equality vs nonorthogonality at k=3.
for i,u in enumerate(reps):
    for j,v in enumerate(reps):
        z=tuple(np.outer(u,v@G).reshape(-1)%q)
        expected=(q-1)**2*(27 if i==j else 18)
        assert hist3[z]==expected
print('all tests passed')
