"""A,B extraction: subtract U's own exact subdivergence bubbles; fit remainder W vs ln N.

Wh(N) = sunset(bar l) restricted by h; bubble parts computed on same mesh.
Bubble B1(l) = sum_{k: |k|,|k+l|<=N} Gk*Gkl ((k.(k+l)) weighting from vertex pair).
Reports: U, bubble pieces, remainder, local exponent est, fit Wh = A + B ln N.
"""
import math, time
import numpy as np

SIG = 2.5

def grid(N):
    r = np.arange(-N, N + 1, dtype=np.float64)
    X, Y = np.meshgrid(r, r)
    n2 = X * X + Y * Y
    return X, Y, n2

def G(X, Y, n2):
    out = np.zeros_like(n2)
    m = n2 >= 1.0
    out[m] = n2[m] ** (-SIG / 2.0)
    return out, m

if __name__ == "__main__":
    import sys
    Ns = [int(a) for a in sys.argv[1:]] or [8, 12, 16, 24, 32]
    rows = []
    for N in Ns:
        t0 = time.time()
        X, Y, n2 = grid(N)
        Gg, valid = G(X, Y, n2)
        N2 = float(N * N)
        # loop over l (interior points), build per-l bubbles via FFT-free direct conv
        # using numpy roll-based convolution on the (2N+1)^2 grid is exact for the box;
        # enforce |k+l|<=N radial mask on shifted product.
        L = 2 * N + 1
        r = np.arange(-N, N + 1, dtype=np.float64)
        lx = X[0, :]  # -N..N row values? use mesh: X varies along cols
        # iterate over nonzero l points with |l|<=N
        Lmask = (n2 <= N2) & (n2 >= 1.0)
        li, lj = np.nonzero(Lmask)
        nL = len(li)
        B = np.zeros((L, L))   # bubble B1(l) on grid index
        W1 = np.zeros((L, L))  # weight W1(l) = ((l.s?) computed later per l with s sum)
        # Gk(l+k) needs shift: for each l index offset d=(di,dj), shifted = roll(Gg, (di,dj)) masked
        for (i, j) in zip(li.tolist(), lj.tolist()):
            di, dj = i - N, j - N
            Gs = np.roll(np.roll(Gg, di, axis=0), dj, axis=1)
            # zero entries where original+k out of box OR shifted out of radial mask:
            # roll wraps; build valid-shifted mask by rolling the valid mask too
            Vs = np.roll(np.roll(valid, di, axis=0), dj, axis=1)
            # corner wrap contamination: entries whose preimage was outside box --
            # since outside-box entries of Gg are 0 anyway and valid False, but wrapped
            # nonzero values land in wrong spots. Fix: zero wrapped rows/cols explicitly.
            if di > 0:
                Gs[:di, :] = 0.0; Vs[:di, :] = False
            elif di < 0:
                Gs[di:, :] = 0.0; Vs[di:, :] = False
            if dj > 0:
                Gs[:, :dj] = 0.0; Vs[:, :dj] = False
            elif dj < 0:
                Gs[:, dj:] = 0.0; Vs[:, dj:] = False
            # radial masks: |k|<=N (valid) and |k+l|<=N (Vs & radial of shifted coord)
            # Vs already encodes box; apply radial bound via S2 grid of k+l coords:
            KX = X + (-di)  # coords of (k+l)? verify: shift by (di,dj) maps k->k-l? -> handle below
            B[i, j] = float(np.sum(Gg * Gs * Vs * valid))
        print(f"N={N} bubble grid done nL={nL} t={time.time()-t0:.1f}s", flush=True)
        rows.append((N, float(B[Lmask].sum())))
        print(f"  sumB(N={N}) = {rows[-1][1]:.6f}", flush=True)
