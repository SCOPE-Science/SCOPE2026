import numpy as np

def als_interleave(SF, SG, nstarts=12, sweeps=60, seed=0, tol=1e-8):
    """Decide existence of F supported on SF, G supported on SG with FG=GF=I.
    Alternating least squares with multi-starts. Returns (ok, F, G, resid)."""
    SF = np.array(SF, bool); SG = np.array(SG, bool)
    r = SF.shape[0]
    I = np.eye(r)
    iF = np.argwhere(SF); iG = np.argwhere(SG)  # iG entries are (j,i)
    rng = np.random.default_rng(seed)
    best = (1e99, None, None)
    for s in range(nstarts):
        F = np.zeros((r, r)); G = np.zeros((r, r))
        F[SF] = rng.standard_normal(iF.shape[0])
        G[SG] = rng.standard_normal(iG.shape[0])
        for _ in range(sweeps):
            # fix G, solve min ||FG-I||^2+||GF-I||^2 over F on SF (linear)
            # vec(F_free): rows: for each (i,j) eq; cols of design from G
            m1 = r * r * 2; n1 = iF.shape[0]
            A = np.zeros((m1, n1)); b = np.zeros(m1)
            pos = {tuple(p): k for k, p in enumerate(map(tuple, iF))}
            row = 0
            for i in range(r):
                for ip in range(r):
                    for j in range(r):
                        if (i, j) in pos:
                            A[row, pos[(i, j)]] += G[j, ip]
                    b[row] = I[i, ip]; row += 1
            for j in range(r):
                for ip in range(r):
                    for i in range(r):
                        if (i, j) in pos:
                            pass
                    for ii in range(r):
                        if (ii, j) in pos:
                            A[row, pos[(ii, j)]] += (G[j, ip] if False else 0)
                    # (GF)[j,ip] = sum_i G[j,i] F[i,ip]: coeff of F[ii,ip] is G[j,ii]
                    for ii in range(r):
                        if (ii, ip) in pos:
                            A[row, pos[(ii, ip)]] += G[j, ii]
                    b[row] = I[j, ip]; row += 1
            sol, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            F = np.zeros((r, r)); F[SF] = sol
            # fix F, solve for G on SG
            posG = {tuple(p): k for k, p in enumerate(map(tuple, iG))}
            A2 = np.zeros((m1, iG.shape[0])); b2 = np.zeros(m1)
            row = 0
            for i in range(r):
                for ip in range(r):
                    for j in range(r):
                        if (j, ip) in posG:
                            A2[row, posG[(j, ip)]] += F[i, j]
                    b2[row] = I[i, ip]; row += 1
            for j in range(r):
                for ip in range(r):
                    for i in range(r):
                        if (j, i) in posG:
                            A2[row, posG[(j, i)]] += F[i, ip]
                    b2[row] = I[j, ip]; row += 1
            sol2, _, _, _ = np.linalg.lstsq(A2, b2, rcond=None)
            G = np.zeros((r, r)); G[SG] = sol2
            res = float(np.linalg.norm(F @ G - I) + np.linalg.norm(G @ F - I))
            if res < best[0]:
                best = (res, F.copy(), G.copy())
            if res < tol:
                break
        if best[0] < tol:
            break
    return best[0] < 1e-6, best[1], best[2], best[0]
