import numpy as np, math
H=0.375; c2=H*(2*H-1); ch=H
def gen(remaining):
    if not remaining: yield []; return
    i=remaining[0]
    for k in range(1,len(remaining)):
        j=remaining[k]
        rest=tuple(x for idx,x in enumerate(remaining) if idx!=0 and idx!=k)
        for r in gen(rest):
            yield [tuple(sorted((i,j)))]+r
def pairing_info(P):
    consec=[(i,j) for (i,j) in P if j==i+1]
    nonc=[(i,j) for (i,j) in P if j>i+1]
    active=sorted(set([j for (i,j) in nonc]+[i for (i,j) in nonc]+[h+1 for (h,h1) in consec]))
    col={p:c for c,p in enumerate(active)}
    refs={}
    for (h,h1) in consec:
        r=h-1
        refs[(h,h1)] = None if r<0 else col[r]
    return consec,nonc,active,col,refs
def estimate(P, N=600000, batches=12, seed=0):
    consec,nonc,active,col,refs=pairing_info(P)
    k=len(active)
    rng=np.random.default_rng(seed)
    nb=N//batches; vals=[]
    for b in range(batches):
        X=rng.random((nb,k)); X.sort(axis=1)
        f=np.ones(nb)
        for (i,j) in nonc:
            d=np.maximum(X[:,col[j]]-X[:,col[i]],1e-300)
            f=f*c2*(d**(2*H-2))
        for (h,h1) in consec:
            top=X[:,col[h1]]
            base=np.zeros(nb) if refs[(h,h1)] is None else X[:,refs[(h,h1)]]
            d=np.maximum(top-base,1e-300)
            f=f*ch*(d**(2*H-1))
        vals.append(np.mean(f)/math.factorial(k))
    return np.array(vals)
L6=list(gen(tuple(range(6))))
for idx,P in enumerate(L6):
    e=estimate(P,seed=100+idx)
    print(idx,P,"mean %.6f med %.6f iqr %.4f"%(e.mean(),np.median(e),np.percentile(e,75)-np.percentile(e,25)))
