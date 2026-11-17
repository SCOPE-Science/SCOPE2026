"""Standalone finite-field incidence and distance-spectrum checks.

Requires Python >=3.9 and NumPy. Run: python checker.py
Supports the prime fields of orders two and three and the nonprime field of order four.
"""
from itertools import product, combinations
from collections import deque
from math import sqrt, log
import numpy as np


def field(q):
    if q in (2, 3):
        return (lambda x, y: (x+y) % q), (lambda x, y: (x*y) % q)
    if q == 4:
        def add(x, y): return x ^ y
        def mul(x, y):
            a0,a1=x&1,(x>>1)&1
            b0,b1=y&1,(y>>1)&1
            c0=a0*b0
            c1=(a0*b1)^(a1*b0)
            c2=a1*b1
            return (c0^c2)|((c1^c2)<<1)
        return add,mul
    raise ValueError('q must be 2, 3, or 4')


def make_graph(q):
    add,mul=field(q)
    neg=lambda a: next(x for x in range(q) if add(a,x)==0)
    inv={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    def normal(v):
        for x in v:
            if x:
                return tuple(mul(y,inv[x]) for y in v)
        raise ValueError('zero vector')
    def orth(v,w):
        ans=0
        for i,j in ((0,2),(1,3)):
            ans=add(ans,add(mul(v[i],w[j]),neg(mul(v[j],w[i]))))
        return ans==0
    pts=sorted({normal(v) for v in product(range(q), repeat=4) if any(v)})
    idx={p:i for i,p in enumerate(pts)}
    lines=set()
    for x,y in combinations(pts,2):
        if orth(x,y):
            line={idx[y]}
            for c in range(q):
                line.add(idx[normal(tuple(add(a,mul(c,b)) for a,b in zip(x,y)))])
            assert len(line)==q+1
            lines.add(tuple(sorted(line)))
    lines=sorted(lines)
    v=(q+1)*(q*q+1)
    assert len(pts)==len(lines)==v
    edges=[[] for _ in range(2*v)]
    for j,line in enumerate(lines):
        for x in line:
            edges[x].append(v+j)
            edges[v+j].append(x)
    assert all(len(x)==q+1 for x in edges)
    return edges


def distances(edges):
    n=len(edges)
    out=[]
    for i in range(n):
        dd=[-1]*n
        dd[i]=0
        todo=deque([i])
        while todo:
            u=todo.popleft()
            for v in edges[u]:
                if dd[v]<0:
                    dd[v]=dd[u]+1
                    todo.append(v)
        assert all(0<=x<=4 for x in dd)
        out.append(dd)
    return np.asarray(out,dtype=np.int64)


def bisection(q):
    k=q+1
    def f(p):return -k +q*k*2**p -q*q*k*3**p +q**3*4**p
    lo,hi=0.,1./q
    assert f(lo)<0<f(hi)
    for _ in range(75):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def expected_spectrum(q,p):
    k=q+1
    v=(q+1)*(q*q+1)
    f=q*(q+1)**2//2
    h=q*(q*q+1)//2
    a=2**p;b=3**p;c=4**p
    high=k+q*k*a+q*q*k*b+q**3*c
    alternating=-k+q*k*a-q*q*k*b+q**3*c
    pos=(q-1)*a-q*c+sqrt(2*q)*(1-b)
    neg=(q-1)*a-q*c-sqrt(2*q)*(1-b)
    zero=-k*a+q*c
    return sorted([high,alternating]+[pos]*f+[neg]*f+[zero]*(2*h))


def verify(q):
    E=make_graph(q); n=len(E);k=q+1
    D=distances(E)
    a=np.asarray([[int(j in E[i]) for j in range(n)] for i in range(n)],dtype=np.int64)
    shells=[1,k,q*k,q*q*k,q**3]
    assert all(list(np.bincount(D[i],minlength=5))==shells for i in range(n))
    # Reconstruct each distance matrix through integer walk-count recurrences.
    for i in range(n):
        walk=np.zeros(n,dtype=np.int64); walk[i]=1
        ww=[]
        for r in range(1,5):
            nxt=np.zeros(n,dtype=np.int64)
            for j in range(n):
                if walk[j]:
                    for z in E[j]:
                        nxt[z]+=walk[j]
            walk=nxt
            ww.append(walk.copy())
        w1,w2,w3,w4=ww
        ident=np.arange(n)==i
        assert np.all((D[i]==2)==(w2-k*ident))
        assert np.all((D[i]==3)==(w3-(2*q+1)*w1))
        assert np.all(k*(D[i]==4)==(w4-(3*q+1)*w2+q*k*ident))
    beta=bisection(q)
    assert 0 < beta < 1/q
    tested=[0.0,beta/2,beta,1/q,1.0]
    for p in tested:
        F=np.where(D==0,0,np.power(D.astype(float),p))
        observed=np.linalg.eigvalsh(F)
        pred=np.asarray(expected_spectrum(q,p))
        assert np.max(np.abs(observed-pred)) < 5e-7, (q,p,np.max(np.abs(observed-pred)))
        if p < beta-1e-8:
            assert observed[-2]<-1e-7
        if abs(p-beta)<1e-8:
            assert abs(observed[-2])<1e-7
            assert observed[-3]<-1e-7
        if p>beta+1e-8:
            assert observed[-2]>1e-7
    print(f'q={q}, vertices={n}, beta={beta:.12f}, q^3 beta={q**3*beta:.9f}, spectra=OK')


if __name__=='__main__':
    for q in (2,3,4):
        verify(q)
    print('GQ_NEGATIVE_TYPE_EXACT_AND_SPECTRAL_CHECKS_PASS')
