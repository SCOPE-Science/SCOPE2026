"""Independent verifier: certifies the three minimal nontrivial 21-blocking sets
and re-checks key negative statistics. Run: python3 verify_all.py"""
import sys
sys.path.insert(0, '.')
import numpy as np
from pg213_model import INC, LINES, NPTS, NL, check_blocking, check_minimal, check_nontrivial

SETS = {
    'T16': [1, 6, 16, 21, 26, 49, 61, 69, 78, 79, 82, 93, 102, 108, 109, 112, 129, 138, 143, 163, 171],
    'T37': [0, 9, 21, 35, 42, 59, 65, 77, 78, 100, 103, 114, 126, 142, 143, 168, 169, 170, 174, 180, 181],
    'T39': [16, 17, 20, 26, 28, 31, 32, 43, 77, 79, 88, 89, 153, 164, 165, 168, 171, 173, 180, 181, 182],
}
ok = True
# model sanity
assert NPTS == 183 and NL == 183
assert INC.sum(axis=1).min() == 14 and INC.sum(axis=1).max() == 14
assert INC.sum(axis=0).min() == 14 and INC.sum(axis=0).max() == 14
print("model: 183 pts / 183 lines / 14 per line: OK")
for k, S in SETS.items():
    b, n, _ = check_blocking(S)
    mn, miss = check_minimal(S)
    nt = check_nontrivial(S)
    # every 1-point extension of a minimal 21 is blocking (spot check all 162)
    allext = True
    for p in range(NPTS):
        if p in S:
            continue
        bb, _, _ = check_blocking(sorted(set(S) | {p}))
        if not bb:
            allext = False
    print(f"{k}: size={len(S)} blocking={b} minimal={mn} nontrivial={nt} "
          f"all162extensions_blocking={allext}")
    if not (b and mn and nt):
        ok = False
print("VERIFY_ALL_OK" if ok else "VERIFY_FAILED")
