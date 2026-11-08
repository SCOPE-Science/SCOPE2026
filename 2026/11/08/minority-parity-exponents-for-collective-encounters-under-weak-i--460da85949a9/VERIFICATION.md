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

## Actual verification

The source checker `check_phase_barrier.py` was executed from the package source path using Python, NumPy and SymPy and returned `PASS 179 deterministic verification assertions`. It compares exact symbolic first-passage equations, the star mean, the positive-root derivative polynomial, the first-order asymptotic and matrix inversions for several leaf counts and reset probabilities. It also tests the discounted hitting transform, the restart identity, and rare-exponent convergence for two to four walkers on stars, a path and an even cycle.

## Proof coverage and limits

The matrix checks independently test finite parameter instances but do not constitute an infinite-dimensional, arbitrary-graph or asymptotic proof. The proof relies on the explicit parity-count lower bound, a positive prescribed-path lower bound, analyticity of the discounted finite Markov resolvent, and the renewal transform's small-success asymptotics. Coefficient determination for a general graph requires finite matrix construction and differentiation. No external independent audit or certification is asserted.
