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

# Mathematical verification and limits

The analytical result is proved by a normalized invariant phase distribution, explicit solution of a finite-state Poisson corrector and a martingale bracket calculation. The derivative and baseline enhancement are exact rational identities with quadratic numerators; the distinct stage-count cutoffs follow from strict monotonicity of a hyperbolic quotient. The small symbolically checked tests are not substitutes for those analytic proofs.

Run `python CHECKER.py` with Python 3 and SymPy installed. The checker solves the finite Markov Poisson equation independently at exact rational rate tuples in six stage counts, computes the asymptotic variance rate directly from the corrected jumps, and tests the proposed expression. It also verifies symbolic derivative and enhancement factorizations and representative threshold inequalities. The completed test run reported `PASS: 40 independent exact rational and symbolic checks`.

The scope excludes interacting motors, arbitrary multiple kinetic defects, modified local forward/backward affinity, external bath-energy costs, and any inference about experimental noise. No independent scientific review has been performed.
