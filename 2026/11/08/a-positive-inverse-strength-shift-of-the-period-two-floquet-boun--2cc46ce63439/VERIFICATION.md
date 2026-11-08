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

# Reproducibility and mathematical scope

Run `python verify.py` with Python 3 and `mpmath` installed. The checker performs high-precision checks of algebraic identities, orbit equations, threshold root and slope, and several finite large-parameter roots of the exact multiplier equation. Expected final output includes `VERIFY_OK flip_curve_asymptotic=4 ricker_limit=1 positive_shift=1`.

The proof is analytic and covers the indicated real parameter domain. These finite checks cannot establish the global quantifiers, uniqueness, or complete historical originality. Independent scientific validation has not been performed.
