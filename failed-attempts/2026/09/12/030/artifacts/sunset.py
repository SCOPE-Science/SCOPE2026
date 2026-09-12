"""Vectorized sunset sums U_N (sharp) and S_N (heat) for resonant T_res, sigma=5/2.

F(k,l) = N/D, N=(k.l)(l.s)+(l.s)(s.k)+(s.k)(k.l), D=|k|^2.5|l|^2.5|s|^2.5, s=k+l.
U_N: ball |k|,|l|,|s|<=N.  S_N: weights exp(-(|k|^2+|l|^2+|s|^2)/N^2).
Stdlib+numpy only.
"""
import math, time, json
import numpy as np

SIG = 2.5

def pts(N):
    r = np.arange(-N, N + 1)
    X, Y = np.meshgrid(r, r)
    n2 = X * X + Y * Y
    m = (n2 >= 1) & (n2 <= N * N)
    x = X[m].astype(np.float64); y = Y[m].astype(np.float64)
    n = np.sqrt(n2[m].astype(np.float64))
    return x, y, n

def sums(N, heat=False, block=2048):
    x, y, n = pts(N)
    ds = n ** SIG  # |.|^sigma per point
    if heat:
        w = np.exp(-(n / N) ** 2)
    # k half-list (evenness)
    kh = (x > 0) | ((x == 0) & (y > 0))
    kx, ky, kd = x[kh], y[kh], ds[kh]
    if heat:
        kw = w[kh]
    N2 = float(N * N)
    tot = 0.0
    nb = int(math.ceil(len(kx) / block))
    for b in range(nb):
        s = slice(b * block, (b + 1) * block)
        SX = kx[s, None] + x[None, :]
        SY = ky[s, None] + y[None, :]
        S2 = SX * SX + SY * SY
        valid = (S2 >= 1.0) & (S2 <= N2)
        SN = np.sqrt(np.where(valid, S2, 1.0))
        SD = np.where(valid, SN ** SIG, 1.0)
        KDL = kx[s, None] * x[None, :] + ky[s, None] * y[None, :]
        LDS = x[None, :] * SX + y[None, :] * SY
        SDK = SX * kx[s, None] + SY * ky[s, None]
        NUM = KDL * LDS + LDS * SDK + SDK * KDL
        DEN = kd[s, None] * ds[None, :] * SD
        term = np.where(valid, NUM / DEN, 0.0)
        if heat:
            term = term * (kw[s, None] * w[None, :] *
                           np.where(valid, np.exp(-(S2 / N2)), 0.0))
        tot += float(term.sum())
    return 2.0 * tot

if __name__ == "__main__":
    out = {}
    for N in [6, 8, 12, 16, 24, 32, 48, 64]:
        t0 = time.time()
        U = sums(N, heat=False)
        t1 = time.time()
        S = sums(N, heat=True)
        t2 = time.time()
        out[N] = (U, S)
        print(f"N={N:3d} U={U:14.6f} S_heat={S:14.6f}  "
              f"U/sqrtN={U/math.sqrt(N):10.5f} S/sqrtN={S/math.sqrt(N):10.5f}  "
              f"t=({t1-t0:.1f},{t2-t1:.1f})s", flush=True)
    with open("sums.json", "w") as f:
        json.dump({str(k): v for k, v in out.items()}, f)
