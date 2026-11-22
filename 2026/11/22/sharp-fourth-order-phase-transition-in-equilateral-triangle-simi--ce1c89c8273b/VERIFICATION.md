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

# Reproducibility and limits

Execute `python3 CHECK.py` using Python 3's standard library. The script evaluates the complete similarity-translation fiber integral from the actual transformed triangle vertex coordinates on a two-dimensional midpoint grid. It also evaluates the derived fundamental-sector integral using piecewise Simpson quadrature. Ten aspect ratios across the threshold were checked against the claimed exact branch expression, with successful execution and explicit tolerances. Independently, exact symbolic integration of the stated polynomial double integral and algebraic differentiation were checked during derivation. Neither numerical grid nor finite sample checks prove the all-real theorem; the full proof is provided in `RESULT.md`.

The first public motivating-source date is the 2026-11-05 arXiv v1 submission. The previously published two-dimensional footprint and triangle-target volume results are explicitly distinguished; no claim of exhaustive priority or independent certification is made.
