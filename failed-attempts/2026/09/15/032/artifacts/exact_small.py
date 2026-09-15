"""Exact stationary solve for small (q=2) outward ASEP trees via generator nullspace.
Levels: N=2 => sites: root(0), 2 leaves; N=3 => 1+2+4=7 sites (128 states, fine).
Rates: entry alpha at root if empty; each bulk site jumps at rate 1 to uniformly
chosen child (1/q each); leaf exits rate beta. Continuous-time generator -> stationary.
Report densities per level and current J = alpha(1-rho0); compare candidate formulas.
"""
import numpy as np
import itertools

def build(q, N, alpha, beta):
    # index sites: level i occupies block; total S=(q^N-1)/(q-1)
    S = (q**N - 1)//(q-1)
    # children map
    def level_of(s):
        c=0; lo=0
        for i in range(N):
            if s < lo + q**i: return i
            lo += q**i
        raise ValueError
    lvl=[level_of(s) for s in range(S)]
    start=[0]*N
    acc=0
    for i in range(N):
        start[i]=acc; acc+=q**i
    def children(s):
        i=lvl[s]; pos=s-start[i]; c0=start[i+1]+pos*q
        return [c0+k for k in range(q)]
    n=2**S
    G=np.zeros((n,n))
    for st in range(n):
        occ=[(st>>s)&1 for s in range(S)]
        # entry
        if occ[0]==0:
            ns=st|1; G[st,ns]+=alpha
        for s in range(S):
            if occ[s]==0: continue
            i=lvl[s]
            if i==N-1:
                ns=st^(1<<s); G[st,ns]+=beta
            else:
                for c in children(s):
                    if occ[c]==0:
                        ns=st^(1<<s)^(1<<c); G[st,ns]+=1.0/q
        G[st,st]=-G[st].sum()
    return G,lvl,S

def stat(G):
    n=G.shape[0]
    A=G.T.copy(); A[-1,:]=1.0
    b=np.zeros(n); b[-1]=1.0
    return np.linalg.solve(A,b)

def level_means(pi,lvl,S,N,q):
    n=len(pi); r=np.zeros(N)
    for st in range(n):
        p=pi[st]
        if p==0: continue
        for s in range(S):
            if (st>>s)&1:
                # find level
                r[lvl[s]]+=p
    # per-site: divide by q^i
    return np.array([r[i]/q**i for i in range(N)])

def J_of(alpha, r0): return alpha*(1-r0)

def mf_simple(alpha): return alpha/(1+alpha)  # naive MF J if rho0=J

def bm_root(alpha,q):
    lo,hi=1e-14, min(alpha,q)*(1-1e-12)
    def f(J):
        r=1-J/alpha
        if r<=0: return np.inf
        return J/r + (J/q)**q - 1
    for _ in range(200):
        m=(lo+hi)/2
        if f(m)>0: hi=m
        else: lo=m
    J=(lo+hi)/2; return J, 1-J/alpha

for (q,N,alpha,beta) in [(2,2,0.5,1.0),(2,2,1.0,1.0),(2,3,0.5,1.0),(2,3,1.0,2.0),(2,2,2.0,0.5)]:
    G,lvl,S=build(q,N,alpha,beta)
    pi=stat(G)
    rho=level_means(pi,lvl,S,N,q)
    J=J_of(alpha,rho[0])
    Jbm,rbm=bm_root(alpha,q)
    print(f"q={q} N={N} a={alpha} b={beta} rho={np.round(rho,5)} J={J:.5f} Jbm={Jbm:.5f} rbm={rbm:.5f} Jsimple={mf_simple(alpha):.5f}")
