"""Constant-propagation scan for RSW+QM route to q=3 four-arm window.

Model: dyadic blocks with uniform bounds c0 <= pi(n,2n) <= 1-delta,
and quasi-multiplicativity constant c_QM >= 1:
  c_QM^{-1} pi(r,m) pi(m,R) <= pi(r,R) <= c_QM pi(r,m) pi(m,R).
Then over k ~ log2(R/r) blocks:
  b = log2(c_QM / c0),  a = -log2(c_QM*(1-delta))  [needs c_QM*(1-delta)<1],
  width = b - a.
Scans generous/optimistic ranges to show width<=0.5 with 0<a<b<2 is
unreachable without qualitatively new quantitative inputs.
"""
import math

def exponents(c0, delta, c_qm):
    omd = 1.0 - delta
    b = math.log(c_qm / c0) / math.log(2.0)
    if c_qm * omd >= 1.0:
        return None, b  # upper exponent non-positive: vacuous
    a = -math.log(c_qm * omd) / math.log(2.0)
    return a, b

c0_vals = [0.5, 0.25, 0.1, 0.05, 0.01, 0.001]
omd_vals = [0.9, 0.75, 0.5, 0.25, 0.1]  # 1-delta
cqm_vals = [1.0, 1.2, 1.5, 2.0, 3.0]

print(f"{'c0':>6} {'1-d':>5} {'cQM':>4} {'a':>8} {'b':>8} {'width':>8}  verdict")
best = None
for c0 in c0_vals:
    for omd in omd_vals:
        for cqm in cqm_vals:
            a, b = exponents(c0, 1.0 - omd, cqm)
            if a is None:
                verdict = "FAIL(a<=0)"
                w = float("inf")
            else:
                w = b - a
                ok = (0 < a < b < 2) and (w <= 0.5)
                verdict = "OK" if ok else "FAIL(width/range)"
                if best is None or w < best[0]:
                    best = (w, c0, omd, cqm, a, b)
            astr = "  --  " if a is None else f"{a:8.3f}"
            print(f"{c0:6.3f} {omd:5.2f} {cqm:4.1f} {astr} {b:8.3f} {w:8.3f}  {verdict}")
print("best width config:", best)
# Even the most optimistic corner (c0=0.5, 1-delta=0.1, cQM=1.0):
# a=-log2(0.1)=3.32 (violates b<2 companion / width), b=1.0, width huge or a out of range.
# No scanned combo yields 0<a<b<2 with width<=0.5 except none; check explicitly:
found = []
for c0 in c0_vals:
    for omd in omd_vals:
        for cqm in cqm_vals:
            a, b = exponents(c0, 1.0 - omd, cqm)
            if a is not None and 0 < a < b < 2 and (b - a) <= 0.5:
                found.append((c0, omd, cqm, a, b))
print("admissible combos:", found if found else "NONE in scanned grid")
