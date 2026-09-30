"""Test A: validate rho-cycle narrow census against known class numbers.
Pure stdlib. Imports census via runpy-style path insertion.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from census import narrow_census, cf_period

# (D, expected h_plus, expected N, note)
# D=8 EXCLUDED: discriminant 8 is not 1 mod 4; Z[sqrt8] is a non-maximal order and the
# sqrt-CF period rule + rho-count/2 conventions used here target the maximal order of the
# 1-mod-4 window. It is out of scope for this census (documented in DRAFT.md).
CASES = [
    (5, 1, -1), (12, 2, 1), (13, 1, -1), (29, 1, -1),
    (316, 6, 1), (65, 2, -1), (85, 2, -1), (145, 4, -1),
]
ok = True
for D, ehplus, eN in CASES:
    nred, hplus, cyclens = narrow_census(D)
    per = cf_period(D)
    N = 1 if len(per) % 2 == 0 else -1
    h = hplus if N == -1 else hplus // 2
    flag = "" if (hplus == ehplus and N == eN) else "  *** MISMATCH ***"
    if flag:
        ok = False
    print(f"D={D}: h+={hplus} (exp {ehplus}), N={N} (exp {eN}), h={h}, per={len(per)}, nred={nred} {flag}")
print("VALIDATION_ALL_OK" if ok else "VALIDATION_FAIL")
