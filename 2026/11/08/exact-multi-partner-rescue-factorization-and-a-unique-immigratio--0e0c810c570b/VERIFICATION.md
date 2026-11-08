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

# Verification record

The exact identity follows from a reference model with independent arrival and loss clocks and a ratio of first-arrival probabilities after replacing the empty-state extinction hazard. The first-step recursion of the actual subset-state Markov chain provides a mathematically distinct calculation and was compared using exact `fractions.Fraction` arithmetic in 270 heterogeneous cases for two through seven required partners. All comparisons passed.

The standalone `checker.py` also evaluated 200 numerical budget-optimization problems for two through nine partners, checking total allocation, common marginal logarithmic gain, risk ordering, dominance of random feasible allocations, and consistency with equal allocation. The small- and large-budget share limits were checked at extreme numerical budgets. The checker executed successfully with Python's standard library only.

The general identity and global uniqueness are proven analytically; finite cases alone would not establish them. The first-order asymptotic statement assumes fixed positive hazards and a fixed number of partners. Neither the validation script nor this review is an independent external audit, and no empirical parameter fit has been performed.
