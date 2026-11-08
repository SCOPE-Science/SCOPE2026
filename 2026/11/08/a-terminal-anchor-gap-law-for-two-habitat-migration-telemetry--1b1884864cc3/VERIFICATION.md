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

The proof uses direct likelihood differentiation, a shape theorem for the single-gap information function, constrained maximization on a simplex, and a locally unique stationary branch. The standalone `verify.py` checks these ingredients with standard-library rational and floating-point arithmetic, including exact polynomial comparisons and independent finite-path likelihood enumeration. The existence and uniqueness statements for all sufficiently large horizons, as well as the asymptotic equivalents, follow from the written proof rather than finite checks. No external or independent audit has been performed.
