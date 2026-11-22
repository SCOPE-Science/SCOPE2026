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

The combinatorial formula and explicit graph-update rule were checked using the embedded standalone `check_dynamics.py`, on all \(q=2,3,4,5\), \(n=2,3,4,5,6,7,8\), with the generated `check_dynamics.out` capturing the complete count table and terminal `ALL_CHECKS_PASSED`. The checker directly applies the open-neighborhood modal color rule at each vertex, verifies that every state with two tied maximal colors returns in exactly two steps, and verifies that all other states are fixed by the next update. It independently counts those period-two states and compares them to the exponential-polynomial coefficient formula using integer factorial-weighted convolution.

The Poisson critical-window statement is proved by exact multinomial falling-factorial moments, a union bound for occupancies at least \(k+1\), and a second-moment estimate for occupancy \(k-1\). A finite computer experiment, even an exhaustive one, is not treated as a proof of this asymptotic assertion.

No independent external audit has been performed. Historical-priority confirmation beyond the cited works remains open.
