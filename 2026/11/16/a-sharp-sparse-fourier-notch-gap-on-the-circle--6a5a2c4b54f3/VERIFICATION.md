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

The exact reproducible algebraic checks are in `CHECK.py` and need Python 3.10 or later plus SymPy from `requirements.txt`. They check the degree-six Chebyshev expansion of the dual polynomial, its roots and signs, the rational/radical quadrature equations, sixth cosine moment, and the nonzero sine-system determinant. Execute `python CHECK.py` in this folder. Expected terminal output begins with `CHECK_OK`.

The infinite-dimensional part of the theorem is proved by integration of a pointwise nonnegative polynomial against an arbitrary positive Borel measure, combined with elementary moment constraints; it is not an exhaustive computation of arbitrary measures. Equality classification uses a finite exact determinant rather than numerical condition estimates. This verification is an algebraic replay of the written proof and is not independent external validation.
