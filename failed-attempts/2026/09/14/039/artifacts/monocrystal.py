"""Nakajima monomial crystal enumeration for D4 product crystal B(2w2, R_nat)."""
from collections import defaultdict
adj = {0:[1],1:[0,2,3],2:[1],3:[1]}
parity = {1:0, 0:1, 2:1, 3:1}
def add(e1,e2,sign=1):
    r=dict(e1)
    for k,v in e2.items():
        r[k]=r.get(k,0)+sign*v
        if r[k]==0: del r[k]
    return r
def zexp(i,k):
    d={(i,k):1,(i,k+2):1}
    for j in adj[i]:
        d[(j,k+1)]=d.get((j,k+1),0)-1
    return {k:v for k,v in d.items() if v!=0}
def wt(p):
    w=[0]*4
    for (i,k),a in p.items(): w[i]+=a
    return tuple(w)
def eps_phi(p,i):
    P=parity[i]
    ks=[k for (j,k) in p if j==i]
    lo=min(ks)-4 if ks else -6; hi=max(ks)+4 if ks else 6
    s=[k for k in range(lo-2,hi+3) if k%2==P%2]
    tot=defaultdict(int)
    for (j,k),v in p.items():
        if j==i: tot[k]+=v
    c=0; epsd={}
    for k in s: c+=tot.get(k,0); epsd[k]=-c
    c2=0; phid={}
    for k in reversed(s): c2+=tot.get(k,0); phid[k]=c2
    return max(epsd.values()),max(phid.values()),epsd,phid
def apply_e(p,i):
    eps,phi,epsd,phid=eps_phi(p,i)
    if eps==0: return None
    k=min(k for k,v in epsd.items() if v==eps)
    return add(p,zexp(i,k))
def apply_f(p,i):
    eps,phi,epsd,phid=eps_phi(p,i)
    if phi==0: return None
    k=max(k for k,v in phid.items() if v==phi)
    return add(p,zexp(i,k-2),sign=-1)
def key(p): return tuple(sorted(p.items()))
def gen_fund(i,c):
    start={(i,c):1}; seen={key(start):start}; frontier=[start]
    while frontier:
        p=frontier.pop()
        for j in range(4):
            q=apply_f(p,j)
            if q is not None and key(q) not in seen:
                seen[key(q)]=q; frontier.append(q)
    return list(seen.values())

if __name__=="__main__":
    F=gen_fund(1,0)
    print("fund size",len(F))
    # product set
    prod={}
    for a in F:
        for b in F:
            p=add(a,b); prod[key(p)]=p
    print("product set size:",len(prod))
    # closure under e,f (should already be closed)
    # BFS closure from top monomial y20*y20
    top={(1,0):2}
    seen={key(top):top}; frontier=[top]
    while frontier:
        p=frontier.pop()
        for j in range(4):
            for q in (apply_e(p,j),apply_f(p,j)):
                if q is not None and key(q) not in seen:
                    seen[key(q)]=q; frontier.append(q)
    print("closure from top size:",len(seen))
    print("product==closure?", len(prod)==len(seen), set(prod)==set(seen))
    # weight distribution
    from collections import Counter
    c=Counter(wt(p) for p in prod.values())
    print("distinct weights:",len(c))
    import numpy as np
    C=np.array([[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]])
    lam=(0,2,0,0)
    def sub(a,b): return tuple(x-y for x,y in zip(a,b))
    print("weight (0,2,0,0) count:",c[(0,2,0,0)]," weight (0,0,0,0) count:",c[(0,0,0,0)])
    # list zero-weight monomials
    for k,p in prod.items():
        if wt(p)==(0,0,0,0):
            print(dict(sorted(p.items())))
