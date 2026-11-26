---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification scope

The unchanged `checker.py` is a standalone Python 3.9+ finite consistency program. Its recorded successful run ends with `PASS: 19578 finite exact-arithmetic and complex-root assertions.` Its rational-arithmetic checks exercise lattice phase laws and sawtooth means for coprime integer durations. Its numerical Newton checks use a finite list of approximants to a duration ratio of \(\sqrt2\) to illustrate the classical denominator expansion and noncancellation at the sampled roots. They are neither exact root certificates nor proofs of an infinite sequence.

The main quantitative rate obstruction is analytic: at a reset epoch with fixed duration counts the mean jumps by an exact binomial probability. Stirling asymptotics along typical counts and comparison with the left limit give the limsup bound. The checker does not test or prove that bound. The weak-limit, lattice convergence, and mean-transform statements likewise use the analytic arguments in `RESULT.md`, not finite extrapolation. The denominator expansion is credited to the prior Dirichlet-polynomial result; the model-specific spectral assertion is noncancellation for the mean.
