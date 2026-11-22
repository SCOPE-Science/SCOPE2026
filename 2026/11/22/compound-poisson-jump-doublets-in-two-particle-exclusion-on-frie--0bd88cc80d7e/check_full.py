"""Construct original unordered-pair dynamics without quotient formulas; compare cumulants."""
import itertools
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

for m in range(1,13):
    n=2*m+1
    edges={(0,u) for u in range(1,n)}
    edges.update((2*i+1,2*i+2) for i in range(m))
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    pairs=list(itertools.combinations(range(n),2));index={x:i for i,x in enumerate(pairs)}
    count=len(pairs)
    Q=lil_matrix((count,count),dtype=float);rates=[]
    for idx,p in enumerate(pairs):
        w=0
        for u in p:
            for v in adj[u]:
                if v not in p:
                    to=tuple(sorted((v, next(x for x in p if x!=u))))
                    Q[idx,index[to]]+=1
                    w+=1
        Q[idx,idx]=-w
        rates.append(w)
    rates=np.array(rates,dtype=float)
    mu=np.mean(rates)
    f=rates-mu
    # enforce unique zero mean of Poisson solution by pinning one row and postcentering
    A=(-Q).tolil();A[0,:]=0;A[0,0]=1
    rhs=f.copy();rhs[0]=0
    h=spsolve(A.tocsr(),rhs);h-=np.mean(h)
    F=1+2*np.mean(f*h)/mu
    targetmu=6*(2*m-1)/(2*m+1)
    targetF=(40*m**3-52*m**2+110*m-71)/(3*(2*m-1)*(2*m+1)**2)
    assert abs(mu-targetmu)<1e-11,(m,mu,targetmu)
    assert abs(F-targetF)<1e-9,(m,F,targetF)
    print(f'm={m:2} configs={count:3} mean={mu:.12g} F={F:.12g} PASS')
print('PASS all independent full-configuration calculations')
