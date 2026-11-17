---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every good must be alone for m=4, since an empty agent would violate inter-EF1 if any agent held two goods. At m=5 exactly one agent holds two goods, one a minimum-valued item; singleton agents must value their own good at least the smaller of that pair. The two center-EFX inequalities reduce to u+v>=s+t and s+t+e>=max(u,v). The proof supplies explicit allocations in a+d<=b+c and a+d>b+c cases. Appending a good no larger than old maximum preserves four-good feasibility. Rank-of-appended observation R is uniform independent of sorted spacings; exponential order gaps are independent with rates 5,4,3,2,1 and uniform gaps normalized iid exponentials. Integration produces p10=4/105 for exponential and 1/120 for uniform, from which exact remaining table entries follow. Direct independent enumerator checked all 461 positive integer multiset profiles within its stated finite range, examining 23741 allocation cases until fairness witness; finite verification is corroboration, not an unrestricted proof.

## originality

PASS

The explicit necessary-and-sufficient first obstructed-size inequalities and coupled resource-addition probabilities were not shown to follow from the previously published delegated-fairness impossibility and hardness results; earlier four-good counterexamples are subsumed and properly credited. Best-of-knowledge originality, not proof of historical first discovery.

## value

PASS

The exact frontier at first nontrivial inventory sizes and positive-probability loss of fairness upon adding an item are structural fairness results; coupled probability tables under two canonical continuous priors quantify the consequence of the value-law tail, not an arbitrary isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
