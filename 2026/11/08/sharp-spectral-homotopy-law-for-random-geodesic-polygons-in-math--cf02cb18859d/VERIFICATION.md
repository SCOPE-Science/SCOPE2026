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

# Verification scope
The analytical proof checks the universal covering-space deck sign, the exact trace identity for all integer \(m\ge3\), the Gegenbauer eigenvalue recurrence for all integer \(d\ge3\), multiplicities, absolute trace-series convergence, the Hilbert--Schmidt remainder bound, and asymptotic mode separation.

## Standalone checker
Run `python3 check_projective_polygons.py` with Python 3's standard library. The checker separately reconstructs spectral eigenvalues and compares the three-vertex specialization against a one-dimensional numerical integral in dimensions 3 through 10. It checks the finite-length error estimate for dimensions 3, 4, 5, and 8, and lengths 4, 6, and 12. It directly samples 330,000 independent ordered polygons from Gaussian sphere lifts at six dimension/length pairs; observed frequencies lie within six nominal binomial standard errors. Success ends with `PROJECTIVE_POLYGON_SPECTRAL_PARITY_OK 330000`.

## Limits
Numerical quadrature has finite precision, and Monte Carlo is stochastic. Neither proves the infinite series or asymptotic; those follow from the proof. Historical originality has not undergone independent validation. No external audit is claimed.
