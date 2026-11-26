---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two leaves of an edge determine its majority if they agree, so a locked pair cannot unlock; if they disagree, the first ring locks them to the current hub opinion without moving the hub. Consequently the leaf-freezing time is the maximum of m independent Exp(1) first-ring times. Integrating the survival function gives sum_{j=1}^m 1/j (or zero if m=0). Once frozen, a mixed-color pattern has exactly the two hub states, with rates b' and a' and stationary A weight a'/k. A uniform pattern reaches its unique absorbing state. Mixed-pair configurations are transient since a mixed edge rings almost surely and the reverse change is impossible. If the hub opposes the only initially locked color, consensus is decided by the first ring among the locked and mixed edges, with probability a/k or b/k as applicable; all other cases follow by locking. Averaging over the iid start gives the displayed expression, including q=0,1 and q=1/2. An independently written literal three-bit majority enumerator checked the rates with multiplicities, terminal SCCs, exact Bellman absorption equations for all 2728 states through k=5 and exact iid polynomial coefficients, not just sampled q values. There were 2,4,8,16,32 terminal SCCs; the k=5 probabilities split as 1140 zero, 488 one and 420 strictly fractional. Replay: replay/3_hyperstar.py. Finite evidence only; the sample-path argument proves all k. Uploaded script inspected, not executed.

## originality

FAIL

The October 18 Resultary record reports the same simultaneous majority on triples sharing just one hub, and a strictly broader arbitrary-positive-weight theorem for every initial state, both consensus colors and persistent disagreement. The unbiased law is explicitly identical. Equal-rate Poisson clocks have the same ordered edge sequence as uniform independent choices; the continuous-time formulation changes the clock, not hitting or communication. The additional biased-iid average, rate normalization and leaf-freezing order statistic are direct consequences, not an independently substantive surviving claim.

## value

FAIL

The persistent-disagreement example and exact law are valuable as mathematics, but they are not a new benchmark in this frozen record. Equal-weight specialization plus continuous-time clock embedding, a one-step iid product average and an elementary exponential order statistic do not constitute a separate motivated scientific advance. No repair is justified by the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
