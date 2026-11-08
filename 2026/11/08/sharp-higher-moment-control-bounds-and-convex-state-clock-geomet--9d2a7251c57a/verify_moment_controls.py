#!/usr/bin/env python3
"""Independent numerical and exact tests for finite-state passage-moment control laws.

Run with: python verify_moment_controls.py
Requires numpy and sympy. Finite checks corroborate but do not establish the theorem.
"""
import math
import random
import numpy as np
import sympy as sp


def matrix_from_edges(n, edges, factors=None):
    """Killed-chain M=-Q: edges=(source,destination,rate); destination n is target."""
    M=np.zeros((n,n),float)
    factors=factors or {}
    for idx,(u,v,k) in enumerate(edges):
        z=factors.get(idx,1.0)
        M[u,u]+=z*k
        if v<n:
            M[u,v]-=z*k
    return M


def raw_moment(M,start,m):
    G=np.linalg.inv(M)
    return math.factorial(m)*np.linalg.matrix_power(G,m).dot(np.ones(len(M)))[start]


def exact_two_state():
    a,b,k=sp.symbols('a b k',positive=True)
    M=sp.Matrix([[a+k,-k],[-b,b]])
    G=M.inv()
    assert sp.simplify(G-sp.Matrix([[b,k],[b,a+k]])/(a*b))==sp.zeros(2)
    for m in range(1,7):
        moment=sp.factor(sp.factorial(m)*(G**m*sp.ones(2,1))[0])
        lead=sp.limit(moment/k**m,k,sp.oo)
        assert sp.simplify(lead-sp.factorial(m)/(a*b)**m)==0
        assert sp.simplify(sp.limit(k*sp.diff(moment,k)/moment,k,sp.oo)-m)==0
    return 6


def tests():
    rng=random.Random(20260806)
    exact=exact_two_state()
    local=0
    finite=0
    clock=0
    ncase=0
    for n in (2,3,4,5):
      for case in range(36):
        # Direct absorption from each state guarantees transience, even at grouped rate 0.
        edges=[]
        for u in range(n):
            edges.append((u,n,0.3+3*rng.random()))
            for v in range(n):
                if u!=v and rng.random()<0.72:
                    edges.append((u,v,0.1+2*rng.random()))
        u=rng.randrange(n)
        group=[j for j,(p,q,k) in enumerate(edges) if p==u and (q==n or rng.random()<0.6)]
        if not group:
            group=[j for j,(p,q,k) in enumerate(edges) if p==u][:1]
        t=0.15+3*rng.random()
        fac={j:t for j in group}
        M=matrix_from_edges(n,edges,fac)
        G=np.linalg.inv(M)
        B=matrix_from_edges(n,edges,{j:1.0 for j in group})-matrix_from_edges(n,edges,{j:0.0 for j in group})
        dG=-G@(t*B)@G
        for m in range(1,7):
            P=[np.linalg.matrix_power(G,q) for q in range(m+1)]
            U=math.factorial(m)*P[m].dot(np.ones(n))[0]
            dU=math.factorial(m)*sum((P[q]@dG@P[m-1-q]).dot(np.ones(n))[0] for q in range(m))
            sens=dU/U
            assert -m-1e-8<=sens<=m+1e-8,(n,m,sens)
            # Check algebraic sensitivity against independent log-param finite difference.
            h=1e-5
            hi={j:t*math.exp(h) for j in group}
            lo={j:t*math.exp(-h) for j in group}
            fd=(math.log(raw_moment(matrix_from_edges(n,edges,hi),0,m))-
                math.log(raw_moment(matrix_from_edges(n,edges,lo),0,m)))/(2*h)
            assert abs(sens-fd)<2e-5,(sens,fd)
            local+=1
            # Integrated robustness bound for a finite change.
            factor=1.1+2*rng.random()
            hi={j:t*factor for j in group}
            ratio=raw_moment(matrix_from_edges(n,edges,hi),0,m)/U
            assert factor**(-m)-1e-8<=ratio<=factor**m+1e-8
            finite+=1
        # For independent state-clock changes, log moment is convex.
        base=matrix_from_edges(n,edges)
        W=np.linalg.inv(base)
        theta=np.array([rng.uniform(-0.8,0.8) for _ in range(n)])
        Z=np.exp(theta)
        A=W@np.diag(1/Z)
        for m in (1,2,3,4):
            # Enumerate positive products to construct the probability on count vectors.
            weights=[]; counts=[]
            def expand(path,product):
                if len(path)==m:
                    N=np.bincount(path,minlength=n).astype(float)
                    weights.append(product*math.exp(-np.dot(theta,N)))
                    counts.append(N)
                    return
                prev=0 if not path else path[-1]
                for dest in range(n):
                    term=W[prev,dest]
                    if term>0:
                        expand(path+[dest],product*term)
            expand([],1.0)
            weights=np.array(weights)
            counts=np.array(counts)
            probs=weights/weights.sum()
            mean=probs@counts
            cov=(counts-mean).T@((counts-mean)*probs[:,None])
            eig=np.linalg.eigvalsh(cov)
            assert eig.min()>-1e-8
            assert abs(mean.sum()-m)<1e-8
            assert np.all(mean>=-1e-8) and np.all(mean<=m+1e-8)
            assert np.max(abs(cov@np.ones(n)))<1e-7
            assert abs(math.factorial(m)*weights.sum()-math.factorial(m)*
                       np.linalg.matrix_power(A,m).dot(np.ones(n))[0])<1e-7*max(1,weights.sum()*math.factorial(m))
            clock+=1
        ncase+=1
    print('PASS exact-two-state-sharpness:',exact,'moment orders')
    print('PASS grouped-edge elasticities:',local,'and independent finite differences')
    print('PASS finite-change power bounds:',finite)
    print('PASS state-clock convex-Hessian checks:',clock)
    print('PASS independently generated networks:',ncase)

if __name__=='__main__':
    tests()
