"""Delsarte LP for binary codes, solved with the numpy-only simplex.

Primal (bound on code size M for given n,d):
  vars a_1..a_n (A_0 = 1 fixed, A_i = 0 for 1<=i<d, A_i = a_i for i>=d).
  max  sum_{i>=d} a_i        (so M = 1 + obj)
  s.t. for each k=1..n:  sum_{i>=d} K_k(i) a_i >= -C(n,k)     [Delsarte: B_k>=0]
       a_i >= 0.
  i.e. with c = ones, Amat[k,i] = -K_k(i), b = C(n,k):  max c.a s.t. Amat a <= b, a>=0.

Dual (min b.y s.t. Amat^T y >= c, y>=0):
  min  sum_k C(n,k) y_k   s.t.  for each i>=d: sum_k -K_k(i) y_k >= 1, y>=0.
  i.e.  sum_k K_k(i) y_k <= -1 for all i in [d..n].  Then M <= 1 + b.y.

Certificate recorded: float y plus exact (Fraction) verification of the
dual constraints. To get an EXACT rational certificate whose violation can be
checked in integers, we round y to rationals with denominator D and verify
  sum_k K_k(i) * (Ynum_k) <= -D   for all i>=d,  Ynum>=0,
giving the rigorous bound  M <= 1 + sum_k C(n,k) Ynum_k / D.

n=36, d=14 is the target; we also audit (36,13) and small cases.
"""
import json
import os
import numpy as np
from math import comb
from fractions import Fraction
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from simplex import simplex_le


def krawtchouk(n):
    K = np.zeros((n + 1, n + 1))
    C = [[comb(a, b) if 0 <= b <= a else 0 for b in range(n + 1)] for a in range(n + 1)]
    for k in range(n + 1):
        for i in range(n + 1):
            s = 0
            for j in range(k + 1):
                s += ((-1) ** j) * C[i][j] * C[n - i][k - j]
            K[k, i] = s
    return K


def delsarte(n, d, verbose=True):
    K = krawtchouk(n)
    idx = list(range(d, n + 1))          # primal var positions
    p = len(idx)
    c = np.ones(p)
    Amat = np.zeros((n, p))
    b = np.zeros(n)
    for r, k in enumerate(range(1, n + 1)):
        b[r] = comb(n, k)
        for s, i in enumerate(idx):
            Amat[r, s] = -K[k, i]
    res = simplex_le(c, Amat, b)
    a = res["x"]
    y = res["y"]                          # dual vars y_1..y_n
    M = 1.0 + res["obj"]
    if verbose:
        print(f"Delsarte(n={n},d={d}): LP obj(sum A_i)={res['obj']:.10f} -> M<={M:.10f}")
        print(f"  nonzero dual y_k: {[(k+1, round(float(v),10)) for k,v in enumerate(y) if v>1e-9]}")
        print(f"  nonzero A_i: {[(i, round(float(v),6)) for i,v in zip(idx,a) if v>1e-9]}")
    return {"n": n, "d": d, "obj": res["obj"], "M": M, "a": a, "y": y, "idx": idx, "K": K}


def rationalize_certificate(n, d, y, idx, start_D=10**6, tries=(10**6, 10**7, 10**8)):
    """Round y up to rationals with denominator D; verify exact dual constraints.
    Because constraints are sum K_k(i) y_k <= -1 with possibly negative K, we
    round each y_k UP (ceil) so that... careful: K_k(i) can be negative, so
    ceil does not preserve the inequality direction. Instead: take Ynum=ceil(D*y),
    then EXACTLY check sum K_k(i) Ynum_k <= -D for every i>=d using integers.
    If some i fails, increase D / scale up and re-check (searches a true feasible
    rational point near the float optimum by uniform inflation: multiply by (1+eps)).
    """
    K = krawtchouk(n)
    Kint = np.round(K).astype(int)
    Cnk = [comb(n, k) for k in range(n + 1)]
    y = np.array(y, float)
    for D in tries:
        for infl in [1.0, 1.001, 1.005, 1.02, 1.05, 1.1, 1.2]:
            Ynum = np.ceil(D * infl * y - 1e-9).astype(int)
            Ynum = np.maximum(Ynum, 0)
            ok = True
            worst = 0
            for i in idx:
                s = int(sum(Kint[k, i] * Ynum[k - 1] for k in range(1, n + 1)))
                if s > -D:
                    ok = False
                    worst = max(worst, s + D)
            if ok:
                num = int(sum(Cnk[k] * Ynum[k - 1] for k in range(1, n + 1)))
                return {"D": D, "infl": infl, "Ynum": Ynum.tolist(),
                        "bound_num": num, "M_num": num + D, "M_den": D,
                        "M_float": (num + D) / D}
    return None


if __name__ == "__main__":
    out = {}
    for (n, d) in [(36, 14), (36, 13), (36, 15), (36, 16), (33, 14), (34, 15), (22, 7), (22, 8)]:
        r = delsarte(n, d)
        cert = rationalize_certificate(n, d, r["y"], r["idx"])
        print(f"  rational cert: {cert['M_num']}/{cert['M_den']} = {cert['M_float']:.6f} "
              f"(D={cert['D']}, infl={cert['infl']})" if cert else "  NO rational cert found")
        out[f"{n}_{d}"] = {"M_float": r["M"], "obj": r["obj"],
                           "dual_y": [float(v) for v in r["y"]],
                           "A": [float(v) for v in r["a"]], "idx": r["idx"],
                           "cert": cert}
    with open(os.path.join(HERE, "delsarte_results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("wrote delsarte_results.json")
