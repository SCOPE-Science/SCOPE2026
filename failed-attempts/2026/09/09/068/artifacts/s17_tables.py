"""Step 17: explicit shortened enumerators for k=1..5 (from unique balanced profiles).
For each k: n0(w) = C(72-w,k)/C(72,k)*A_w (weight-w words vanishing on S).
Shortened Ck [72-k,36-k]: A'[w]=n0(w). Verify: integrality, sum=2^(36-k),
min distance, and MacWilliams dual spectrum nonnegativity/integrality.
Writes s17_tables.json + prints tables.
"""
from math import comb
from fractions import Fraction
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
out = {}
for k in [1, 2, 3, 4, 5]:
    D = comb(72, k)
    Ap = {}
    for w in range(73 - k):
        num = comb(72 - w, k) * A[w] if A[w] else 0
        assert num % D == 0, (k, w)
        Ap[w] = num // D
    s = sum(Ap.values())
    assert s == 2 ** (36 - k), (k, s)
    d = next(w for w in range(1, 73 - k) if Ap[w] != 0)
    # dual spectrum via Krawtchouk n=72-k, dim=36-k
    n = 72 - k
    B = {}
    for j in range(n + 1):
        t = Fraction(0)
        for w in range(n + 1):
            if Ap[w]:
                kk = sum(Fraction((-1) ** u) * comb(w, u) * comb(n - w, j - u)
                         for u in range(n + 1) if 0 <= u <= w and 0 <= j - u <= n - w)
                t += Ap[w] * kk
        t //= Fraction(2 ** (36 - k))
        assert t.denominator == 1 and t >= 0, (k, j, t)
        B[j] = int(t)
    assert sum(B.values()) == 2 ** 36
    dd = next(j for j in range(1, n + 1) if B[j] != 0)
    print(f"k={k}: [{n},{36-k}] sum=2^{36-k} OK; d={d}; dual-dist={dd}; "
          f"A'16={Ap.get(16,0)} A'20={Ap.get(20,0)} A'36={Ap.get(36,0)}")
    out[k] = {"A": Ap, "dual_dist": dd, "min_dist": d}
json.dump({str(k): {"A": {str(w): out[k]["A"][w] for w in out[k]["A"]},
                    "min_dist": out[k]["min_dist"], "dual_dist": out[k]["dual_dist"]}
           for k in out}, open(os.path.join(HERE, "s17_tables.json"), "w"), indent=1)
print("wrote s17_tables.json")
