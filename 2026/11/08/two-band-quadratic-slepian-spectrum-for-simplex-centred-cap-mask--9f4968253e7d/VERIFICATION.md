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

Execute `python check.py` with Python 3.10+, NumPy, SciPy, and SymPy in the directory containing this file. No network requests or data downloads are used. The executed package copy returned `SIMPLEX_CAP_H2_CHECKS_PASS 260`.

The source program differentiates the quartic primitive symbolically, compares the closed zonal coefficient with independent numerical integrals in dimensions 3 through 20, checks the trace and both eigenvalue bounds, checks the exact simplex Gram spectrum, and performs direct cap-by-cap spherical quadrature for the entire five-dimensional quadratic-harmonic Gram matrix in dimension three. It also integrates the nonzero cubic moment at the unique isotropic aperture. The direct spherical integration does not call the tensor formulas being corroborated.

The analytic argument in `RESULT.md` is the proof for arbitrary dimension. The program's finite evaluations, quadrature tolerances, and successful exit are not an exhaustive infinite-dimensional certificate. The independent audit channel has not been performed.
