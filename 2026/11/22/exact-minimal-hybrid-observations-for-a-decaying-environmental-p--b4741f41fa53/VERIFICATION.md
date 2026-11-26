---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Convolving the decaying input with the passive loss kernel gives a symmetric divided difference of exponentials, including the finite coincident-rate limit. For a=exp(-lambda Delta) and b=exp(-delta Delta), P(2 Delta)/P(Delta)=a+b. At known gain, P(Delta)/(k Delta C(Delta)) is L(b/a), with L(u)=integral_0^1 u^s ds and L'(u)>0, including L'(1)=1/2. These give a,b and C0 uniquely. At unknown gain the two active readings give a and C0; the sum then gives b, and the first passive reading gives k. Both inverse maps are smooth at positive interior collisions. The minimum-three claim holds on the generic distinct-rate domain: with two passive readings the rate swap persists, with two active readings the loss rate is missing, and with one of each at positive passive time one can vary lambda, match C through C0, and then implicitly adjust delta because the passive convolution is strictly decreasing in delta with nonzero derivative. A passive reading at zero is uninformative. At unknown gain, a rate swap can be masked at any single active time (including zero) by rescaling C0 and keeping k C0 fixed; a single positive-time passive reading instead permits arbitrary delta compensated by k, even knowing the entire active trace. The passive Taylor expansion is even with a quadratic leading sensitivity for fixed positive time. Independent convolution quadrature checked both inverses in 30 bounded cases, including both rate orders and exact and near equality. Replay: `python3 /workspace/branches/review_checks.py 3`.

## originality

PASS

The supported distinction is the exact minimum hybrid scalar counts for the two calibration regimes, their constructive fixed-time schedule, and the smooth inverse at collision. The response law, rate-exchange ambiguity and general structural identifiability are not new. No inspected prior statement establishes the combined finite-design and lower-bound result. This is a bounded best-of-knowledge assessment, notably not a definitive comparison to Hawker's full text.

## value

PASS

The two exact calibration-dependent designs answer a natural experiment-selection problem in the idealized model. The necessity by observation type says why, at unknown gain, more samples of the same type cannot replace a missing type of observation; collision regularity shows a genuine advantage over extracting unlabeled poles. These are structural distinctions, not claims of improved field accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
