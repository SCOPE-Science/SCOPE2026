#!/usr/bin/env python3
"""Bounded recovery test: bidegree consistency of the d5 alternative for the beta_{3/3} lift.

Target (p=3, W=S/9): b lifts beta_{3/3}; d5(b) is claimed zero or a nonzero class in
(s, t-s) = (7, 45). This script checks, by exact integer arithmetic, whether any
Adams-Novikov differential from the lift's bidegree can reach the specified target,
exhausting d_r for r=2..9 and validating conventions against beta_{1/1}.
"""
p = 3

def beta_bidegree(i, j):
    # Greek letter beta_{i/j}: s=2, t = 2i(p^2-1) - 2j(p-1); stem = t - s.
    s = 2
    t = 2 * i * (p ** 2 - 1) - 2 * j * (p - 1)
    return (s, t, t - s)

def diff_image(s, t, r):
    # d_r: (s,t) -> (s+r, t+r-1)
    return (s + r, t + r - 1)

def diff_preimage(S, T, r):
    # unique source (s,t) with d_r(s,t) = (S,T)
    return (S - r, T - r + 1)

report = []
ok = True

# 0. Sanity: beta_{1/1} must be stem 10 (known beta_1 at p=3).
b11 = beta_bidegree(1, 1)
report.append(f"beta_1/1 bidegree (s,t,stem) = {b11} (expect (2,12,10))")
assert b11 == (2, 12, 10), "convention check failed"
report.append("sanity PASS: beta_{1/1} stem is 10, degree formula validated")

# 1. beta_{3/3} bidegree.
b33 = beta_bidegree(3, 3)
report.append(f"beta_3/3 bidegree (s,t,stem) = {b33} (expect (2,36,34))")
assert b33 == (2, 36, 34)

# 2. d5 image of the lift vs specified nonzero target (s=7, t-s=45) i.e. (S,T)=(7,52).
img5 = diff_image(*b33[:2], 5)
report.append(f"d5(beta_3/3 lift): (S,T) = {img5}, (s,t-s) = {(img5[0], img5[1]-img5[0])} (expect (7,40)/(7,33))")
assert img5 == (7, 40)
pre5 = diff_preimage(7, 52, 5)
report.append(f"unique d5 preimage of (s,t-s)=(7,45) i.e. (S,T)=(7,52): (s,t,stem) = {(pre5[0], pre5[1], pre5[1]-pre5[0])} (expect (2,48,46))")
assert pre5 == (2, 48)
gap_t = pre5[1] - b33[1]
gap_stem = (pre5[1] - pre5[0]) - b33[2]
report.append(f"gap: Delta_t = {gap_t}, Delta_stem = {gap_stem} (both 12; nonzero horn unreachable)")
assert (gap_t, gap_stem) == (12, 12)

# 3. Exhaustion: images of (2,36) under all d_r, r=2..9; preimages of (7,52).
hit = False
for r in range(2, 10):
    im = diff_image(*b33[:2], r)
    stem = im[1] - im[0]
    report.append(f"  d_{r} image of (2,36): (S,T)={im} stem={stem}")
    assert stem == 33, "stem must drop by exactly 1"
    if im == (7, 52):
        hit = True
    pr = diff_preimage(7, 52, r)
    report.append(f"  d_{r} preimage of (7,52): (s,t)={pr}")
    assert pr != (2, 36), "no differential preimage coincides with the lift"
assert not hit
report.append("exhaustion PASS: no d_r (r=2..9) sends (2,36) to (7,52); no preimage is (2,36)")

# 4. Window membership: both bidegrees are in-window, so this is a genuine mismatch, not truncation.
for (lbl, s, t) in [("lift (2,36)", 2, 36), ("required source (2,48)", 2, 48)]:
    in_win = (0 <= s <= 3) and (28 <= t - s <= 46)
    report.append(f"  {lbl}: stem={t-s}, in window = {in_win}")
    assert in_win

report.append("VERDICT: CONFIRMED BLOCKED — nonzero horn (d5(b) in (7,45)) dimensionally impossible for any beta_{3/3} lift.")
print("\n".join(report))
