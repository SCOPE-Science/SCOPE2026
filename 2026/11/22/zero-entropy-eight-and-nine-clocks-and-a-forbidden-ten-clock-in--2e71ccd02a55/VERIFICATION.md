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

Run `python3 verification/verify_short_clocks.py`. It reconstructs the temporal-height graphs from the Rule 110 truth table, computes cyclic strongly connected components, checks all cyclic component sizes, edge counts and time-column periods for heights 1, 2, 3, 4, 5, 8, 9 and 10, and prints `FULL_SPECTRAL_COUNTS_OK` on success. This exact finite graph exhaustion, together with the closed-walk bijection, establishes the all-circumference assertions.

Run `python3 verification/check_direct.py` for independent bit-parallel evolution of every state on each ring of length 3 through 20. It reports the exact primitive-eight, primitive-nine and primitive-ten populations and prints `BRUTE_FORCE_OK` on success. This second finite experiment checks the first ring sizes but does not itself prove the infinite-size statement.

Both scripts were executed from the actual delivered files; the `.out` files record their output. The theorem does not classify transient basins or periods other than 8, 9 and 10. Independent external audit is not performed.
