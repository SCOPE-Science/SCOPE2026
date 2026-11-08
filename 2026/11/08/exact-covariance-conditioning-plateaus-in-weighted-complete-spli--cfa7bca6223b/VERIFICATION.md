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

The self-contained program `verify.py` uses only the Python standard library. Run `python3 verify.py` from a directory containing the program. A successful run emits:

`SPLIT_WEIGHTED_ZONOTOPE_COVARIANCE_CHECKS_PASSED cases=36 entries=1344 sampled_vertices=83400 phase_profiles=35164 total_order_cases=24`

It independently enumerates all \(p!(p+1)^q\) parametrized vertices in each of 36 small exact-rational cases and computes full covariance matrices by integer sums. It constructs the three-eigenspace projector formula and checks all 1,344 entries exactly; it also verifies direct total-order vertex deduplication in 24 cases and exact phase-sign inequalities for 35,164 additional parameter pairs.

These computations **do not prove** the spectrum or the sharp phase diagram for every integer graph size and positive real weight. The proof for all parameters is the symbolic moment argument, symmetry decomposition and exact inequality derivation in `RESULT.md`. No independent mathematical audit has yet been performed.
