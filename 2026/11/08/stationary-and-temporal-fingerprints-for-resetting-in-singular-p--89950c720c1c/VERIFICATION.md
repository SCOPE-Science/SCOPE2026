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

Run `python checks/check_theorem.py` with NumPy, SciPy and SymPy. The checker performed symbolic equalities for the radial-to-squared-Bessel generator and reset moment equations; integrated 15 stationary Bessel-density moment/normalization quantities against independent gamma-product formulas; sampled strict MLR shape comparisons over four shape pairs; checked the strict moment-ratio derivative on a parameter grid; performed an exact three-parameter inverse round trip; and simulated stationary lag pairs from the exact BESQ noncentral-chi-square transitions and exact Poisson reset-age sampling for all three conventional calculus choices. It printed a `PASS` message when run from the package.

The mathematical proof, including infinite-domain integrability, strict posterior ordering, and global injectivity, appears in `RESULT.md`. Numerical or symbolic spot checks alone do not establish uniqueness or generality. The checker requires no external data; no external certificate or independent audit is claimed.
