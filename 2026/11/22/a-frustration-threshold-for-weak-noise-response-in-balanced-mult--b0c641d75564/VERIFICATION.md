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

Run `python verify.py` using Python 3, NumPy, SciPy and SymPy. It reconstructs continuous-time rate-one contrarian copying plus rate-\(a\) unbiased refresh on four small complete multipartite systems, computes stationary moments directly and tests the semigroup at three positive time lags. A separate symbolic portion checks the exact rational pair and variance identities. The saved script returned `FINITE_STATE_CHECKS_PASSED 62` and `SYMBOLIC_IDENTITIES_PASSED 3`.

These finite examples and symbolic simplifications supplement the generator proof in `RESULT.md`. The all-size claims depend on the stated generator closure and eigenfunction identities, not on extrapolating from examples. The inaccessible multipartite anti-voter chapter leaves a stated priority risk. No independent scientific audit has been performed.
