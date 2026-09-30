"""Exact dihedral-orbit census for the e=0 alternating 4-tangle subfamily.

Extends census_scratch: canonical orbit representative under D4 (rotation x reversal),
exact knot counts per crossing, and pair-count / traversability arithmetic.
Stdlib only.
"""
import json
from itertools import product
from census_scratch import proper_tangles, tangle_pairing, montesinos_components


def dihedral_images(t):
    n = 4
    rots = [tuple(t[(i + s) % n] for i in range(n)) for s in range(n)]
    return rots + [tuple(reversed(r)) for r in rots]


def main():
    tang = {}
    pair_cache = {}
    for c in range(2, 13):
        tang[c] = proper_tangles(c)
        for (p, q), cf in tang[c]:
            pair_cache[(p, q)] = tangle_pairing(list(cf))
    out = {}
    grand_knots = 0
    for C in (16, 17, 18):
        seen = set()
        knots = 0
        tuples = 0

        def rec(rem, parts):
            nonlocal knots, tuples
            if len(parts) == 4:
                if rem == 0:
                    for combo in product(*[tang[c] for c in parts]):
                        pairs = [pair_cache[pq] for pq, cf in combo]
                        if montesinos_components(pairs) != 1:
                            continue
                        tuples += 1
                        key = tuple(pq for pq, cf in combo)
                        canon = min(dihedral_images(key))
                        if canon not in seen:
                            seen.add(canon)
                            knots += 1
                return
            for v in range(2, rem - 2 * (3 - len(parts)) + 1):
                if v > 12:
                    continue
                parts.append(v)
                rec(rem - v, parts)
                parts.pop()

        rec(C, [])
        out[C] = {"ordered_knot_tuples": tuples, "dihedral_orbits": knots,
                  "max_fiber": None}
        grand_knots += knots
    out["total_distinct_knots_e0"] = grand_knots
    out["pairs"] = grand_knots * (grand_knots - 1) // 2
    # traversability: seconds per pair -> years for 1.9e8 pairs
    for rate in ("1s", "60s", "1ms"):
        k = {"1s": 1, "60s": 60, "1ms": 0.001}[rate]
        out[f"years_at_{rate}_per_pair"] = out["pairs"] * k / 3.154e7
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
