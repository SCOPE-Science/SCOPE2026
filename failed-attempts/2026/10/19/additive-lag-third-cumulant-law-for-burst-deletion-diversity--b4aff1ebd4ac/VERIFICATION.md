---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Comparing deletion starts i<j gives equality exactly when X_t=X_{t+b} on i≤t<j, so each class of equal outputs is a contiguous run and D_b−1 counts lag-b disagreements. For uniform letters, equalities on a forest are independent Bernoulli(1/q) by revealing tree vertices from roots. Edges at distinct positive lags cannot coincide, so all covariance terms vanish; in order three only triangle terms survive. Writing t=1/q, the joint probabilities for a single, two, and all three triangle agreements are t,t²,t² respectively; the centered disagreement product has expectation −(t²−t³). The triangle exists exactly when a+b=c and the two different middle positions give 2(n−c) triangles. At n=3 there are no admissible triples. An independent literal enumeration of deletion outputs at q=4,n=5 gave −3/16 for (1,2,3), −3/32 for (1,3,4), and zero for (1,2,4) and (2,3,4). The marginal fixed-lag graph consists of b disjoint paths.

## originality

FAIL

The specific burst notation and coefficient were not found verbatim, but the result is the first two mixed-degree specializations of the published edge-weighted Potts/Fortuin–Kasteleyn identity applied to the standard lag representation. Extracting those coefficients reduces immediately to two-edge forests and the two placements of a middle vertex in a triangle. This is demonstrable stronger prior coverage, not a verdict based on a matching title or unavailable text.

## value

FAIL

The joint statistic is natural and the additive resonance is a useful illustration. The asserted scientific increment nevertheless consists of the constant-degree extraction of the already known exact graph moment identity, on a lag graph whose only three-edge cycles have gaps a,b,a+b. No surviving invariant beyond this direct consequence is established, and there is no substantive repair in merely reframing that calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
