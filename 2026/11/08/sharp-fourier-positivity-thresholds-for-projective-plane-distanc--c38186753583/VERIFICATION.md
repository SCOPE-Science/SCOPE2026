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

Run `python check.py` in an environment with Python 3, NumPy and SciPy. The script uses modular arithmetic to construct the point and line sets of \(\mathrm{PG}(2,p)\) for \(p=2,3,5,7\), checks the exact integer identities \(BB^T=pI+J\), computes graph shortest paths independently, calculates all eigenvalues at exponents on both sides of and at the critical value, and compares the centered inertia to the analytical values. Its dense symmetric-eigenvalue checks use absolute tolerance \(10^{-9}\). A successful replay prints `ALL_PROJECTIVE_PLANE_NEGATIVE_TYPE_CHECKS_OK`. In this package the tests completed successfully for all four fields.

The general proof is a symbolic calculation from projective-plane incidence axioms and holds for non-Desarguesian planes, which the checker does not construct. The asymptotic statement follows from a smooth inverse at the origin; no empirical extrapolation is involved. No proof assistant or independent external audit has been performed.
