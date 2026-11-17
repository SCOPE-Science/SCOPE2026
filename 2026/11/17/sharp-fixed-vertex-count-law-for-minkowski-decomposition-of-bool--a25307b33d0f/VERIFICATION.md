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

# Reproducibility and scope

The standalone `verify.py` uses only the Python 3 standard library. It evaluates the exact inclusion–exclusion count for every tested \(d,k\), calculates the prime-factor recurrence via coordinate-set partitions, and independently enumerates all Boolean subsets in dimensions one through four (up to ten vertices), testing all proper coordinate splits for the product condition. It also compares the four-, six-, and nine-vertex closed forms to the recurrence through dimension five.

Run `python verify.py`; an assertion failure means a finite verification test failed. These exact finite checks corroborate the unrestricted algebraic proof and do not constitute an infinite proof or an independent specialist audit.

The structural premise — the coordinate-product characterization of Minkowski decomposition — is Theorem 1.1 and its proof in Higashitani–Padrol–Sanyal (arXiv:2605.22594). Its use is explicit. The asymptotic restriction is fixed \(k\), varying ambient dimension, conditioned on no constant coordinates. No external independent audit has been performed.
