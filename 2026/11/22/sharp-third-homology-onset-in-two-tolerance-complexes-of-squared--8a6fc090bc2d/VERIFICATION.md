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
# Reproducibility and scope

Run `python verify.py` with Python 3 and SymPy. The script enumerates every nonempty simplex for each integer from seven through twelve directly from the deletion-based two-tolerance definition. It constructs signed boundary matrices over the exact ring \(\mathbb Z\), verifies \(\partial_3\partial_4=0\), computes Smith normal forms of \(\partial_4\) and of the canonical disjoint-triangle cycle inclusion, independently compares matrix ranks modulo two, and checks the asserted integral ranks and the first missing tetrahedra. The complete stdout of the checker is included as `verification_output.txt` and was regenerated from the embedded script. Exact matrix dimensions and the full Smith diagonal counts are in that output, not merely an aggregate PASS line.

The algebraic proof of two-connectedness and the passage from unit Smith factors to integral homotopy types are stated in `RESULT.md`. Computations are exhaustive for these six lengths only; no statement for longer cycles and no independent mathematical audit is made. The code depends on the standard SymPy exact integer Smith-normal-form implementation, and does not provide an independently implemented arbitrary-precision Smith solver.
