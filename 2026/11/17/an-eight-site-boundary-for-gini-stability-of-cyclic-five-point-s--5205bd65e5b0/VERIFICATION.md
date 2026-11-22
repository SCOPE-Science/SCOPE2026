---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The classical least-squares centered quadratic stencil is (-3,12,17,12,-3)/35 and fixes constants. Every real vector decomposes into positive nested binary cuts modulo constants; the Gini pair sum is additive over such nested cuts, while postfilter Gini obeys the triangle inequality, so the exact operator norm is the maximum over nonempty binary masks. For each n=5,6,7,8 independent exact integer enumeration visited all (2^n−2) masks: totals 30,62,126,254=472 and fixed-cardinality maxima (110,180);(157,256,303);(204,338,414);(251,420,531,560). Quotients give sharp L_n=(6/7,101/105,69/70,251/245). The n≥8 impulse formula follows algebraically from five distinct nonzero entries and their 10 mutual variations: G_n(35S_ne0)=47n−125, G_n(e0)=n−1. Thus strict amplification for all n≥8 is proved without extrapolating finite cases. The triangle inequality over five shifts gives L_n≤47/35, attained only in the n→∞ supremum. Correctness is limited to the specified periodic, equal-mass Gini setting; per-size norms n≥9 are not claimed.

## originality

PASS

Best-of-knowledge PASS for sharp Gini operator norms on short cyclic rings and the universal n=8 amplification boundary. Candan–Inan 2014 full primary article explicitly derives this same five-coefficient stencil (equation (4) and text p.205) but studies minimum-norm polynomial fit and implementation, not complete-pair Gini amplification. The related full Resultary three-tap Gini theorem establishes an exact norm for a positive averaging filter, not the signed five-tap SG multiplier; its cut variance identity cannot infer the present maxima. The exact 47/35 absolute coefficient sum is elementary and not claimed novel alone; the finite exact cut threshold and its analytical all-size witness are the meaningful new statements.

## value

PASS

The five-point Savitzky–Golay filter is widely used to reduce measurement noise but has negative outer weights, so a global pairwise-dispersion contraction property is not automatic. Exactly locating the eight-site transition, with all-real-input proof and sharp family-wide amplification envelope, is a meaningful natural stability boundary for an established operator, not just a rederived coefficient stencil or arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
