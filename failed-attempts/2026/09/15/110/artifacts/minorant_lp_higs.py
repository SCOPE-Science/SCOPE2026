"""Rigorous LP certificate (scipy/HiGHS) for the bandlimited-minorant obstruction.

Conventions (match analytic number theory): test function phi with
supp hat{phi} subset [-Delta, Delta], i.e. ordinary-frequency bandlimit Delta.
Sampling theorem: phi(x) = sum_n c_n sinc(2*Delta*x - n), c_n = phi(n/(2Delta)).
Objective: maximize int phi(x) W(x) dx, W(x) = 1 + sin(2 pi x)/(2 pi x)
(SO(even) 1-level density), subject to phi <= 1_{[-w,w]} on a dense grid,
|c_n| <= C (box). Since phi=0 is feasible, LP optimum >= 0 always; optimum 0
means NO positive-mass minorant exists at this Delta (Route A blocked).
Beurling-Selberg analytic reference: Lebesgue minorant mass <= 2w - 1/Delta.

Runs Delta=1.0 (max unconditional natural-average support) vs Delta=2.0
(generous harmonic support). Expect 0 vs clearly positive.
"""
import numpy as np
from scipy.optimize import linprog

def W_SOeven(x):
    x = np.asarray(x, dtype=float)
    out = np.ones_like(x)
    nz = x != 0
    t = 2 * np.pi * x[nz]
    out[nz] = 1.0 + np.sin(t) / t
    return out

def sinc_mat(xs, ns, Delta):
    # basis b_n(x) = sinc(2 Delta x - n)
    U = 2.0 * Delta * xs[:, None] - ns[None, :]
    out = np.empty_like(U)
    z = (U == 0)
    nz = ~z
    out[z] = 1.0
    uu = U[nz]
    out[nz] = np.sin(np.pi * uu) / (np.pi * uu)
    return out

def run(Delta, w=0.30, M=32, extent=20.0, step=0.04, C=3.0):
    ns = np.arange(-M, M + 1)          # centers n/(2Delta) cover |x| <= M/(2Delta)
    xs = np.arange(-extent, extent + 0.5 * step, step)
    A = sinc_mat(xs, ns, Delta)
    b = np.where(np.abs(xs) <= w, 1.0, 0.0)
    qxs = np.arange(-extent, extent, 0.01)
    B = sinc_mat(qxs, ns, Delta)
    q = (B * W_SOeven(qxs)[:, None]).sum(axis=0) * 0.01
    res = linprog(-q, A_ub=A, b_ub=b, bounds=(-C, C), method='highs')
    if res.status != 0 or res.x is None:
        return dict(Delta=Delta, status=res.status, message=res.message,
                    fun=float('nan'), maxviol=float('nan'), sumabs=float('nan'))
    c = res.x
    viol = float((A @ c - b).max())
    return dict(Delta=Delta, status=res.status, message=res.message,
                fun=float(-res.fun), maxviol=viol, sumabs=float(np.abs(c).sum()),
                nvars=A.shape[1], ncon=A.shape[0],
                centers_halfwidth=M / (2 * Delta))

if __name__ == "__main__":
    for Delta in [1.0, 2.0]:
        r = run(Delta)
        print(f"Delta={Delta}: vars={r['nvars']} cons={r['ncon']} "
              f"centers|_x|<={r['centers_halfwidth']:.1f}")
        print(f"  LP optimum (weighted minorant mass) = {r['fun']:.6f}")
        print(f"  max grid violation = {r['maxviol']:.2e}, status={r['status']}")
    print("Analytic Beurling-Selberg reference: Lebesgue minorant mass <= 2w-1/Delta:")
    for Delta in [1.0, 2.0]:
        print(f"  Delta={Delta}: 2*0.30 - 1/{Delta} = {0.60-1.0/Delta:+.4f}")
