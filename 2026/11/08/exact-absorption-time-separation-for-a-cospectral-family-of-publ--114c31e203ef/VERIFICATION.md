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

# Verification

The provided `check_absorption.py` is a standalone Python 3 standard-library exact-arithmetic checker. It compares the symbolic beta-sum mean times against two independently set up finite-state waiting-time recurrences for each \(m=2,\ldots,8\), then compares graph-adjacency subset recurrences at \(m=2,3\). It checks the five-vertex exact means \(25/3\), \(33/4\), and difference \(1/12\).

Observed replay: `PASS 7 exact independent comparisons`; `PASS explicit graph state recursion m 2`; `PASS explicit graph state recursion m 3`.

The infinite-family proof is analytic and relies on the coupon-collector identity, independent exponential clocks, a finite beta expansion, and explicit upper/lower asymptotic bounds. Finite checks do not verify arbitrary \(m\), exclude equivalent literature, or constitute independent scientific audit.
