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

# Reproducibility and limitations

Run `python checker.py` from this directory with Python 3, SymPy, and mpmath. The script verifies the exact diagonal and transverse Jacobian identities symbolically, 200 independently generated parameter combinations in rational arithmetic, eight high-precision quadratures plus one exact-boundary case of the relevant logarithmic integral, exact neutral-ray instances, and the positive lower bound in sampled physical parameters. Its terminal line begins `PASS` if all assertions succeed.

The full mathematical justification, including quantifiers and both sides of the piecewise logarithmic integral, is in `RESULT.md`. The script's finite checks cannot establish ergodicity or a universal infinite-time theorem; those follow analytically using the standard doubling-map conjugacy, Birkhoff's theorem, and a justified Jensen identity. The exact positivity claim concerns the linearized antisymmetric direction for almost every initial point on the synchronized chaotic diagonal. It is not a verification of a global attracting or repelling basin.
