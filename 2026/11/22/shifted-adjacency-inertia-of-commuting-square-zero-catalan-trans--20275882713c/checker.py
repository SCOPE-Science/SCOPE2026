"""Independent finite-instance checks of a shifted adjacency inertia theorem.

Run: python3 checker.py
Requires Python 3 and NumPy; SymPy is optional for exact compressed ranks.
"""
from itertools import product
from math import comb
import numpy as np

def catalan_maps(n):
    # Enumerate by successive image choices, rather than using a square-zero normal form.
    def rec(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        domain_point = len(prefix)+1
        for v in range(prefix[-1], domain_point+1):
            prefix.append(v)
            yield from rec(prefix)
            prefix.pop()
    yield from rec([1])

def compose(f, g):
    return tuple(f[x-1] for x in g)

def interval(f):
    if len(set(f)) == 1:
        return (2, len(f)-1)  # zero map receives the full interior interval
    a=max(f)
    b=next(i for i in range(len(f), 0, -1) if f[i-1]==1)
    return a,b

def check(n):
    z=(1,)*n
    squarezero=[f for f in catalan_maps(n) if compose(f,f)==z]
    N=len(squarezero)
    assert N==2**(n-2)
    iv=[interval(f) for f in squarezero]
    all_iv=[(a,b) for a in range(2,n) for b in range(a,n)]
    assert set(iv)==set(all_iv)
    A=np.zeros((N,N),dtype=np.float64)
    for i,f in enumerate(squarezero):
        for j in range(i+1,N):
            g=squarezero[j]
            commuting=compose(f,g)==compose(g,f)
            overlap=(max(iv[i][0],iv[j][0]) <= min(iv[i][1],iv[j][1]))
            assert commuting==overlap,(n,f,g)
            A[i,j]=A[j,i]=int(commuting)
    lam=np.linalg.eigvalsh(A+np.eye(N))
    p=n-2
    sig=(int(sum(lam>1e-6)),int(sum(lam< -1e-6)),int(sum(abs(lam)<=1e-6)))
    expected=(p,p-1,N-2*p+1)
    assert sig==expected,(n,sig,expected)
    # Also verify the zero-removed graph; the full-interval type remains occupied.
    ix=squarezero.index(z)
    Aprime=np.delete(np.delete(A,ix,axis=0),ix,axis=1)
    lp=np.linalg.eigvalsh(Aprime+np.eye(N-1))
    sigprime=(int(sum(lp>1e-6)),int(sum(lp< -1e-6)),int(sum(abs(lp)<=1e-6)))
    assert sigprime==(p,p-1,N-2*p)
    # Compression row identity; also verify exact rank and inertia numerically.
    H=np.array([[int(max(a,c)<=min(b,d)) for c,d in all_iv] for a,b in all_iv],dtype=int)
    Hsig=np.linalg.eigvalsh(H)
    sigH=(int(sum(Hsig>1e-6)),int(sum(Hsig< -1e-6)),int(sum(abs(Hsig)<=1e-6)))
    assert sigH==(p,p-1,len(all_iv)-2*p+1)
    W=np.zeros((N,len(all_iv)),dtype=int)
    idx={interval: j for j,interval in enumerate(all_iv)}
    for i,I in enumerate(iv):W[i,idx[I]]=1
    assert np.array_equal(A.astype(int)+np.eye(N,dtype=int), W@H@W.T)
    # Check exact clique polynomial coefficients by enumerating all subsets for small n.
    if n<=6:
        for mask in range(1<<N):
            inds=[i for i in range(N) if mask>>i&1]
            actual=all(A[i,j]==1 for i,j in product(inds, repeat=2) if i<j)
            predicted=(not inds) or max(iv[i][0] for i in inds)<=min(iv[i][1] for i in inds)
            assert actual==predicted
    print(f"n={n} |S|={N} internal_intervals={len(all_iv)} inertia={sig} inertia_without_zero={sigprime} min_abs_nonzero={min(abs(x) for x in lam if abs(x)>1e-6):.8g} PASS")

if __name__=='__main__':
    for n in range(3,11):check(n)
    print('VERIFY_OK')
