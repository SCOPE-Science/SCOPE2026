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

The standalone checker `chord_fraction_verifier.py` was run with Python 3 and installed NumPy/SciPy. It compared 128 chord configurations against Cartesian segment-line intersection, tested the exact symmetry and used Gaussian quadrature of the exact conditional cumulative distribution. It returned `CROSSING_CHORD_DIVISION_CHECKS_OK`.

The limiting coefficient was also calculated analytically by the boundary-layer integral. Convergence in total variation was assessed through an explicit change of variables, almost-everywhere density convergence and Scheffé's lemma. None of these analytic conclusions is inferred solely from numerical quadrature. The full David–Fix (1964) text was unavailable; no independent validation or priority certification is asserted.
