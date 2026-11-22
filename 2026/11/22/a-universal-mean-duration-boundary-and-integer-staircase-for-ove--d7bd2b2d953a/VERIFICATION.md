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
# Reproducibility and limitations
Run `python verify.py` using an ordinary Python 3 installation (standard library only). The verifier prints `CHECKS_PASSED 67326` and exits normally. It uses reproducible seeded random inequalities and deterministic transition bisections for exponential and gamma event durations. It tests the zero-derivative bracket, count optimality from the relaxed optimizer, and an explicit \(P=12\), \(B=8\), \(h=1/2\), \(L\sim\mathrm{Exp}(1)\) example.

The mathematical proof, independent of numerical testing, is in `RESULT.md`. The crucial steps are the exact gap formula, strict Jensen equality conditions, the negative relaxed-count second derivative, and a strictly increasing neighboring-count difference that changes sign only if activation cost is below mean event duration. The theorem assumes positive continuous event-duration density, finite mean, uniform independent event-start phase, partial-overlap detection, and overhead measured in energy-equivalent live time; these conditions are not inferred from field observations. Finite numerical checks establish no infinite-dimensional uniqueness by themselves. No independent external audit has occurred.
