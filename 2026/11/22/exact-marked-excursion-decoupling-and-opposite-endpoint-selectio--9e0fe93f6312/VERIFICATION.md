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

# Scientific verification

The accompanying `verify.py` is a standalone Python standard-library script. Running `python verify.py` checks an explicit two-atom Brownian example and its exact origin-mark covariance. It then constructs a finite-state, discrete nearest-neighbor search process from transition probabilities and enumerates the full time-evolving state distribution with two alternative reset sites, retaining both the first-barrier-origin and final-absorption-origin marks. The resulting conditional joint distributions agree with independently calculated one-cycle probabilities at two distinct barrier levels. A separate killed-lattice calculation tests quadratic convergence to the continuous Brownian boundary solution, and midpoint quadrature tests opposite-endpoint Beta-density scaling toward Gamma means.

These checks are numerical and discrete-model diagnostics, **not** exhaustive verification of all continuous trajectories or a substitute for the proof. The exact continuous theorem follows from the boundary-value solution, regenerative mark selection, the strong Markov property and one-sided Laplace asymptotics in `RESULT.md`. The density-layer limit assumes positive power-law endpoint behavior; the script tests one representative choice and does not establish all possible exponents numerically.

The scientific review assesses correctness, originality and value within the stated model and literature comparisons. No independent scientific audit, formal proof certification or publication-priority determination has been performed.
