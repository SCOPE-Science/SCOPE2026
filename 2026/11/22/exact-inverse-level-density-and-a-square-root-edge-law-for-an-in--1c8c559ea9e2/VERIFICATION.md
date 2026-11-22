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

# Verification details

The analytic proof uses rational independence of frequencies, the crossing-flux/coarea formula for a smooth torus level, direct cosine-sign averaging, exact sum-to-product factorization at zero, and a local quadratic expansion near an extremal phase. The smooth-level flux argument deliberately excludes zero and both endpoints; zero is treated by an exact arithmetic counting identity and the endpoints are impossible by irrationality.

Run the standalone `check.py` using Python 3 with NumPy and SciPy. It compares deterministic sign-change counts in finite input windows with independent numerical quadratures; these checks cannot prove convergence, exhaustive real-root counts, or originality. A numerical checker cannot certify infinite-quantifier claims.
