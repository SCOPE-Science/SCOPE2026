"""Resonant vertex-weighted sunset: D(N) = V^Pol(sharp,N) - V^BPHZ(N) + tail bounds.

Definitions (all explicit, lattice Z^2, sigma=5/2, mu=1):
  F(k,l) as in sunset.py (resonant quartic-gradient numerator).
  Raw U(N) = sum_{|k|,|l|,|s|<=N} F.
  BPHZ: V^BPHZ(N) = U(N) - C(N) with overall-divergence counterterm
      C(N) = a0*sqrt(N) + b0*ln N + c0,  (a0,b0,c0) = least-squares fit of U
      over calibration window CAL=[24,32,48,64] (fixed BEFORE seeing D).
      (BPHZ with minimal subtraction of the divergent part = standard BPHZ
      finite part for this power-counting: subtracts divergent asymptotic.)
  Polchinski: V^Pol(N) = U(N) - C_sharp(N) + R_smooth(N) where the sharp cutoff
      boundary layer is replaced by smooth heat-kernel weight:
      R_smooth(N) = sum_{shell N/2<max|.|<=N} F * (w_heat - 1),
      w_heat = exp(-(|k|^2+|l|^2+|s|^2)/N^2).
      Hence D(N) = R_smooth(N) - (c0 part absorbed) ... explicitly:
      D(N) = R_smooth(N) + (C(N) - C_sharp(N)); with C_sharp=C this is D(N)=R_smooth(N).
      So D(N) = sum_{boundary-influenced} F*(w_heat-1), absolutely convergent
      summandwise; tail |.|>N bounded by majorant below.
  Tail/majorant: |F(k,l)| <= M(k,l) := 3|k|^{-1.5}|l|^{-2.5}|s|^{-2.5}
      + cyclic (from |num|<=3|k|^2|l|^2|s|^2... proved in DRAFT Lemma 3.1).
      Rate: sharp-boundary layer of width O(1) at radius N contributes O(N^{-1/2})
      after subtraction (Lemma 3.3); smooth-tail part O(e^{-cN}) for heat.
  Delta_reg: D*_heat - D*_sharp with D*_sharp = 0 by construction (same sharp
      regulator as BPHZ) => Delta_reg = D* = lim R_smooth(N).
"""
import math, json
import numpy as np

SIG = 2.5
CAL = [24, 32, 48, 64]

def pts(N):
    r = np.arange(-N, N + 1)
    X, Y = np.meshgrid(r, r)
    n2 = X * X + Y * Y
    m = (n2 >= 1) & (n2 <= N * N)
    return (X[m].astype(float), Y[m].astype(float),
            np.sqrt(n2[m].astype(float)), n2[m].astype(float))

def DN(N, block=2048):
    x, y, n, n2 = pts(N)
    ds = n ** SIG
    kh = (x > 0) | ((x == 0) & (y > 0))
    kx, ky, kd = x[kh], y[kh], ds[kh]
    kn2 = n2[kh]
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
        F = np.where(valid, NUM / DEN, 0.0)
        K2 = kn2[s, None]; L2 = n2[None, :]
        w = np.where(valid, np.exp(-(K2 + L2 + S2) / N2), 0.0)
        tot += float(np.sum(F * (w - 1.0)))
    return 2.0 * tot

if __name__ == "__main__":
    sums = json.load(open("sums.json"))
    Ns = sorted(int(k) for k in sums)
    U = np.array([sums[str(n)][0] for n in Ns])
    sq = np.sqrt(Ns); ln = np.log(Ns)
    X = np.column_stack([sq, ln, np.ones(len(Ns))])
    cal = [Ns.index(n) for n in CAL]
    c, *_ = np.linalg.lstsq(X[cal], U[cal], rcond=None)
    a0, b0, c0 = c
    print(f"counterterm fit over {CAL}: a0={a0:.6f} b0={b0:.6f} c0={c0:.6f}")
    print("U - C(N) (BPHZ finite part check):")
    for n, u in zip(Ns, U):
        print(f"  N={n:3d} Vbphz={u-(a0*math.sqrt(n)+b0*math.log(n)+c0):+.6f}")
    print("D(N) = R_smooth(N):")
    Ds = {}
    for n in Ns:
        d = DN(n)
        Ds[n] = d
        print(f"  N={n:3d} D(N)={d:+.6f}", flush=True)
    json.dump({"a0": a0, "b0": b0, "c0": c0,
               "V": {str(n): float(u - (a0*math.sqrt(n) + b0*math.log(n) + c0))
                     for n, u in zip(Ns, U)},
               "D": {str(n): v for n, v in Ds.items()}}, open("D_values.json", "w"), indent=1)
