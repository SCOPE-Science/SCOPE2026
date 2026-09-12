#!/usr/bin/env python3
"""Recovery test B: TRUE diagram-level enumeration of low-twist Montesinos
knots (numerator closure, same-sign slopes, TRUE PD crossings in {17,18,19},
lengths 6,7,8), with alternating + hyperbolicity spot checks on a sample.
Run: python3 recovery_enum.py [sample_checks]
"""
import sys
import time
import warnings
warnings.filterwarnings('ignore')
import spherogram as sg
from itertools import product

SLOPES = [(1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (2, 3), (3, 2)]


def main():
    t0 = time.time()
    knot_diags = []  # (combo, n)
    for r in (6, 7, 8):
        for combo in product(SLOPES, repeat=r):
            ts = [sg.RationalTangle(p, q) for p, q in combo]
            S = ts[0]
            for t in ts[1:]:
                S = S + t
            try:
                L = S.numerator_closure()
            except Exception:
                continue
            n = len(L.crossings)
            if n in (17, 18, 19) and len(L.link_components) == 1:
                knot_diags.append((combo, n))
        print(f"r={r}: knot diagrams cumulative={len(knot_diags)} "
              f"t={time.time()-t0:.1f}s", flush=True)
    print("TOTAL knot diagrams (ordered, true PD 17-19):", len(knot_diags))
    if len(sys.argv) > 1 and sys.argv[1] == 'sample_checks':
        import random
        random.seed(1327)
        samp = random.sample(knot_diags, min(12, len(knot_diags)))
        for combo, n in samp:
            ts = [sg.RationalTangle(p, q) for p, q in combo]
            S = ts[0]
            for t in ts[1:]:
                S = S + t
            L = S.numerator_closure()
            try:
                M = L.exterior()
                vol = M.volume()
                print(combo, 'PD=', n, 'alt=', L.is_alternating(),
                      'sol=', M.solution_type(),
                      'vol=%.4f' % vol, 'sym=', M.symmetry_group(),
                      'canon_tet=', M._canonical_cells_are_tetrahedra())
            except Exception as e:
                print(combo, 'PD=', n, 'EXTERIOR-ERR', str(e)[:120])


if __name__ == '__main__':
    main()
