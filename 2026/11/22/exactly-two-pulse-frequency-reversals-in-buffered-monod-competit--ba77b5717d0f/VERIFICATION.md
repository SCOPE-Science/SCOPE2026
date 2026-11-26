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

The periodic jump-decay solution has H−L=10T, giving both input flux and mean concentration equal to 10 in the chosen units. Integrating r/(1+r) and 2r/(10+r) with dt=−dr/r gives the two logarithms. The signed numerator of their log-ratio comparison is (H−L)(80−HL−H−L), whose second factor equals 10F(T)/(exp(T)−1)², with positive denominator. For F's Taylor coefficients the degree-0 and degree-1 terms cancel; exact coefficients have signs − in degrees 2–5, + in 6–15 (computed independently), and − in all degrees ≥16 because 16−n≤0. The function J=(TF′−6F)/T¹⁶ is strictly decreasing on (0,∞) by its Laurent series: positive coefficients multiply negative powers; negative nonconstant coefficients have positive powers. It tends to +∞ at zero by F(T)=−4T²+O(T³) and to −∞ by TF′−6F∼−2T²e^(2T). Thus F/T⁶ strictly increases then decreases with one maximum, is negative toward both endpoints, and is positive at T=5: F(5)=e⁵(3e⁵−266)+13 and e⁵>100 from its Taylor terms. Both positive roots are simple, with the claimed signs. Independent high-precision bisection reproduces both decimals, without relying on these numbers for exhaustion. The equal density term cancels in the log ratio; after n periods it differs from its initial value by nTΔ, with uniformly bounded within-period modulation at fixed T. Logistic bounds with positive minimum growth and upper growth bound two, valid between pulses with continuous biomasses, keep total abundance bounded and ultimately away from zero. This makes the ratio result actual extinction of the loser, not just relative decline. At equality there is no strict exclusion. Continuity in the positive parameters preserves alternating strict witness signs at 1, 5, 20, hence at least two reversals locally, not an exact perturbed count.

## originality

PASS

The supported distinct claim is the exactly-two reversal count for the specified single exponential-decay pulse family with fixed mean and fixed input flux, including its exact threshold equation. The exclusion consequence at each fixed T is an instance of the existing shared-crowding selection theorem. A different same-day analytic Monod result already establishes a two-reversal phenomenon for symmetric two-level forcing with fixed mean; the frozen claim does not establish priority for that general phenomenon. Neither that forcing theorem nor the fixed-T selection theorem implies the frozen count.

## value

PASS

Changing only pulse timing at fixed mean and input flux is a natural modeling question. For two simple saturating responses this gives a minimal exact witness against a monotone ranking in the pulse interval, with proof of exhaustion and both thresholds, not just two simulated crossover points. The square-wave analogue does not make this redundant: at the frozen growth constants its symmetric forcing never reverses the ranking. That difference makes the precise exponential-waveform result a useful benchmark for separating forcing shape from mean and arguing about robustness of growth ranking. The shared-crowding extinction step is not the source of distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
