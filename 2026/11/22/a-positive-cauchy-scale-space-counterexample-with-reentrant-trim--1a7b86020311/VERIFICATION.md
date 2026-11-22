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

The supplied `check_exact.py` is the complete independent-from-numerical-sampling algebraic reproduction of the four-height sign certificate. Its only nonstandard dependency is SymPy. It checks the rational derivative identity by symbolic cancellation, reconstructs the four primitive integer polynomials, evaluates rational sign witnesses, and counts sign variations. It does not infer global mode counts from a plot: Descartes' rule and strict sign brackets prove them.

The signed critical-point count on the real line follows from the exact derivative factorization and parity. The equal-weight construction uses \(249\) data points with repeated values; its pairwise-distinct extension relies on simple critical points and stability, and no explicit perturbation radius is provided.

There has been no independent mathematical audit and no assessment of inaccessible historical literature beyond the documented checks. Scientific novelty remains provisional.
