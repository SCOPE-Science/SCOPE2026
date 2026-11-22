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

# Verification of the dyadic three-descent Eulerian fiber theorem

Run the standalone standard-library checker with `python3 verify.py`. On a successful run it reports `VERIFY_OK` and `all_levels_finite_checks=PASS`.

The checker constructs Eulerian numbers independently using their two-term triangle recurrence for 101 indices, compares each with the closed exponential formula, counts 24,570 exact residue fibers in 36 full period blocks over \(1\le k\le12\), checks 49,140 period shifts, and tests 3,810 exact dyadic valuation identities for even and odd index charts. All tests passed in the reviewed package.

The exhaustive finite blocks do not prove assertions for unbounded \(k\). The general proof uses the exact formula and four dyadic isometric charts derived algebraically in RESULT.md. In particular, the distinction between a period candidate and the *least* eventual period is proved by the even-chart isometry, not inferred from testing. The starting index is a sufficient bound; minimum onset and an independent mathematical audit are not asserted.
