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
The exact analytic eigenvalue formula is derived in `RESULT.md` from the normalized Bergman monomial orthonormal basis. The rational outer-annulus constants and sign comparisons were checked using exact fractions. The asymptotic all-index exclusion relies on proof in `RESULT.md`, not on a finite sample or a timeout.

To reproduce the supplementary checks, run `python3 check.py` from the package directory (Python 3 standard library only). The script verifies the algebraic root bracket, the finite set of rational strict inequalities, the finite rational signs, and high-precision representative large-degree ties for degrees 10, 20, 40, 80, and 160. It makes no independent certification claim.

The general mode-jump theorem is for all sufficiently large integers, not a numerically determined first admissible degree. Potential historical priority gaps are discussed in `REVIEW.md`.
