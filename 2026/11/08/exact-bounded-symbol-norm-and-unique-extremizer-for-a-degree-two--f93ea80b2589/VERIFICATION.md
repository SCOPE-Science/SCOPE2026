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

# Reproducibility and proof checks

The symbolic theorem is proved in `RESULT.md`; the proof does not use numerical enumeration or computer-assisted certificates. The analytic check covers the unique minimizer of the Poisson-weighted distance objective, all three model-space moment conditions, the best-possible norm bound, and the equality case.

To reproduce a finite, noncertifying diagnostic run, execute `python3 CHECK.py`. It independently evaluates the weighted integrals by periodic midpoint quadrature, constructs the proposed explicit symbol, and tests its scalar moments and modulus for seven parameters. It does **not** establish infinite-parameter claims.

The formula uses normalized arc measure \(dm(e^{it})=dt/(2\pi)\), the inner-product convention linear in the first argument, and the rank-one sign convention in the cited 2026 source.

No independent audit or external mathematical validation has been performed.
