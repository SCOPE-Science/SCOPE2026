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

The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. From the package directory, run `python3 verify.py`. It constructs continuous-time Markov generators for one-, two-, and three-stage exponential rest chains, solves their stationary moment equations, and compares their second and fourth moments against the independent renewal-reward formulas for 90 stage-and-parameter combinations. It also checks 30 instances of the displayed exact threshold-comparison identity and 3 exact rational brackets for the Erlang-2 critical root, totaling 123 checks. The actual execution passed all 123.

The analytical proof supplies the unbounded-domain statements: general independent rest distributions of finite mean, uniqueness of the stationary moment law, the unique positive critical root, and the strict comparison with memoryless rest. Exact-rational finite cases alone do not prove these universal assertions. No independent external audit has been performed.
