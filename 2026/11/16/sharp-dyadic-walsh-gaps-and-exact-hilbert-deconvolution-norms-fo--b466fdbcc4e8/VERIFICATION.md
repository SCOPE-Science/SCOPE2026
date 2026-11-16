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

# Reproducible mathematical checks

Run `python3 wheel_checker.py` with Python 3.8 or later and no third-party packages. The script computes exact indicator Walsh transforms for rim lengths 3 through 9 and checks the 349,504 coefficients against parity, four-divisibility, singularity, sharp positive gaps, the weighted matrix-tree determinant at sampled signings, exact transfer products, and Parseval. It also checks sharpness witnesses through rim length 90 and determinant evaluations through length 20. Expected terminal marker: `WHEEL_SPANNING_TREE_WALSH_GAP_PASS coefficients=349504 witnesses=88`. This does not verify the result for infinitely many rim lengths; those conclusions use the proof in `RESULT.md`. No independent audit or independent validation is asserted.
