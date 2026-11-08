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

The six-edge expectation identity follows from independence and inclusion of an edge in the rooted phylogenetic diversity exactly when at least one descendant survives. The universal lower bound for one to three leaves is proved symbolically by isolating the unique possible two-leaf clade interaction; it is not based on enumerating parameter values.

The standalone standard-library script `check.py` was executed with `python3 check.py`. It evaluates edge survival products and also independently enumerates all 16 survivor subsets under each of the 16 intervention subsets, obtaining exact agreement. Every singleton and doubleton value, the unique greedy order, the unique best pair and the gap of \(11/50\) were checked with rational arithmetic. No infinite-range claim is inferred from these finite checks.

The distinct historic four-taxon failure in Hartmann and Steel (2006), Figure 2, has unequal unprotected survival probabilities; its existence does not alone verify the equal-baseline restriction here. This work has not undergone independent scientific audit.
