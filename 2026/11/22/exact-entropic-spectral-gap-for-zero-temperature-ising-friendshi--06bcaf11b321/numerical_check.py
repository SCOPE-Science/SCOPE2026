import itertools,math,numpy as np
from scipy.optimize import brentq

def secular(n):
    p=(2/3)**n
    ws=[math.comb(n,k)*(2/3)**(n-k)*(1/3)**k for k in range(n+1)]
    def f(x): return 1+2*sum(w/(3*k-x) for k,w in enumerate(ws))
    return brentq(f,1.e-11,min(2*p,0.999999),xtol=1.e-15)

def direct(n):
    vertices=2*n+1
    edges=[]
    for i in range(n): edges.extend([(0,2*i+1),(0,2*i+2),(2*i+1,2*i+2)])
    cfg=[]
    for spins in itertools.product((-1,1),repeat=vertices):
        count=sum(spins[a]==spins[b] for a,b in edges)
        if count==n: cfg.append(spins)
    assert len(cfg)==2*3**n
    ix={c:j for j,c in enumerate(cfg)}
    H=np.zeros((len(cfg),len(cfg)))
    for a,spins in enumerate(cfg):
        for v in range(vertices):
            nxt=spins[:v]+(-spins[v],)+spins[v+1:]
            if nxt in ix:
                b=ix[nxt]
                H[a,b]=-1
                H[a,a]+=1
    ev=np.linalg.eigvalsh(H)
    return ev[1],len(cfg),max(abs(H.sum(axis=1)))
for n in range(2,6):
    a,se,p=direct(n)
    b=secular(n)
    print(n,a,b,a-b,se,p)
