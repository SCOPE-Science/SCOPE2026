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

The theorem is supported by the explicit Poisson-equation solution and the exact partial-fraction cancellation in `RESULT.md`. Reproduce the computational checks using `python VERIFY.py` with NumPy, SciPy and SymPy; 158 assertions were satisfied for exact-rational test spectra, independent numerical density-matrix superoperators and exceptional-flux reduction.

All infinite-dimensional-looking quantifiers are finite-dimensional and arbitrary \(n\ge2\); sampled dimensions do not prove generality. The proof of the general formula uses a simple energy spectrum, equal spectral target weights, exponential probe intervals and ideal yes/no projection. The exceptional triangle fluxes require the separate two-energy calculation. The law is for the count of attempts, not physical arrival-time variance. Research priority and independent validation are not established.
