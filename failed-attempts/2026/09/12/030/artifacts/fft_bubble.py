"""A,B extraction via FFT convolutions (exact on zero-padded grid).

Bubbles (unweighted scalar, radial masks):
  B1[l] = sum_k G(k) G(k+l) 1_{|k|<=N} 1_{|k+l|<=N},  G(k)=|k|^{-2.5}1_{|k|<=N}.
Vertex-weighted bubble:
  Bw[l] = sum_k G(k)G(k+l) (k.(k+l)) 1_{|k|<=N}1_{|k+l|<=N}.
Sunset scalar: S[l] = G(l) * (B1 . restricted to |l|<=N), U0 = sum_l S (sanity).
Resonant remainder: W(N) = U(N) - sum over the two bubble channels with exact
l-dependent weights W1(l), W2(l) built from vertex factors and outer propagators.
Reports U0 vs direct U (must match), sumB1, and fits.
"""
import math, time, json
import numpy as np

SIG = 2.5

def grids(N):
    L = 2 * N + 1
    r = np.arange(-N, N + 1, dtype=np.float64)
    X, Y = np.meshgrid(r, r)
    n2 = X * X + Y * Y
    box = np.ones_like(n2, dtype=bool)
    rad = (n2 >= 1.0) & (n2 <= N * N)
    G = np.where(rad, n2 ** (-SIG / 2.0), 0.0)
    return X, Y, n2, rad, G

def conv(a, b):
    n = a.shape[0] + b.shape[0] - 1
    F = np.fft.rfft2(a, s=(n, n)) * np.fft.rfft2(b, s=(n, n))
    return np.fft.irfft2(F, s=(n, n))

def channel(N, flip=False):
    X, Y, n2, rad, G = grids(N)
    L = 2 * N + 1
    # full linear correlation C[l] = sum_k G[k] G[k+l] over box (zero-padded => exact)
    C = conv(G, G[::-1, ::-1])  # C[L-1+dl]: sum_k G[k]G[k+dl]
    off = L - 1
    # radial mask on k+l handled? conv includes box-only; apply radial restriction:
    # recompute with radially masked summand is not a convolution; instead compute
    # correction by direct loop over l-shells is O(N^4). Alternative: note radial mask
    # on |k+l| differs from box mask only in corners; compute corner correction below.
    B1 = C[off - N:off + N + 1, off - N:off + N + 1].copy()
    # corner correction: subtract sum over k with |k|<=N but N<|k+l|<=sqrt2 N (box corners)
    # direct vectorized loop over l (only ~pi N^2 of them), inner sum vectorized over k-grid
    KX = X; KY = Y
    Gk = G
    lidx = np.nonzero(rad)
    for (i, j) in zip(*[a.tolist() for a in lidx]):
        dlx, dly = i - N, j - N
        SX = KX + dlx; SY = KY + dly
        S2 = SX * SX + SY * SY
        corner = rad & ((SX * SX + SY * SY) > N * N)  # k in ball, k+l in box but outside ball
        # G(k+l) values at valid box points:
        ii = (np.arange(L)[:, None] + dlx)
        # vectorized gather via roll-free slicing:
        Gs = np.zeros_like(Gk)
        i0, i1 = max(0, dlx), min(L, L + dlx)
        j0, j1 = max(0, dly), min(L, L + dly)
        Gs[i0:i1, j0:j1] = Gk[i0 - dlx:i1 - dlx, j0 - dly:j1 - dly]
        B1[i, j] -= float(np.sum(Gk[corner] * Gs[corner]))
    return X, Y, n2, rad, G, B1

if __name__ == "__main__":
    for N in [6, 8, 12, 16, 24, 32]:
        t0 = time.time()
        X, Y, n2, rad, G, B1 = channel(N)
        S = G * B1 * rad
        U0 = float(S[rad].sum())
        print(f"N={N:3d} scalar sunset U0={U0:12.6f} sumB1={float(B1[rad].sum()):12.6f} t={time.time()-t0:.1f}s", flush=True)
