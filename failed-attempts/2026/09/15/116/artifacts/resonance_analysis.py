"""Resonance audit for a tower-Liouville frequency in d=3 (log-scale only).

alpha = (L, sqrt(2)-1, sqrt(3)-1), L = sum_{t>=1} 2^{-m_t}, m_1=2, m_{t+1}=2^{m_t}.
k_j=(q_j,0,0), q_j=2^{m_j}. delta_j := ||q_j L|| = T_j < 2*2^{-(m_{j+1}-m_j)}.

j=1,2: exact dyadic arithmetic via Fraction (small ints only).
j>=3: log-scale rigorous bounds only (m_4 = 2^65536 overflows float).
"""
import json
import math
from fractions import Fraction

LOG10_2 = math.log10(2.0)
M1, M2, M3 = 2, 4, 16
E4 = 65536  # m_4 = 2^E4

S3 = sum(Fraction(1, 2**m) for m in (M1, M2, M3))

rows = []
for j, Mj in ((1, M1), (2, M2)):
    q = 2 ** Mj
    frac = (q * S3) % 1
    d = min(frac, 1 - frac)
    assert d < Fraction(1, 2)
    # omitted tail q_j*sum_{t>=4} 2^{-m_t} <= 2*2^{m_j-m_4}; in log10 this is
    # (m_j+1-m_4)*log10(2) with m_4 = 2^65536 ~ 10^19728.3, hence < -10^19728.
    # Compare via logs: m_4 > 10^19728, so tail_log10 < -10^19728 << -1e6.
    # (No float conversion of m_4 itself.)
    tail_log10_ub = -1e19728 if False else None
    assert (1 << E4) > 10**19728  # int arithmetic only; proves tail << -1e6
    dfloat = float(d)
    rows.append({"j": j, "q": q, "delta": dfloat,
                 "log10_inv_delta": -math.log10(dfloat),
                 "K": math.log(1.0 / dfloat) / q,
                 "fourier_log10": -q / math.log(10),
                 "omitted_tail_comment": "rigorously 0 at all printed digits"})
    print(rows[-1])

# j=3: delta_3 <= 2^{-(m_4-m_3-1)}; write everything in log scale.
# log10(m_4) = 65536*log10(2) ~ 19728.3, so log10(1/delta_3) ~ 10^19728.3
# (double-exponential). The int m_4 itself is never converted to float.
scale = E4 * LOG10_2  # ~19728.3
print("log10(m_4) =", scale)
print("log10(1/delta_3) lower bound ~ 10^%.2f (double-exponential)" % scale)
print("i.e. log10(1/delta_3) >= (m_4-m_3-1)*log10(2) with m_4 = 2^65536")
K3_log10_lb = (E4 - M3) * LOG10_2 + math.log10(math.log(2.0))
print("log10(K_3 lower bound) =", K3_log10_lb)
q3 = 2 ** M3
c3_log10 = -q3 / math.log(10)
print("q_3 =", q3, "fourier log10 =", c3_log10)

for lam in (0.1, 0.01, 0.001):
    vals = [round(math.log10(r["delta"]) - math.log10(lam) - r["fourier_log10"], 4)
            for r in rows]
    print("lam=%g log10(delta/(lam*c)) j=1,2:" % lam, vals,
          " j=3: hugely NEGATIVE (non-perturbative at every fixed lam)")

gap = {str(lam): lam * sum(10 ** r["fourier_log10"] for r in rows)
       for lam in (0.1, 0.01, 0.001)}
print("gap-sum j=1,2:", gap)

with open("output/artifacts/resonance_table.json", "w") as f:
    json.dump({"rows": rows, "K3_log10_lb": K3_log10_lb,
               "c3_log10": c3_log10, "gap_sums": gap,
               "log10_m4": scale}, f, indent=1)
print("wrote output/artifacts/resonance_table.json")
