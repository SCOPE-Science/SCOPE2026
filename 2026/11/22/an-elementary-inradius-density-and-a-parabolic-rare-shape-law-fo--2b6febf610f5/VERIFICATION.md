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

# Verification notes

The supplied `VERIFY.py` uses only Python's standard library. From the same file package, run `python3 VERIFY.py`. It compares six direct survival integrals to six density-tail integrals, verifies the density integral to within numerical quadrature tolerance, bisects the density's unique mode and checks its value, checks six endpoint normalizations, and performs four seeded angular-simplex sampling comparisons.

The scripted check prints `ALL_CHECKS_PASSED` with the supplied program when run in a standard Python 3 environment. Its finite comparisons are independent diagnostics, not exhaustive proof. Exact normalization, uniqueness, the asymptotic expansions, and conditional limit laws rest on the displayed transformations and inequalities in `RESULT.md`. The upper-shape and lower-shape total-variation claims follow from dominated convergence of the explicitly rescaled constant-density regions; no rate of convergence in total variation is asserted.

The inaccessible primary full texts remain a historical originality risk. No external independent audit was performed.
