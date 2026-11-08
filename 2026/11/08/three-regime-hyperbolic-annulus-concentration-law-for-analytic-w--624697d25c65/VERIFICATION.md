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

The principal claim is the three-regime norm limit for the annulus \(1-1/U<|z|^2<1-1/(U+H(U))\), with \(H(U)/U\) tending to zero, a positive constant, or infinity. The known beta eigenvalue staircase selects a maximizing index. The analytical proof then uses uniform asymptotics of its logarithmic expression, the beta density formula, local uniform gamma-density convergence, and the independent beta--gamma representation for the wide-width regime. These facts prove the three limits for arbitrary admissible growth sequences.

The standalone Python-standard-library program `check.py` checks the beta gap and tied optimizing modes, and one critical-width gamma asymptotic example; it prints `WAVELET_ANNULUS_STAIRCASE_CHECKS_PASS 618` when successful. The finite computations corroborate the input identities and one of the regimes but cannot verify all infinite limits. The other two asymptotic regimes are established by the proof only.

No independent mathematical audit has been performed.
