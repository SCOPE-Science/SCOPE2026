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

# Reproducibility and limits

Run `python verify.py` with Python 3 and NumPy. In the recorded run, the checker returned **PASS: 24486 supplementary deterministic assertions**. Checks include the exact \(K=2\) benchmark \(32/27\), spectral approximation inequalities at sampled dimensions and all tested ranks, direct finite Landweber noise-map recurrence versus the diagonal covariance formula, sharpness families at multiple ranks, and the large-\(K\) asymptotic constants.

The analytic theorem is contained in `RESULT.md`. Random examples are not exhaustive; the infinite-dimensional quantification over all finite matrices and all integers \(K\) follows from the proof, not the checker. The risk that related spectral approximation statements appear in unindexed literature remains. The independent audit has not been performed.
