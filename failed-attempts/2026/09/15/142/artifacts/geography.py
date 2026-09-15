"""Bounded recovery test: geography + distinguishing-gap arithmetic for 3CP^2 # 3CPbar.

Checks: (1) target invariants; (2) canonical SW formal dimension; (3) BMY/Noether
admissibility; (4) rational-blowdown predecessor arithmetic; (5) statement of the
SW vanishing-vs-nonvanishing gap that any proof must cross.
"""
e, sig = 8, 0
b2 = e - 2  # closed simply connected: e = 2 + b2
assert b2 == 6
bp = (b2 + sig) // 2
bm = (b2 - sig) // 2
chi_h = (e + sig) / 4
c1sq = 2 * e + 3 * sig
d = (c1sq - 2 * e - 3 * sig) / 4
print(f"target: e={e} sig={sig} b2={b2} b+={bp} b-={bm} chi_h={chi_h} c1^2={c1sq} d_canon={d}")
assert (bp, bm) == (3, 3)
assert chi_h == 2.0 and c1sq == 16 and d == 0.0
# Complex-geography admissibility (necessary, not sufficient)
bmy = (c1sq <= 9 * chi_h)
noether = (c1sq >= 2 * chi_h - 6)
print(f"BMY c1^2<=9chi_h: {c1sq}<= {9*chi_h} -> {bmy}")
print(f"Noether c1^2>=2chi_h-6: {c1sq}>= {2*chi_h-6} -> {noether}")
assert bmy and noether
# Rational-blowdown predecessors: blowdown along C_p sends (e,s)->(e-(p-1), s+(p-1)).
# Invert: predecessor of (8,0) is (8+p-1, -(p-1)).
print("p -> predecessor (e', s', description):")
for p in range(2, 10):
    ep, sp = e + (p - 1), sig - (p - 1)
    b2p = ep - 2
    bpp = (b2p + sp) // 2
    bmp = (b2p - sp) // 2
    print(f"  p={p}: e'={ep} s'={sp} b+'={bpp} b-'={bmp}")
# Distinguishing gap (connected-sum theorem, standard side):
# standard 3CP2#3CPbar splits with b+>0 on both sides -> SW_std = 0.
# A proof must exhibit irreducible X, same (pi1,e,sig,parity), with SW_X != 0.
print("SW_std(3CP2#3CPbar)=0 by connected-sum theorem; need irreducible X with SW_X!=0.")
print("RESULT: arithmetic admissible, but no verified (model, configuration, SW "
      "computation) exists in-lane for any route -> TARGET BLOCKED.")
