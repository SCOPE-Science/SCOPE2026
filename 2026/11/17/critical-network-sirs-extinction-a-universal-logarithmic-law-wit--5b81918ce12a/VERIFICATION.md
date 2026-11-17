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

# Verification and reproducibility

The theorem is proved analytically in `RESULT.md`: positivity and global threshold extinction, spectral projection, exponentially damped stable convolutions, the exact quadratic/cubic vector-field expansion, and integration of the reciprocal Perron amplitude. Each limit is explicitly an infinite-time mathematical claim proved there, not inferred from sampled trajectories.

`checks/check.py` is standalone with Python and SymPy for exact symbolic verification. It checks the two-node Perron normalization, projected linear equation, immunity slaving, cubic coefficient, exact rational signs at two waning rates, and second-order invariance. Optional NumPy/SciPy trajectories check finite-time residual slopes; they are not exhaustive or proofs. The checker was executed successfully on these sources and returned the exact and supplemental check passes.

The full result holds for all nonzero admissible infected seeds and strictly positive recovery/waning rates at exact spectral criticality. The coefficient's first-public motivating source date is documented from arXiv v1 (2026-04-22). An independent audit has not been performed.
