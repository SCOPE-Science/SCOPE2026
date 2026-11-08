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

The exact analytic checks reconstruct the two-phase stationary variances, derive independent fresh-interval and equilibrium-residual renewal formulas, and solve the resulting rational equation for the unknown Laplace transform. The only algebraically singular frequency is \(s=ar\); at that point the forward transform is distribution-independent for fixed mean, and continuity recovers the unknown Laplace-transform value. The normalizing stationary variance determines the mean before inversion.

The included `checker.py` uses independent phase-resolvent generators and exact rational arithmetic to check exponential, two-stage Erlang, and hyperexponential idle clocks, plus explicit deterministic/exponential spectral comparisons. These checks verify representative computations, not every possible law. Reproduction: `python checker.py` with an unmodified standard Python 3 interpreter. The proof, not the checker, establishes the general distribution-level statement. Independent audit: not performed.
