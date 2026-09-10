"""Finite-truncation search: can phi2(x;y2)=P(x-y2) isolate singletons?
For a row B=(b_0..b_{m-1}) (rationals) and each k, need c_k with
  (c_k - b_k) in PSET={2^n} and (c_k - b_i) not in PSET for i!=k.
Search small integer B's and bounded c range. Reports witness tables.
This tests ONLY the pre-Ramsey (ii)+(iii) finite approximation for phi2 alone
(does not assert full ICT pattern, which additionally needs mutual indiscernibility).
"""
from fractions import Fraction

PSET = {Fraction(2**n) for n in range(12)}

def isolates(B, clo, chi):
    """For each k, find c in [clo,chi] (integer steps) isolating k. Return dict."""
    B = [Fraction(b) for b in B]
    out = {}
    for k in range(len(B)):
        wits = []
        c = Fraction(clo)
        while c <= chi:
            if (c - B[k]) in PSET and all((c - B[i]) not in PSET for i in range(len(B)) if i != k):
                wits.append(c)
            c += 1
        out[k] = wits
    return out

cases = [
    [0, 1],
    [0, 1, 2],
    [0, 3],
    [0, 2, 6],
    [0, 5, 6],
]
for B in cases:
    res = isolates(B, -4, 40)
    print("B =", B)
    for k, w in res.items():
        print(f"  k={k}: witnesses={ [str(x) for x in w[:8]] }{'...' if len(w)>8 else ''} (n={len(w)})")
    ok = all(len(w) > 0 for w in res.values())
    print("  isolates-all:", ok)
print("PHI2_FINITE_SEARCH_DONE")
