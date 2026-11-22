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

# Verification and limits

The analytical proof derives independent order-ratios from exponential order statistics and proves the local indicator process is one-dependent. It evaluates the leading coefficient from an integral, bounds the one- and two-point remainder terms, invokes a cited standard local-dependence Poisson-process theorem, and passes to the continuum by Riemann sums. The supercritical regime uses a second-moment bound and monotone shape-parameter coupling. These steps, not numerical experiments, justify the infinite assertions.

The standalone `CHECK.py` was executed successfully: `PASS 13315 deterministic/seeded checks`. It checks finite exact inequalities against numerical quadrature, tests a finite combinatorial characterization, checks the adjacent-event bound and runs seeded Monte Carlo diagnostics. Numerical evidence is not a proof of the Poisson limit or mathematical novelty. No independent audit has been performed.
