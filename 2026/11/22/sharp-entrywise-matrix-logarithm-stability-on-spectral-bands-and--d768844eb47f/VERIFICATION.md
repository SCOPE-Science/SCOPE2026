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

The analytic certificate is the proof in `RESULT.md`, including the positive-contraction row lemma, all-index resolvent bound, saturation by a rank-one projector and admissible interior perturbation pairs, and integrable asymptotic bounds. Run `python checker.py` with NumPy and SciPy installed to independently reproduce the 625 finite numerical comparisons between the closed form, quadrature, divided-difference derivatives and finite-input perturbations. These numerical assertions support implementation consistency and are not proofs of the infinite claims. Independent mathematical validation has not been performed.
