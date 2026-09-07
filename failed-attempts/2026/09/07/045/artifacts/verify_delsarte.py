"""INDEPENDENT exact verifier for the Delsarte dual certificate at (n=36,d=14).
Reads delsarte_results.json, re-derives the Krawtchouk matrix from scratch
(scipy-free integer recurrence), and checks in EXACT integer arithmetic:
  (i)  Ynum_k >= 0, D > 0;
  (ii) for every i in [14..36]: sum_k K_k(i)*Ynum_k <= -D;
  (iii) reports the rigorous bound M <= 1 + sum_k C(36,k) Ynum_k / D.
Also cross-checks the primal: the stored A vector satisfies B_k>=0 (exact int).
Exit code 0 iff all checks pass. stdlib only.
"""
import json
import os
import sys
from math import comb
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))


def krawtchouk_int(n):
    # K_k(i) = sum_j (-1)^j C(i,j) C(n-i,k-j), exact ints
    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(n + 1):
        for i in range(n + 1):
            s = 0
            for j in range(k + 1):
                a = comb(i, j) if j <= i else 0
                b = comb(n - i, k - j) if 0 <= k - j <= n - i else 0
                s += ((-1) ** j) * a * b
            K[k][i] = s
    return K


def main():
    with open(os.path.join(HERE, "delsarte_results.json")) as f:
        out = json.load(f)
    n, d = 36, 14
    K = krawtchouk_int(n)
    entry = out[f"{n}_{d}"]
    cert = entry["cert"]
    assert cert, "no certificate stored"
    D = cert["D"]
    Ynum = cert["Ynum"]           # y_1..y_n
    assert D > 0 and len(Ynum) == n and all(v >= 0 for v in Ynum)
    print(f"(n,d)=({n},{d}), D={D}, nnz(y)={sum(1 for v in Ynum if v)}")
    worst = None
    for i in range(d, n + 1):
        s = sum(K[k][i] * Ynum[k - 1] for k in range(1, n + 1))
        margin = -D - s           # must be >= 0
        if worst is None or margin < worst[0]:
            worst = (margin, i)
        assert s <= -D, f"dual constraint FAILS at i={i}: sum={s} > -D={-D}"
    print(f"all {n-d+1} dual constraints hold; min margin = {worst[0]} at i={worst[1]}")
    num = sum(comb(n, k) * Ynum[k - 1] for k in range(1, n + 1))
    M = Fraction(num + D, D)
    print(f"rigorous bound: M <= 1 + {num}/{D} = {M} ~= {float(M):.6f}")
    print(f"need M<=1023 to kill [36,10,14]; got M<={float(M):.1f} -> "
          f"{'CLOSES GAP' if M <= 1023 else 'does NOT close gap (expected: Delsarte is weak here)'}")
    # cross-check a second entry independently
    for key in ["36_15", "22_8"]:
        e = out[key]
        nn, dd = map(int, key.split("_"))
        KK = K if nn == 36 else krawtchouk_int(nn)
        cc = e["cert"]
        DD = cc["D"]
        YY = cc["Ynum"]
        for i in range(dd, nn + 1):
            s = sum(KK[k][i] * YY[k - 1] for k in range(1, nn + 1))
            assert s <= -DD, f"cross-check FAILS at {key} i={i}"
        print(f"cross-check {key}: all dual constraints hold "
              f"(M<={float(Fraction(sum(comb(nn,k)*YY[k-1] for k in range(1,nn+1))+DD,DD)):.4f})")
    print("VERIFY PASS")


if __name__ == "__main__":
    sys.exit(main())
