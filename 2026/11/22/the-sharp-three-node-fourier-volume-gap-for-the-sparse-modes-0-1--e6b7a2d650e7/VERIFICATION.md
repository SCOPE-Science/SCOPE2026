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

# Verification

**Analytic:** Derive the cubic discriminant and Schur factor, optimize the concave quadratic angular parameter, use exact derivative factorizations and rational upper bounds on the two excluded branches, and reconstruct the unique equality orbit using the normalized root polynomial. The compact domain and boundary cases (repeated nodes, zero symmetric sum, and tightness equality) are included.

**Reproducibility:** Run `python CHECK.py` using only the standard library; the saved checker prints `CHECKS_PASSED 62453`, root and determinant approximations. It verifies polynomial derivative identities exactly with rational arithmetic and applies independent determinant tests, a dense two-angle grid, and symmetry orbit tests. These sampled checks do not establish continuum or independent certification.

**Source comparison:** Full scientific result texts of two closest three-coset Fourier determinant papers were read, while the motivating November 2026 article was available only as a publisher abstract/bibliography. Research novelty remains conditional on accessible literature. The check does not certify publication priority.
