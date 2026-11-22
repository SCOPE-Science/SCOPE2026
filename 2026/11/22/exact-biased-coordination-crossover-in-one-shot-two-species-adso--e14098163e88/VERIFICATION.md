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

The proof in `RESULT.md` gives the infinite-volume construction, cavity ODE, conserved integral, balanced explicit solution, and dominated-convergence high-degree limit. Independently run `python check.py` with Python 3.10 or later and SciPy installed. The program emits `PASS: 296 deterministic assertions` when successful.

The executable checks numerical solutions at multiple degrees, times and biases, the exact published one-dimensional hyperbolic expression for \(z=2\), the balanced formula, the signed-coverage identity, and the minority-coefficient approach. Its separate finite-depth causal simulation provides probabilistic spot-checks, not exact infinite-volume certificates. The unproved scope includes finite-cycle corrections, repeated attempts, random graph limits, and the simultaneous small-bias / large-degree boundary layer.
