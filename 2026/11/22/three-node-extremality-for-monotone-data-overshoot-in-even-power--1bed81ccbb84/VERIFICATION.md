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

Run `python verify.py` with Python 3.9+, SymPy and mpmath. The self-contained file uses exact rational arithmetic for finitely many grids and symbolic differentiation for the three-node profile, plus high-precision evaluation of the stationary equation. The printed PASS messages were observed on the packaged source before embedding. All infinite-grid quantifiers, the sharp universal inequality, and strict nonattainment rely on the explicit analytic argument in `RESULT.md` (Steps 1–4); finitely many tests are not exhaustive proofs.

The theorem is specific to real, nondecreasing nodal data on uniform grids, even exponents at least two and local polynomial degree one. Related historical priority and alternative terminology have not been independently certified.
