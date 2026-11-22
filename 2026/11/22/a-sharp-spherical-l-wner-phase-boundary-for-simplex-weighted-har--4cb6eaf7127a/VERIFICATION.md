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

# Verification notes

Run `python3 check.py` from the extracted package directory. Python's standard library is the only dependency. Observed output:

```
HARMONIC_LOEWNER_THRESHOLD_PASS formal_vertex_cases= 12 rearrangement_cases= 21
```

The script exhaustively checks Minkowski-sum generating points for dimensions \(2\) through \(5\) at three positive rational simplex weights (the equality cases of the radius and the full contact count). It checks pairwise rearrangement extrema for dimensions \(2\) through \(8\), again at three rational weights. The all-dimensional and continuous-weight assertions follow from the rearrangement lemma, explicit orbit covariance, trace/determinant argument, and strict-volume perturbation in `RESULT.md`, **not** from finite enumeration. The threshold equality case is addressed analytically by allowing zero weight on the aligned orbit. The program does not claim independent verification.
