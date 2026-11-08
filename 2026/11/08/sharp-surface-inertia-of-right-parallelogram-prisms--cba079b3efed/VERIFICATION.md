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

Run `python verify.py` with SymPy and NumPy. The script confirms the exact polynomial decomposition and the equality case symbolically, then independently integrates all six faces at 5-point Gauss–Legendre accuracy on 4,000 fixed-seed positive-parameter prisms. Since each face integrand is quadratic, Gauss–Legendre quadrature is exact in exact arithmetic; in floating point, the stated tolerances allow rounding. The proof covers all real admissible parameters without reliance on samples. Source-date limitation: manuscript dated December 19, 2007 and contemporaneous journal volume 2007, but original online release day not independently established. No external mathematical certification was requested or performed.
