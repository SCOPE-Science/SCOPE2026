"""Step K: integral SNF Kh per (h,q) block for 10_124 (independent path + torsion).
For each differential d (integer matrix, sparse), compute SNF diagonal via
fraction-free minors? Full SNF on 5000-dim matrices is heavy. Instead: for each
(h,q) block, homology H = ker(d_out)/im(d_in) over Z. Compute via SNF of the
two maps using sage-like fraction-free elimination with gcd (Kannan-Bachem style
on small blocks; big blocks: use mod-p ranks + a single large-prime check? No—
need torsion: compute SNF only where needed.
Cheaper rigorous torsion certificate: H has torsion iff ... use structure via
SNF of stacked matrices per block. Largest blocks ~1680-dim: fraction-free SNF
may be slow but let's try per-block with sympy? No sympy. Implement simple SNF
via minors/GCD for invariant factors: d1 = gcd of entries, d1*d2 = gcd of 2x2
minors... too slow for big.
Pragmatic: compute SNF with fraction-free Gauss (Bareiss) to get rank + det-factor
per block, then torsion = |det of full-rank minor|/1... Bareiss gives exact det.
Plan: for each (h,q): A = d_in (as dense small? blocks up to 1680x835 = 1.4M entries; Bareiss O(n^3) too slow).
Alternative: torsion locations are KNOWN-small (katlas says Z2 at (3,15)?,(7,21)?). Verify targeted: compute H per block via presentation matrix SNF using PARI? no. Use simple approach: Smith via row/col gcd elimination with early stop, only on blocks where mod-p rank < complex-dim suggests... Actually torsion doesn't change mod-p rank for p odd. Compare rank mod 2 vs mod odd-p: torsion Z2 reduces... rank over F2 vs Q differ iff 2-torsion present in adjacent degrees. Compute ALL block ranks mod 2 AND mod 1e9+7: discrepancies locate torsion (standard trick), then SNF only those blocks (small?).
"""
import json, sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data
from kh_stepG import build_differentials, sparse_rank
from collections import defaultdict

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    pd = parse_pd(d['10_124']['pd'])
    _, diffs = build_differentials(pd, 10, 0, 2)
    print('ndiffs=', len(diffs))
    rk2 = {}
    for (h, q) in sorted(diffs):
        rows, cols, dd = diffs[(h, q)]
        rk2[(h, q)] = sparse_rank(rows, cols, dd, 2)
    json.dump({('%d,%d' % k): v for k, v in rk2.items()}, open('output/artifacts/kh_ranks_mod2.json', 'w'))
    r7 = json.load(open('output/artifacts/kh_ranks_1000000007.json'))
    print('blocks where rank differs mod2 vs mod1e9+7:')
    for k in sorted(set(list(r7.keys()) + ['%d,%d' % kk for kk in rk2])):
        a = r7.get(k)
        kk = tuple(map(int, k.split(',')))
        b = rk2.get(kk)
        aval = a[2] if a else None
        if aval != b:
            print(k, 'mod1e9+7=', aval, 'mod2=', b)
