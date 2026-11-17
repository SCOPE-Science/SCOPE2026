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

The analytical reconstruction is in `RESULT.md`. The embedded `check.py` is self-contained and uses Python standard-library `fractions.Fraction` to test the exact mass, frequency, entropy, skew-square and quadratic-splitting identities. It evaluates 60 parameter/state settings and uses fourth-order Runge–Kutta integration for two asymmetry regimes, checking the convergence of the phase-corrected nonzero vector at three late times. Run `python3 check.py` to reproduce. Finite tests are supporting diagnostics; the theorem's quantifiers are certified only by the written proof, not numerical samples. No proof is offered off the balanced parameter surface, for vanishing mutation, or for stochastic versions.
