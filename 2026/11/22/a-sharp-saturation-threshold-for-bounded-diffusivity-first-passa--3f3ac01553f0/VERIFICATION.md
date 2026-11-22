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

# Verification record

The first-passage formula follows from the backward boundary-value equation with uniformly positive bounded diffusivity and natural-scale reflection. The proof in `RESULT.md` establishes global optimality via a pointwise strict convexity inequality, not via numerical fitting. The admissible class is all Borel measurable profiles whose values lie within the stated finite bounds almost everywhere and whose spatial mean is fixed.

Run `python checker.py` with NumPy, SciPy and SymPy installed. Executed checks completed successfully: exact symbolic branch and derivative identities, sixteen seeded independent instances comparing exact mean and cost with breakpoint-aware quadrature, sixteen independent bounded equality-constrained numerical optimizations, and the explicit numerical design example. The random seed is fixed in the standalone checker. The numerical comparisons are finite samples only, and make no claim of exhaustive computational verification.

The exact two-branch formulas and sharp \(C^2\)-but-not-\(C^3\) statement rely on the written analytic derivation, not those finite checks. No independent external mathematical assessment has been performed. Potential equivalent, unindexed constrained-design results remain a literature risk.
