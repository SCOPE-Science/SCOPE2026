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

The all-parameter result follows from the prefix-width identities, the individually width-nonincreasing normalization moves except for moves bounded by \(t\), and the explicit one-swap bridge at budget \(t+1\). These are proof obligations independent of computational testing.

Run the included standard-library `verify.py` using `python3 verify.py`. The program computes every cut directly from graph-edge endpoints, independently builds the graph of labelled feasible orderings for \(t=1,2,3\) at budgets \(t\) and \(t+1\), compares its components against the recurrence, and reconstructs an explicit legal route to a canonical ordering for every feasible state in one hub orientation. It additionally probes larger sizes using deterministic pseudo-random samples and directly tests the bridge. Exhaustive checked graph orders are \(2,16\), \(32,296\), and \(2448,13536\) for the two budgets of \(t=1,2,3\), respectively.

The proof does not establish optimal numbers of moves or component structure at budgets below \(t\); the finite checks do not independently certify any infinite statement. Independent mathematical audit: not performed.
