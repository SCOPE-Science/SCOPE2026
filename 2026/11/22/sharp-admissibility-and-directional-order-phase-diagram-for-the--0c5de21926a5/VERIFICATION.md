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

Recover the phase diagram by setting q=(1-a)t^b/[a+(1-a)t^b]. Then tP'/P=q, tq'=bq(1-q), and k=h'=1-P(1+q), so k'=-(P/t)q[(1+b)+(1-b)q]. The bracket has the sign of a(b+1)+2(1-a)t^b. It is positive on the open interval at and above the threshold: for b>0 use a(b+1)>0, and for b<0 use the value 2-a+ab at t=1 and strict decrease toward it. Below threshold it has exactly one zero at the displayed t*, and k decreases then increases. The endpoint values are M and -(1-a). At t* the base is a(1-b)/2 and q=-(b+1)/(1-b), giving the stated -L. Since P<1 and 0<q<1 in the interior and k(1)=a-1<0, the derivative range closes to [-L,M] with 0<L<1. The mixed density is 1+alpha k1 k2; the extreme products are independent across the two coordinates, giving the interval including both endpoints. Outside it a negative interior rectangle follows by continuity, even if the extremum is a boundary limit. For an interior response argument h2>0, hence the conditional CDF v+alpha k1 h2 has the opposite direction to the stochastic order. Its turning point and the transposed direction follow exactly. The ordered density minor factors as alpha times the product of the two ordered k differences. Either reversal gives both signs; otherwise the sign is alpha, with independence giving zero. This covers endpoint admissibility and the equality threshold without extending to b=0. The frozen checker was read, not executed; its finite grids are not the proof. Analytic replay: RESULT.md lines 42–73.

## originality

PASS

The primary literature covers the same family on a sufficient box and the generic rank-one positivity mechanism. What survives as distinct is the evaluated, sharp power-mean derivative envelope and its one-turn and two-direction density-order classifications, not the construction or general derivative test.

## value

PASS

An exact parameter interval is needed to distinguish permissible models from negative-density candidates, especially when the original convenient bound excludes valid and qualitatively different cases. The one-switch threshold and the need for both coordinate thresholds for TP2/RR2 give usable criteria for selecting asymmetric regressions, beyond the rank-one method itself. Value is confined to the given nonzero finite exponents and strict shape range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
