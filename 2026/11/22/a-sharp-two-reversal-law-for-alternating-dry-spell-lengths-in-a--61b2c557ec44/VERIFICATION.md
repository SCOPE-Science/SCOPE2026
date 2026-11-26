---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The two schedules have the same duration 2m per two pulses, so their comparison is the centered second difference of F(t)=e^(−bt)[1−(1+at)e^(−at)]. Writing c=a+b and J=cosh(cd)−1, the normalized difference is B−H with B=cosh(bd)−1 and H=e^(−am)[(1+am)J−ad sinh(cd)]. The derivative has the sign of d sinh(cd)−mJ, giving the interior peak m*=d coth(cd/2). For z=cd/2, log(sinh(z)/sinh(bz/c))=∫ from bz/c to z of coth(v) dv, strictly greater than a m*/2 by strict decrease of coth. This proves H(m*)>B, while H tends to zero at infinity. Hence one upper root always exists, and the lower one is admissible exactly when F(2d)>2F(d). For G(x)=1−(1+x)e^(−x), its elasticity xG′/G is x²/(e^x−1−x), strictly decreasing because its reciprocal has a positive-coefficient power series with positive linear term. Therefore e^(−bd)G(2ad)/G(ad) strictly decreases from 4 to 0, giving the unique threshold. At equality m=d itself is excluded and there is only the upper admissible root. With a single stage the normalized gap is strictly increasing from a negative value to B>0. Independent decimal bisection of the original differences reproduced d_c=0.425304912003236…, the roots 0.372551797020654… and 2.16039402036334… for a=b=1,d=0.2 and all three illustrated percentages. Finite diagnostics are supplementary; uploaded code was not run.

## originality

PASS

The supported contribution is the full finite-gap sign diagram and exact endpoint threshold for the stated Erlang-survival centered difference, with a one-stage obstruction within that family. Standard renewal division by time or curvature/zero-count methods alone do not give the claimed count, transition and strict signs. The strongest inspected pulse/deadline analogues use different kernels or comparisons.

## value

PASS

Under a natural equal-mean, equal-event-count control, a response requiring maturation and survival creates two finite sign reversals, which a one-stage model does not allow. The all-parameter diagram shows exactly when that second reversal is lost and whether it is lost through the schedule boundary; neither a local curvature heuristic nor a numerical plot settles those questions. This is useful as a diagnostic benchmark for idealized cycle-pulse modeling, not as a quantitative field prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
