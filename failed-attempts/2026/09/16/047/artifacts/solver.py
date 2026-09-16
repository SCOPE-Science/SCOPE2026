import numpy as np
def find_interleave(SF,SG,nstarts=30,itmax=200,seed=0):
    SF=np.array(SF,bool); SG=np.array(SG,bool)
    r=SF.shape[0]
    iF=np.argwhere(SF); forb=np.argwhere(~SG)  # forb positions (j,i) in G=inv(F)
    # G=inv(F) indexed [j,i]: F is [i,j]. inv(F) is [i,j]?? careful: F: M->N? Let's define F rows=i(M) cols=j(N)? Actually F maps M->N? Standard: F_ij: M_i->N_j. Matrix mult FG: (FG)[i,i']=sum_j F[i,j]G[j,i']. So G rows=j cols=i. So G as (r x r) with rows=j. inv(F) as square matrix: F is ixj, G is jxi. If we view both as rxr, G = F^{-1} exactly (since FG=I_r, GF=I_r). Indexing consistent: G[j,i] = (F^{-1})[j,i]? F^{-1} rows=j cols=i. Yes same orientation if F rows=i cols=j.
    rng=np.random.default_rng(seed)
    best=(1e99,None,None)
    for s in range(nstarts):
        x=rng.standard_normal(len(iF))
        # simple gradient-free: hill climb with adaptive steps (bounded, fast)
        def build(x):
            F=np.zeros((r,r)); F[SF]=x; return F
        F=build(x)
        step=0.5; cur=1e99
        # evaluate
        def loss(F):
            d=np.linalg.det(F)
            if abs(d)<1e-6: return 1e6
            try: G=np.linalg.inv(F)
            except: return 1e6
            tot=0.0
            for (j,i) in forb:
                tot+=float(G[j,i]**2)
            # also require det nonzero bonus? keep
            return tot
        cur=loss(F)
        for it in range(itmax):
            improved=False
            # coordinate/random directions
            for _ in range(len(iF)*2):
                d=rng.standard_normal(len(iF)); d/= (np.linalg.norm(d)+1e-9)
                for sgn in (1,-1):
                    Fn=build(x+sgn*step*d)
                    v=loss(Fn)
                    if v<cur:
                        x=x+sgn*step*d; cur=v; improved=True; break
                if improved: break
            if cur<1e-12: break
            if not improved: step*=0.5
            if step<1e-8: break
        F=build(x)
        if cur<best[0]: best=(cur,F, np.linalg.inv(F) if abs(np.linalg.det(F))>1e-9 else None)
        if best[0]<1e-12: break
    return best
