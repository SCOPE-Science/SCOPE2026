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

Verified for the eight-state chain with rate-one injection, exit and rightward hops and equal positive exchange w only at the middle site. The marked hop channel counts both accepted bond transitions. Independently used a row-generator martingale calculation: for each mark solve Lh_a=m_a-r_a, where r_a is its instantaneous rate. The centered count plus the bounded potential increment is a martingale with jump indicator_a+h_a(y)-h_a(x). Its limiting covariance per unit time is the stationary rate-weighted sum of products of these jumps. The bounded corrections vanish at covariance-rate scale, and finite irreducibility makes the bracket rate and mean rate independent of initial state. Exact symbolic arithmetic matched the five mean rates and Fano functions and all ten cross-covariances. It recovered the stated positive-coefficient certificates for the boundary derivative and negative Langmuir derivative and the strictly increasing cubic controlling the hop derivative. The unique positive cubic root is 0.38380195482895884... and the Fano factor there is 0.59245585461490491.... The endpoint limits are not assertions at w=0 or infinity.

## originality

PASS

The distinct content supported by the bounded comparison is the exact, all-positive-w second-order classification of these five accepted count marks along the equal-exchange path. The chain and general cumulant machinery are prior. The closest same-day count record works on a different rate path and mark convention; the closest same-model occupation record has different observables. No inspected prior claim entails the full classification. No ordering is inferred from same-day publications.

## value

PASS

Three sites give the smallest open chain with a genuinely internal exchange site. The complete sign matrix and the contrasting increase, decrease and unique maximum answer a natural finite benchmark for how reaction noise differs from boundary and transport noise. The findings apply over the full positive control range and distinguish the aggregate of both hops from boundary traffic; neither one parameter value nor a static occupancy computation could establish them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
