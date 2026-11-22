---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The mathematical proof is in `RESULT.md`. The first program, `checks/check_classes.cpp`, enumerates every nonempty subset of the vertices of \(\mathrm{KG}(n,2)\) for \(n=5,6,7\), directly tests proper independence and the strong-odd neighborhood condition, compares every passing subset against the three asserted types, and independently calculates the true minimum number of color classes using exhaustive dynamic programming over vertex subsets. The output `checks/check_classes.out` records allowed-class counts \(20,41,56\), no unclassified class, and minima \(6,7,7\).

The second program, `checks/check_packings.py`, determines exact maximum triangle packing values via a binary mixed-integer model using SciPy with verified optimality status, separately constructs all no-full-star and full-star cases for orders \(5\) through \(10\), and directly verifies all color classes by disjointness and parity. Output is `checks/check_packings.out`. These implementations check different derivations of the result but do not constitute external mathematical audit.

Reproduce with `g++ -std=c++17 -O2 checks/check_classes.cpp -o check_classes && ./check_classes` and `python3 checks/check_packings.py` (Python 3 with NumPy and SciPy). No private data are needed. The infinite-order part uses the cited classical maximum-packing existence theorem, and finite experiments alone would not prove it.
