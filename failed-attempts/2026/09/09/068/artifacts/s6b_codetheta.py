"""Step 6b (corrected): Construction-A code-theta in modular convention.
Theta_L(q) = sum_{v in L} q^{<v,v>/2}, L = (1/sqrt2){x in Z^72 : x mod 2 in C}.
Per-coordinate: c_i=0 -> f0 = sum_n q^{n^2}; c_i=1 -> f1 = sum_m q^{(m+1/2)^2}.
Work in units u=q^{1/4}: e0(n) = (2n)^2 = 4n^2; e1(m) = (2m+1)^2.
Total exponent E (in u) divisible by 4 <=> integer power of q; Type-II weights
(0 mod 4) guarantee all E = 0 mod 4. Compare q^0..q^8 with extremal series T.
"""
from fractions import Fraction
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
T = json.load(open(os.path.join(HERE, "theta_trace.json")))["theta"]

NU = 33  # u^0..u^32  (q^0..q^8)
g0 = [Fraction(0)] * NU
g1 = [Fraction(0)] * NU
n = 0
while 4 * n * n < NU:
    g0[4 * n * n] += Fraction(1) if n == 0 else Fraction(2)
    n += 1
m = 0
while (2 * m + 1) ** 2 < NU:
    g1[(2 * m + 1) ** 2] += Fraction(2)
    m += 1
print("g0 nonzero:", [(i, int(g0[i])) for i in range(NU) if g0[i]])
print("g1 nonzero:", [(i, int(g1[i])) for i in range(NU) if g1[i]])


def mul(a, b):
    c = [Fraction(0)] * NU
    for i in range(NU):
        if a[i]:
            for j in range(NU - i):
                if b[j]:
                    c[i + j] += a[i] * b[j]
    return c


def pw(a, k):
    r = [Fraction(1)] + [Fraction(0)] * (NU - 1)
    for _ in range(k):
        r = mul(r, a)
    return r

Th = [Fraction(0)] * NU
for w in range(73):
    if A[w]:
        t = mul(pw(g0, 72 - w), pw(g1, w))
        for i in range(NU):
            Th[i] += A[w] * t[i]
odd = [i for i in range(NU) if Th[i] != 0 and i % 4 != 0]
print("code-theta u-exponents outside 4Z (must be none):", odd if odd else "none")
Cq = [int(Th[4 * n]) for n in range(9)]
print("code-theta q^0..q^8:", Cq)
print("extremal   q^0..q^8:", T)
print("MATCH:", all(Cq[n] == T[n] for n in range(9)))
json.dump({"code_theta": Cq, "match_extremal": bool(all(Cq[n] == T[n] for n in range(9)))},
          open(os.path.join(HERE, "s6b_trace.json"), "w"), indent=1)
print("wrote s6b_trace.json")
