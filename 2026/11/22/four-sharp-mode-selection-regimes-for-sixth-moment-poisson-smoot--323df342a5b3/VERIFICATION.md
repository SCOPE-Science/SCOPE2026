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

With each cosine scaled by √2, input energy is a²+b², and each Fourier character in the sixth moment carries the common coefficient 1/8 before multinomial counting. For a nontrivial signed balance, writing n/m=p/q in lowest terms, the absolute net signed counts are a positive integer multiple of (p,q). Their sum must be even and ≤6 because unused occurrences cancel in pairs. This gives (p,q)=(2,1) with multiplier two, (3,1) and (5,1) with multiplier one, and no other distinct-frequency cases. Recounted multinomial coefficients and phases independently; the phase-dependent terms maximize exactly at the stated congruences in each mixed case, giving the displayed F_k and factor (5/2)ρ^{6m}. For the nonresonant and octave cases set q=z²/(1+z²). At t=3/c_k, the cubic minus one is q²(B+Cq) with B and B+C negative. At a smaller t the value for q>0 is strictly smaller; above the threshold the derivative in q is quadratic with opposite signs at 0 and 1, hence exactly one interior maximum. This includes ρ=1 and excludes a pure high mode, even there. Verified the linear energy slopes by −c_k/(2B). In the third/fifth harmonic cases direct differentiation gives the stated P_3 and P_5; each has one sign variation in descending powers (ignoring zeros), positive constant and negative leading term for 0<u≤1. They each have one positive root and improve on both pure endpoints. The implicit roots have z=u/2+O(u³) and u/10+O(u³); the omitted second-order term vanishes by the Taylor expansions of the polynomials. This gives the small-radius energy fractions. The independent signed counts and fractional coefficient checks substantiate coefficients and normalization; the signed-balance and polynomial arguments cover the infinite domains.

## originality

PASS

The sixth-moment resonance identity and the unsmoothed endpoints are already covered. Applying that identity after a diagonal change of amplitudes directly gives the one-variable variational reduction, which is not counted as distinct on its own. The supported distinct claim is the global optimizer classification as damping varies: sharp thresholds with endpoint uniqueness, all-radius third/fifth mixing and phase conditions, and the corresponding onset laws. The best-of-knowledge comparison found close analytic and semigroup analogues but no checked statement covering this classification.

## value

PASS

The classification reveals which resonance balances matter to mode selection under smoothing, not just to the moment expansion. The lower mode persists up to different sharp thresholds generically and at the octave, whereas positive mixtures survive arbitrarily strong damping at the third and fifth harmonics with different onset scales. Exact optimizer and phase uniqueness conditions are useful for norming-function analyses and are not supplied by a full-space contraction bound or an unsmoothed maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
