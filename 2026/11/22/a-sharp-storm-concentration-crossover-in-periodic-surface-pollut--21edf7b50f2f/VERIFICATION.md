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

For identical events spaced by Δ with retention s in (0,1), the post-event map b→s(b+aΔ) contracts to aΔs/(1−s); the time average over an interval is that fixed point plus aΔ/2. Applying this directly at Δ=T and Δ=T/2 with doses 2^p x and x gives the two means. The difference has the sign of coth(x/2)/coth(2^(p−1)x)−2. The logarithmic derivative is −1/sinh(x)+2^p/sinh(2^p x), strictly negative because sinh(u)/u increases for positive u and p>0. The ratio decreases from 2^p to 1, proving strict split advantage even at p=1 and precisely one crossover with the stated orientation for p>1. At p=2 the tie reduces to cosh²(x)−cosh(x)−1=0, with exactly one positive x. The supplied finite checker was inspected, not run; the result follows for the full domain analytically. The two policies remove the same total aT per period in this model, so the conclusion is only about time-average retained mass.

## originality

PASS

Constant dry buildup, exponential event retention and regularly spaced fractional removal are established ingredients. The supported distinct claim is the exact allocation crossover at fixed rain depth and period when changing event count also changes the per-event removal strength by a power law. No inspected prior statement supplies the two-policy threshold and direction over the whole range of p and x.

## value

PASS

The two prescribed policies expose competing effects of a larger dose per event and shorter dry gaps. The exact boundary tells a modeler when the direction reverses, including a domain where the one-storm policy never wins, without requiring simulation or values of a and T. This is useful within the idealized stock model, not a field recommendation, a global scheduling optimum, or a reduction in total export.

The dated certificate retains the supplied scientific assessment, sources and limitations.
