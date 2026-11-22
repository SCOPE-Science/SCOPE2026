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

# Reproduction and verification

Run `python3 verify.py` in the same directory as this document. No external package is needed. The script executes exact-form and finite-quadrature comparisons, finite-difference log-concavity checks, root brackets, and derivative-sign checks. The recorded result was 3,642 assertions passed, with dimensionless example values:

- Terminal heat: \(y_0\approx1.256431208626\), \(T_{*,0}\approx2.437511453744\).
- Cumulative heat: \(y_1\approx2.149125799907\), \(T_{*,1}\approx4.248570184265\).

The proof uses a classical marginal log-concavity theorem; the verify script does not certify that theorem or the infinite domain. In the proof, the representation of \(\phi_k\), endpoint ratio, limiting elasticity, and derivative sign are the decisive analytical steps. Reproducibility is provided for the stipulated scalar model only, not for empirical field conditions or independently reviewed priority.
