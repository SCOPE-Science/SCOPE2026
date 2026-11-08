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

The mathematical argument derives the first-passage mean from the phase-conditioned killed semigroup and a Markov-renewal equation, then proves strict near/far signs by spectral convexity and eigenvalue separation. The code `verify.py` independently calculates the first-passage mean through the matrix renewal kernel and a finite-difference backward equation.

Execution of `python verify.py` passed 432 matrix-renewal comparisons, three selected crossover parameter choices, two numerical examples and four discretized backward-equation comparisons. No assertion extrapolates finite tests to the universal theorem. The finite-difference method imposes an artificial distant reflecting boundary and has an \(O(h^2)\) grid error; it is only supplementary.

No independent mathematical or publication-priority audit has been performed. The accepted argument is a self-review.
