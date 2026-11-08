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

# Reproducibility

Run `python verify_energy.py` using Python 3 and SymPy. The checker verifies both generator-based and coordinate-based moment recursions in 30 exact-rational parameter pairs, each through the sixth-order position moment; checks analytic variance and third-moment factorizations; verifies beta moment limits at dimensions one and two; checks symbolic thermal cumulance identities and the coefficient sign pattern for Descartes' rule; and numerically computes the unique double root. An executable checker does not validate a universal inequality by enumeration; the universal sign claims are proved in RESULT.md.

The numerical double-zero values are approximations. Global uniqueness relies on strict monotonicity in thermal strength, positive end limits, and Descartes' rule, not on a numeric root finder. Non-uniqueness of the zero-tumble invariant law is avoided by requiring strictly positive tumbling rate.
