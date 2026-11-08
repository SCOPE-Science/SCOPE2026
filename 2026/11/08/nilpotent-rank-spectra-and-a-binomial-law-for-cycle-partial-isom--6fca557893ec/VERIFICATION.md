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

# Reproducibility

Run `python3 verify.py` using only Python's standard library. The program independently enumerates partial maps as tuples of images with a sentinel for points outside the domain. For each map it detects whether its functional digraph contains a directed cycle, and compares the resulting domain-rank histogram with the closed polynomial. It also cross-checks the known total cardinality of the cycle partial-isometry monoid.

All nine cases from `n=3` through `n=11` passed in the saved package. Example: at `n=4` the nilpotent rank counts are `[1, 12, 20, 8, 0]` out of a total monoid size of 97; at `n=6` they are `[1, 30, 108, 108, 48, 12, 0]` out of 703. Successful execution prints `VERIFY_OK`.

These are exhaustive checks at the indicated finite sizes only. The unrestricted polynomial identity and convergence bounds are justified by the mathematical proof in `RESULT.md`. Independent mathematical audit has not been performed.
