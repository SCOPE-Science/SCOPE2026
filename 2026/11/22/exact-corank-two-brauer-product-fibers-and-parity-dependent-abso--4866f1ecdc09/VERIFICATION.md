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

The exact checker `verify.py` enumerates labeled Brauer matchings and composes them via three-layer paths. The saved output `checker_output.txt` records complete prescribed-output checks for \(n=3,4\) through product length four and \(n=5\) at length two; all allowed targets and every coefficient are tested, not sampled for these cases. Additional representative-rank and all-hook tests for \(n=6\) independently confirm the local rank transition, and stochastic normalization is checked for \(3\le n<20\) at six lengths.

The general statement is proved in `RESULT.md` using a uniform-hook transition and two-sided permutation invariance. Finite checks do not establish the infinite-dimensional or large-degree limits. No independent audit has been performed.
