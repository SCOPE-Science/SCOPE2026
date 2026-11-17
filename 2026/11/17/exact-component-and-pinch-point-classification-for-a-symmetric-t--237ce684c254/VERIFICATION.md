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

# Reproducibility and verification

Execute `python3 verify.py` using only Python 3's standard library, in the same directory as the result. Expected output: `EQUILATERAL_ANISOTROPIC_EXACT_CHECKS_OK 86778`.

The checker compares the original three positive-definite quadratic costs with the independently written proposed polyhedral conditions, for 12 distinct exact rational parameters and an 85-by-85 grid of exact rational coordinates. It also checks exactly located multiple-site ties, each proposed pinch junction and the normalized shoelace area of the finite core. A second direct derivation in the accompanying proof establishes the algebraic factorization and all topological claims for every positive real parameter. Finite enumeration and exact arithmetic at sampled points do not certify the entire continuum.

The result is a theorem about a precisely symmetric, full-plane model with coincident boundaries retained in both cells. Historical originality remains provisional; no independent audit has been performed.
