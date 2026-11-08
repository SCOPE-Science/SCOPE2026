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

Reproduction: install NumPy and execute `python verify_chord.py` beside this file. A clean run reports `VERIFY_CHORD_OK direct_integrals=12` and the predicted fifth coefficients for harmonics 2 and 12. The script integrates tangent-angle unit vectors with an independent 40-node Gauss–Legendre rule, solves the actual chord-radius equation by 43 bisection iterations, and averages the resulting midpoint-dependent admissible arc gaps. It does not use the fifth-order expansion to compute those chord lengths.

The 12 cases cover the circle and the 2-, 4-, and 12-fold oscillatory curves at radii 0.06, 0.10, and 0.12. Absolute discrepancy between independent quadrature and the fifth-order truncation is below \(2.5\times10^{-8}\) for these fixed examples. The circle integration also agrees with the closed arcsine law to \(3\times10^{-12}\). Two harmonic curves have exactly equal cubic coefficients and opposite signs of the fifth coefficient.

The general theorem is proved analytically using centered secant expansions, local inverse monotonicity, a compactness argument excluding nonlocal small chords, and periodic integration by parts. Finite quadrature is not an infinite proof. The \(O_\Gamma(r^7)\) bound depends on derivatives of each fixed curve and is not asserted uniformly in the oscillation frequency. No independent audit was performed.
