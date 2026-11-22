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

The all-degree proof is the fixed-point computation in `RESULT.md` and does not rely on finite extrapolation. The standalone `verify_orbits.py` uses only Python's standard library and is invoked as `python verify_orbits.py`. Its output is recorded in `verification_output.txt`.

The verifier exhaustively constructs every partial injection preserving cyclic order for \(n=3,4,5,6,7\), checks all \(2n\) group elements against the claimed rank-wise fixed-point polynomials, and for \(n=3,4,5,6\) constructs the disjoint group orbits independently. The verification extends the agreement of the rank and total symbolic Burnside formulas to \(n=18\), but does not claim this finite cutoff proves the general theorem. The original 2000 monoid article was not inspected beyond its abstract, and no independent historical-priority or mathematical audit has been performed.
