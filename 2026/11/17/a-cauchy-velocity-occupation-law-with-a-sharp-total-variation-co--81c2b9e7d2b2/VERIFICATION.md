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

Analytically proved: the first integral; global compact levels; the exact time-occupation density and independent-sign identity; the exponentially controlled \(L^1\) expansion; the sharp total-variation coefficient; the Clausen identity; and weak convergence of the marked joint law.

Reproducible finite check: `python check_cauchy.py` with Python 3, SymPy, SciPy, and mpmath. It verifies a closed derivative identity, a Clausen integral identity, and direct finite-amplitude quadratures. The checker was executed against the artifact at its packaged relative path, reporting `CAUCHY_VELOCITY_OCCUPATION_CHECK_OK`.

Finite quadrature cannot establish a theorem for all amplitudes or a limit as the amplitude diverges. No independent audit or certification is claimed.
