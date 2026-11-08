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

Run `python verify.py` from the directory containing the attached file. The checker uses Python's standard library for all exact enumerations and formal coefficient arithmetic, and `mpmath` for a high-precision numeric root and constant. It checks the defining maps independently of the three-gap formula for every chain length \(0\le n\le11\); validates the first \(33\) algebraic-series coefficients by exact rational recurrence and the squared polynomial identity; and separately enumerates the gap construction through \(n=6\). A successful execution ends with `VERIFY_OK`.

The direct map census checks increasing bijections between equicardinal subsets, equality of parity of every paired point, and equivalence of fence adjacency in source and image. The exact formal-series check verifies \(P(z)(1+zF(z))^2=(1-z^2)^2\) to the specified order, with \(P(z)=1-2z-3z^2+4z^3+4z^6\).

The non-computational proof is in `RESULT.md`, including the construction of the bivariate diagonal rational function, exact diagonal extraction, uniqueness of the dominant singularity, and the coefficient asymptotic. Verification for finitely many dimensions is not a proof of the infinite statement; the infinite statement follows from the algebraic derivation and singularity argument. Publication priority and independent validation have not been established.
