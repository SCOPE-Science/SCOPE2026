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

The exact pairwise-payoff transition rule was independently enumerated over all labeled configurations for \(3\le N\le8\), across 249 rational parameter cases. The supplied `verify.py` checked 33,270 Bellman equations for the probability of unanimous \(A\) and the expected number of updates until unanimity. All passed using Python standard-library rational arithmetic.

Reproduce from this directory with `python verify.py`. The exact example \((N,a,b,p,i)=(10,2,7,1/2,5)\) yields \(P_i=1/2\), \(E_i=151/3\). General results follow from the analytic reversible-chain Dirichlet solution and Stirling/entropy argument in RESULT.md; finite enumeration is not a proof for arbitrary size. The entropy limit is not certified by these finite cases.

Scientific scope: full layer overlap, complete graphs, independent layer and focal-agent sampling, tie retention, and integer payoff thresholds. The supplementary material to the initiating study was not read. Independent external audit has not been performed.
