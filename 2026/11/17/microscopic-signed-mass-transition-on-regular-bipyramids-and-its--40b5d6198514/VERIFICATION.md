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

Run `python verify.py` using Python 3 with NumPy installed. This recomputes Euclidean distance matrices independently of the rotational two-orbit equations, solves their mass-one constant-potential systems, computes eigenvalues of centered distance matrices, checks signed-mass transitions and threshold ordering, and approximates the circle chord integral through direct uniform quadrature. On the reviewed execution, the script passed 2,158 assertions.

The proof of infinitely many dimensions and all positive real heights is symbolic. Finite checks are corroboration, not proof of strict negativity for all zero-mass measures, nor proof of uniqueness on compact sets. The compact theorem optimizes only over finite signed Borel measures. The initial microscopic-weighting existence and magnitude slope relationships use the stated previously established negative-type framework. No independent audit has been performed.
