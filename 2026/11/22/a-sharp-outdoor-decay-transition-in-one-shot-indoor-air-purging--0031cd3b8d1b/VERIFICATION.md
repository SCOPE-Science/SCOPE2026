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

The jump changes the subsequent trajectory by −ηuD(τ)exp(−a(t−τ)); integrating gives the stated product. D rises strictly from −x to 1 and is strictly concave. For T≤t_0 no positive saving is possible (a terminal purge ties no purge); for T>t_0 the positive product is strictly log-concave between its zeros. At T/2 its logarithmic derivative is positive if that point is already in the beneficial interval. The implicit derivative is A/(A−(log D)″), where A=a²exp(a(T−τ))/(exp(a(T−τ))−1)²>0. At onset the stationarity equation is 1/y−1/(ε−y)+O(1)=0, which gives y=ε/2+O(ε²) and the stated quadratic savings. The midpoint test forces both optimal lead and lag to diverge; balancing the two marginal exponential tails then gives the constant timing offset and residual coefficient. Equal rates give an exact geometric balance. For fixed T, the objective converges uniformly on [0,T] as x↓0 to the symmetric objective with unique maximizer T/2, justifying the iterated limits. Independent bisection recovers the three illustrative timings. The supplied verification was inspected but not executed.

## originality

PASS

The standard mass balance, indoor–outdoor tradeoff, and pulse-benefit factorization are not credited as new. The supported distinct result is the exact scalar timing classification for a single fixed-fraction exchange against a decaying exterior, especially the rate-controlled change in optimal horizon fraction, its constant offset and the singular weak-exterior limit. The closest distinct comparisons have different state dynamics or different admissible controls and objectives.

## value

PASS

The precise long-horizon split separates an exterior component that shifts the optimal time by order T from one that does not, even when the exterior amplitude is arbitrarily small and positive. Combined with the finite beneficial horizon and unique optimum, this is an interpretable benchmark beyond the log-concavity calculation alone. Its scope is a single instantaneous exchange, with no baseline infiltration, a fixed source and cumulative concentration as the objective; it does not establish a health or operational ventilation recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
