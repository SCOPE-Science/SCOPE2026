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

The mathematical proof uses conditional Itô isometry, Brownian scaling, the singular-endpoint dominated-convergence lemma, and a Gaussian negative-moment criterion. These steps apply to every fixed positive stiffness power; no finite-time sampling is used to infer an infinite-time theorem.

The standalone file `verify.py` was executed with Python and SciPy. It passed 16 deterministic checks: nine conditional-variance integral comparisons on a known continuous endpoint path, three Gaussian-mixture characteristic-function comparisons for the quadratic model, three tail-prefactor comparisons, and one exact Cauchy-prefactor identity. All comparisons are independent checks of constants and transformations, not certificates of novelty or infinite-time convergence.

Reproduce using `python verify.py` with SciPy installed. Initial paths, the Brownian environmental path and the white thermal noise are precisely normalized in `RESULT.md`. The available calculations provide no independent review or external certification.
