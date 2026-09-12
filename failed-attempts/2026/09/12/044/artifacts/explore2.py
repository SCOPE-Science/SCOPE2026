import numpy as np

def build_basis_correct(y, mults, d):
    q = sum(mults.values())
    D = d - q
    assert D >= 0
    cols = [y**j for j in range(D+1)]
    for k, m in sorted(mults.items()):
        c = np.exp(-2*k)
        for ell in range(1, m+1):
            cols.append(1.0/(y+c)**ell)
    return np.column_stack(cols), D, q

def lawson(y, f, A, iters=25):
    n, p = A.shape
    sc = np.linalg.norm(A, axis=0); sc[sc==0]=1
    An = A/sc
    w = np.ones(n)
    for it in range(iters):
        W = np.sqrt(w)
        Aw = An*W[:,None]; fw = f*W
        coef, *_ = np.linalg.lstsq(Aw, fw, rcond=None)
        r = An@coef - f
        w = np.clip(np.abs(r)/np.mean(np.abs(r)), 1e-8, 1e8)
    coef = coef/sc
    return np.max(np.abs(A@coef-f))

def grid():
    y1 = np.exp(np.linspace(np.log(1e-14), 0, 1500))
    y2 = np.linspace(0, 1, 1500)
    return np.unique(np.concatenate([y1,y2]))

y = grid(); f = np.sqrt(y)
print("npts", len(y))
import itertools
for d in [4,6,9,12,16,20,25]:
    n = 2*d
    tgt = 2*np.exp(-2.8*np.sqrt(n))
    best = 1e9; cfg=None
    # uniform m over 0..K with q=(K+1)*m<=d
    for K in range(0, 20):
        for m in [1,2,3,4,5]:
            q=(K+1)*m
            if q>d: continue
            mults={k:m for k in range(K+1)}
            try:
                A,D,q2 = build_basis_correct(y,mults,d)
                e = lawson(y,f,A)
            except Exception as ex:
                continue
            if e<best: best=e; cfg=(K,m,D)
    print(f"d={d:3d} n={n:3d} best~{best:.3e} cfg={cfg} ratio-vs-tgt={best/tgt:.2e} -lnE/sqrt(n)={-np.log(best)/np.sqrt(n):.3f} (need 2.8 up to +ln2/sqrt(n)={2.8-np.log(2)/np.sqrt(n):.3f} on -ln(E/2)/sqrt(n))")
