import numpy as np, time
def grid():
    y1 = np.exp(np.linspace(np.log(1e-14), 0, 2000))
    y2 = np.linspace(0, 1, 2000)
    return np.unique(np.concatenate([y1,y2]))

def minimax_ls_qr(y, f, cols, iters=60):
    """Lawson with column scaling + QR-based lstsq (gelsd). Scaled pole basis expected."""
    A = np.column_stack(cols)
    sc = np.linalg.norm(A, axis=0); sc[sc==0]=1
    An = A/sc; w = np.ones(len(y))
    best = 1e9
    for it in range(iters):
        W = np.sqrt(w)
        coef, res, rank, sv = np.linalg.lstsq(An*W[:,None], f*W, rcond=1e-13)
        r = An@coef - f
        e = np.max(np.abs(r))
        best = min(best, e)
        w = np.clip(np.abs(r)/np.mean(np.abs(r)), 1e-10, 1e10)
    return best

def scols(y, mults, D):
    # scaled: (c/(y+c))^ell in (0,1]; Legendre-ish poly via shifted Chebyshev on [0,1]
    cols=[]
    # Chebyshev T_j(2y-1)
    T0=np.ones_like(y); T1=2*y-1
    Ts=[T0]
    if D>=1: Ts.append(T1)
    for j in range(2,D+1):
        Ts.append(2*(2*y-1)*Ts[-1]-Ts[-2])
    cols=list(Ts[:D+1])
    for k,m in sorted(mults.items()):
        c=np.exp(-2*k)
        phi=c/(y+c)
        for ell in range(1,m+1): cols.append(phi**ell)
    return cols

y=grid(); f=np.sqrt(y); t0=time.time()
for d in [6,9,12,16,20]:
    n=2*d; tgt=2*np.exp(-2.8*np.sqrt(n))
    best=1e9; bcfg=None
    cands=[]
    for K in range(0,16):
        for m in [1,2,3,4,5,6]:
            q=(K+1)*m
            if q<=d: cands.append(({k:m for k in range(K+1)},d-q,f"unifK{K}m{m}"))
    for k0 in [0,1,2]:
        for K in range(k0+2,14):
            for m in [2,3,4]:
                base={k:m for k in range(k0,K+1)}
                q=sum(base.values())
                if q<=d: cands.append((dict(base),d-q,f"unif{k0}-{K}m{m}"))
    for mults,D,tag in cands:
        try: e=minimax_ls_qr(y,f,scols(y,mults,D))
        except Exception: continue
        if e<best: best=e; bcfg=(tag,D)
    print(f"d={d} n={n} tgt={tgt:.3e} best~{best:.3e} cfg={bcfg} ratio={best/tgt:.2e} -ln(E/2)/sqrt(n)={-np.log(best/2)/np.sqrt(n):.3f} t={time.time()-t0:.0f}s",flush=True)
