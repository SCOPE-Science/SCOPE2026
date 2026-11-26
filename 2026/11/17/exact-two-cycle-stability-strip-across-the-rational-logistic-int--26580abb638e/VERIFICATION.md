---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the repaired statement, the swap equations for two distinct points give sum S=(mu+1)/mu by subtraction and product P=S/(mu-lambda) by addition. Conversely these sum and product equations imply both swap equations; solving the quadratic therefore introduces no extraneous roots. Its discriminant has the sign of H and its vertex lies in (0,1) with positive endpoint values, so a positive discriminant gives exactly one primitive pair in the interval and a double root gives none. At each root x, with other root y, differentiate (1+lambda x)F(x)=mu x(1-x) and use mu S=mu+1: the derivative numerator is mu(y-x)-(1+lambda y). Multiplication gives 1-mu(mu-lambda)(y-x)^2/[(1+lambda x)(1+lambda y)], which reduces to 1-R via the given P,S. With t=sqrt(1+lambda) the critical point is 1/(1+t), the stated invariance endpoint gives H=2 t^2(t+1), and R=4[1+1/(t+1)^2]>2 there. R rises strictly from zero with mu above mu_1 by its three positive factors. It falls strictly with lambda wherever H>0. Comparing a smaller-lambda threshold at the larger lambda either puts it below the latter's mu_1, or places it inside the latter admissible interval with R<2 because the upper invariance endpoint increases. This proves strict increase, including the endpoints. At lambda=1 the quartic divided by mu^2 reduces to s^2-4s-4 with s=mu-1/mu; the allowed root has s=2+2 sqrt(2), giving the corrected radical. The simple zero of H gives the square-root expansion and error by factoring out mu-mu_1 before expanding the positive analytic factor. An independent symbolic calculation confirmed the frozen factorization, discriminant, product derivative, invariance-endpoint identity, and quartic, all of which apply to the repaired theorem.

## originality

PASS

The repaired claim is a uniform exact period-two census and local stability strip for the interior of the known interpolation, with a rigorous strictly increasing secondary boundary on the closed parameter interval and an explicit opening coefficient. The endpoints are included for continuity and credited, not asserted as new. The closest primary paper treats the identical family and gives the exact first fixed-point threshold, but its Section 7 determines the secondary boundaries at four samples by numerical approximation. The strongest indexed prior gives the entire exact rational-endpoint census, multiplier and threshold and goes further for period four there; that specialization is covered and excluded from the supported distinct claim.

## value

PASS

An exact stability boundary for a specified two-parameter interpolation answers what sampled Lyapunov plots cannot: where the only primitive two-cycle is locally attracting, and whether increasing interpolation moves the crossing monotonically at every parameter. The closed-form multiplier and opening coefficient explain onset and loss of hyperbolicity, and the proof applies across the whole invariant strip. That uniform statement survives crediting the known endpoints and does not rely on rediscovering them or merely fitting tabulated values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
