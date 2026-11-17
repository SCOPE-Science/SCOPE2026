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

# Exact reproducibility

Run `python check.py` in the same folder with Python 3 and SymPy. The checker enumerates all twenty affine permutations and every ordered subword. The resulting integral signed chain matrices in degrees one through four have dimensions \(5\times20\), \(20\times60\), \(60\times80\), and \(80\times20\). It verifies boundary composition, Smith factors and ranks, the free top-dimensional collapses, the nonexact integral two-cocycle, its affine multiplier and translation transformations, and every affine element's fixed-cell Lefschetz trace.

The exact output recorded in `verification_output.txt` is reproducible from `check.py`. The proof of the infinite-looking homotopy notation makes no infinite-family assertion: all calculations are exhaustive on this finite semisimplicial complex. Smith factors are computed exactly over the integers; reductions modulo a finite collection of primes would not suffice to establish the absence of torsion. The homotopy wedge additionally uses the explicit top collapses and the simply connected two-skeleton, not homology data alone.
