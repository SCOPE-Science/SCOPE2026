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

## Reproduction
Run `python verify_spectrum.py` using Python 3 with SymPy and NumPy. The standalone checker expands the two critical characteristic-polynomial identities symbolically and asserts exact zero remainders. It also directly forms each complex Hermitian Bloch matrix for 20 combinations of positive decay and alternating offset and verifies all four predicted band endpoints against a 301-point frequency grid. The numerical scan is a consistency check; the global spectral claim is proved analytically in `RESULT.md` using positivity and the continuous Bloch eigenvalues.

## Scientific limits
This does not establish comparable formulas for arbitrary totally positive windows, function-norm sampling, or nonperiodic grids. No independent audit has been carried out.
