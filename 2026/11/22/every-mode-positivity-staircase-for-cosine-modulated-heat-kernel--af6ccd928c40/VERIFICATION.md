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

# Verification and limitations

The included `checker.py` is self-contained and uses the Python standard library. Run `python3 checker.py` from a directory containing the file. It checks cyclic mode comparisons and transition ordering for \(3\le N\le200\), then compares direct finite Fourier transforms of the modulated heat kernel with the predicted eigenvalues for \(3\le N\le25\). It also checks positive-semidefinite, definite, and indefinite instances on and near the sharp boundary. Recorded execution: 200246 assertions passed.

At near-tie large-time cases, floating-point comparison is treated as inconclusive at roundoff scale. Universal uniqueness, no-skips, all-time positivity and nullity are supplied by the analytic argument in `RESULT.md`, not certified by finite regression tests. No external expert or independent validation has occurred. The source dates identify a motivating 2024 preprint; subsequent journal publication dates are not used to reassign its original public date.
