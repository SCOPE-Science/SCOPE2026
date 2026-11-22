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

The embedded programs `verify.py` and `distance_check.py` are self-contained Python 3 scripts, requiring only its standard library. Run `python3 verify.py` and `python3 distance_check.py` in the same directory as the other files.

`verify.py` performs a complete pairwise comparison of direct one-deletion descendant sets at lengths \(1\) through \(10\). It also tests the distinct-pair involution in every token layer through length \(18\), the exact number of unmatched configurations, the parity of those configurations, and the stated optimal-code and edge counts.

`distance_check.py` checks all token-graph distances at lengths \(1\) through \(9\), and tests graph diameters and the count of shortest paths between packed configurations against the rectangular hook-length formula.

Both programs were executed successfully using the actual embedded source files. Neither makes an infinite proof; the all-length arguments appear in `RESULT.md`. The independent mathematical audit has not been performed.
