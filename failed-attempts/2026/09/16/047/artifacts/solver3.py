import numpy as np
from scipy.optimize import least_squares

def interleave_ls(SF, SG, nstarts=10, seed=0, ftol=1e-12, max_nfev=2000):
    """Decide F on SF, G on SG with FG=GF=I. Returns (ok, F, G, resid)."""
    SF = np.array(SF, bool); SG = np.array(SG, bool)
    r = SF.shape[0]
    I = np.eye(r)
    iF = np.argwhere(SF); iG = np.argwhere(SG)
    nf, ng = len(iF), len(iG)
    Fm = np.zeros((r, r), int); Gm = np.zeros((r, r), int)
    for k, (i, j) in enumerate(iF): Fm[i, j] = k + 1
    for k, (j, i) in enumerate(iG): Gm[j, i] = k + 1

    def res(x):
        F = np.zeros((r, r)); G = np.zeros((r, r))
        xf = x[:nf]; xg = x[nf:]
        for k, (i, j) in enumerate(iF): F[i, j] = xf[k]
        for k, (j, i) in enumerate(iG): G[j, i] = xg[k]
        return np.concatenate([(F @ G - I).ravel(), (G @ F - I).ravel()])

    rng = np.random.default_rng(seed)
    best = (1e99, None, None)
    for s in range(nstarts):
        x0 = rng.standard_normal(nf + ng)
        try:
            sol = least_squares(res, x0, ftol=ftol, xtol=1e-12, gtol=1e-12,
                                max_nfev=max_nfev, method='lm')
        except Exception:
            continue
        v = float(np.sum(sol.fun ** 2))
        if v < best[0]:
            F = np.zeros((r, r)); G = np.zeros((r, r))
            for k, (i, j) in enumerate(iF): F[i, j] = sol.x[:nf][k]
            for k, (j, i) in enumerate(iG): G[j, i] = sol.x[nf:][k]
            best = (v, F, G)
        if best[0] < 1e-16:
            break
    v, F, G = best
    resn = float(np.linalg.norm(F @ G - I) + np.linalg.norm(G @ F - I)) if F is not None else 1e99
    return (resn < 1e-6), F, G, resn
