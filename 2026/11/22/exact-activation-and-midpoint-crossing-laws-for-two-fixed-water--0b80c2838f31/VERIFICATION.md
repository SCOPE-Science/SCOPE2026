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

For positive a,b and 0<q<1, integrating the two exponential segments gives the stated log ratio, also at coincidence and at the terminal boundary. After writing F=x(1+ax+b)/[(1+ax)((1+aq)x+bq)], differentiation gives a positive denominator and numerator -b[ax^2-2aqx-q(1+b)]. The only positive root x* is strictly above q; clipping at 1 gives the unique constrained maximum including when x*=1. Evaluation at 1 gives the activation threshold. Evaluation at sqrt(q) gives q[a(1-2sqrt(q))-(1+b)], including the strict no-crossing result at a=1+b. In the crossing regime h_0<log(3)<log(4)<h_{1/2}. Factoring sqrt(q) out of the root gives both the derivative on the interior branch and the asymptotic offset. VERIFY evidence is supplemental: verify.py was inspected, not executed; its finite grid is not a proof.

## originality

PASS

The supported distinct claim is the exact fixed-order, fixed-positive-amount timing classification for the linear store and Hill-exponent-one objective. The closest verified published records change the response or the decision being optimized. Historical irrigation optimization remains a plausible overlap area, but the inspected evidence does not supply the same decision problem or a stronger covering theorem.

## value

PASS

The restricted two-application problem is a useful deterministic benchmark. The threshold for any staggering and the stricter, sometimes nonexistent threshold for a late-season optimum distinguish three practically interpretable timing regimes. The exact sensitivity and midpoint offset say how scheduling changes with season length without reoptimization. This is mathematical value, not a prediction of crop yield or a recommendation for actual irrigation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
