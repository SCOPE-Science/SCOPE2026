import numpy as np

def build_basis(y, mults, D):
    """mults: dict k->m (pole y=-exp(-2k) multiplicity m); poly degree D. Returns A."""
    cols = [y**j for j in range(D+1)]
    for k, m in sorted(mults.items()):
        c = np.exp(-2*k)
        for ell in range(1, m+1):
            cols.append(1.0/(y+c)**ell)
    A = np.column_stack(cols)
    return A

def lawson(y, f, A, iters=40):
    n, p = A.shape
    sc = np.linalg.norm(A, axis=0); sc[sc==0]=1
    An = A/sc
    w = np.ones(n)
    for it in range(iters):
        W = np.sqrt(w)
        Aw = An*W[:,None]; fw = f*W
        coef, *_ = np.linalg.lstsq(Aw, fw, rcond=None)
        r = An@coef - f
        e = np.max(np.abs(r))
        w = np.abs(r)
        w = np.clip(w/np.mean(w), 1e-8, 1e8)
    coef = coef/sc
    return np.max(np.abs(A@coef-f))

def grid(n1=2500, n2=2500):
    y1 = np.exp(np.linspace(np.log(1e-14), 0, n1))
    y2 = np.linspace(0, 1, n2)
    return np.unique(np.concatenate([y1,y2]))

y = grid(); f = np.sqrt(y)
print("npts", len(y))

# scan: uniform multiplicity m, scales 0..K, poly D; y-budget d: (K+1)*m<=d, D<=d
for d in [4,6,9,12,16,20,25,32,40,50]:
    best = 1e9; cfg=None
    for K in range(0, 25):
        for m in [1,2,3,4,6,8]:
            if (K+1)*m > d: continue
            for D in [d, d//2, d//4, 0]:
                mults = {k:m for k in range(K+1)}
                try:
                    A = build_basis(y, mults, D)
                    e = lawson(y,f,A,iters=25)
                except Exception:
                    continue
                if e < best: best=e; cfg=(K,m,D)
    # x-degree n=2d; target exponent check
    n = 2*d
    print(f"d={d:3d} (n={n:3d}) best~{best:.3e} cfg(K,m,D)={cfg} -lnE/sqrt(n)={-np.log(best)/np.sqrt(n):.3f} target-need>=2.8 -> E<= {2*np.exp(-2.8*np.sqrt(n)):.3e}")
