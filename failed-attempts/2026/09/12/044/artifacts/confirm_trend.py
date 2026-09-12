import numpy as np, time
def grid():
    y1 = np.exp(np.linspace(np.log(1e-14), 0, 1500))
    y2 = np.linspace(0, 1, 1500)
    return np.unique(np.concatenate([y1,y2]))
def lawson(y, f, cols, iters=25):
    A = np.column_stack(cols)
    sc = np.linalg.norm(A, axis=0); sc[sc==0]=1
    An = A/sc; w = np.ones(len(y))
    for it in range(iters):
        W = np.sqrt(w)
        coef,_r,_rn,_s = np.linalg.lstsq(An*W[:,None], f*W, rcond=None)
        r = An@coef - f
        w = np.clip(np.abs(r)/np.mean(np.abs(r)), 1e-8, 1e8)
    coef = coef/sc
    return np.max(np.abs(A@coef-f))
def cols_for(y, mults, D):
    cols=[y**j for j in range(D+1)]
    for k,m in sorted(mults.items()):
        c=np.exp(-2*k)
        for ell in range(1,m+1): cols.append(1.0/(y+c)**ell)
    return cols
y=grid(); f=np.sqrt(y); t0=time.time()
for d in [16,20,25]:
    n=2*d; tgt=2*np.exp(-2.8*np.sqrt(n))
    best=1e9; bcfg=None
    cands=[]
    for K in range(0,16):
        for m in [1,2]:
            q=(K+1)*m
            if q<=d: cands.append(({k:m for k in range(K+1)},d-q,f"unifK{K}m{m}"))
    for k0 in [0,1,2]:
        for K in range(k0+2,14):
            base={k:1 for k in range(k0,K+1)}
            if len(base)<=d: cands.append((dict(base),d-len(base),f"base{k0}-{K}"))
            for a in range(k0,K+1):
                for b in range(a,min(a+3,K+1)):
                    m2=dict(base)
                    for k in range(a,b+1): m2[k]=2
                    if sum(m2.values())<=d: cands.append((m2,d-sum(m2.values()),f"tap{k0}-{K}x2[{a},{b}]"))
    for mults,D,tag in cands:
        try: e=lawson(y,f,cols_for(y,mults,D))
        except Exception: continue
        if e<best: best=e; bcfg=(tag,D)
    print(f"d={d} n={n} tgt={tgt:.3e} best~{best:.3e} cfg={bcfg} ratio={best/tgt:.2e} -ln(E/2)/sqrt(n)={-np.log(best/2)/np.sqrt(n):.3f} (need>=2.8) t={time.time()-t0:.0f}s",flush=True)
