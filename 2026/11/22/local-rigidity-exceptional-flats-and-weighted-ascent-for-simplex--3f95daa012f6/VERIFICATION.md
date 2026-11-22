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

# Verification and reproduction

The proof is in `RESULT.md`. The standalone `checker.py` (Python 3 with NumPy) implements the unsigned incidence, Gram projector, Kneser sign matrix, eigenvalue multiplicities, and the exact leakage formula. It checks randomly perturbed rank-\(m\) projections for all integers \(4\le m\le12\), including the exact dimension-seven isotropy. It separately checks four-dimensional flat directions, their strictly positive optimized-weight increase, and the common small-angle coefficient \(48/125\). The observed command `python checker.py` returned:

```
SIMPLEX_LOCAL_SIGN_SPECTRAL_CHECK_OK 2330
```

Each assertion has a finite floating-point tolerance where appropriate. This computational diagnostic does not establish the infinitely many dimensional cases, the existence of a full neighborhood, or publication originality. Those points are addressed analytically and bibliographically in the manuscript. The self-review is reported in `REVIEW.md` and `AUDIT.json`; no independent audit has been performed.
