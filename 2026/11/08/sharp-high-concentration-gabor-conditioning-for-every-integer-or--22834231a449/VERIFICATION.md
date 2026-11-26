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

The replacement resolves the frozen ambiguous universal 'minimizing sequence' claim: at a fixed off-midpoint x=1/4, S and A both tend to zero, so an absolute gap tending to zero does not localize. The revised relative criterion S/A→1 includes exact minimizers and is proved. Under the positive-sign Zak convention translation multiplies by e^(-2πikω) and modulation by b shifts ω to ω-b and multiplies by e^(2πibx). Fourier Parseval in the two modulation cosets yields S=|Z(ω)|²+|Z(ω+1/2)|²=2(|E|²+|O|²), with no missing oversampling factor. Continuity makes its extreme values optimal frame bounds; all finite λ are covered for existence by the known finite-type totally positive frame theorem. The coefficient ratios make e^(-s)P_n(s) decrease, with value one at zero. The leading coefficient gives h=g(1/2)∼n!/(2n)! λ^n e^(-λ/2). On [0,1/4], separation of the nearest even translate gives S/h²→∞ uniformly. On [1/4,1/2], the next even and odd distances are at least 3/2 and 5/4; squared cross terms with principal terms of size O(λ^n e^(-λ/4)) are o(h²) uniformly. Eventual convexity of e^(-2s)P_n(s)^2, from the leading term of its second derivative times e^(2s), minimizes the two-term leading symbol at x=1/2 and gives A∼4h². Away from the midpoint the nearest-even contribution is uniformly larger by a diverging factor, proving relative localization. Near x=0 the odd channel is uniformly o(1), and g≤1 bounds the even channel; evaluating at x=0 matches the limiting upper bound 2. Division gives the stated factorial condition law. Frozen verification notes and checker were inspected rather than executed; finite grids do not establish these uniform estimates.

## originality

PASS

After clarifying the localization scale, the distinct claim is the sharp fixed-lattice large-λ law for each fixed higher convolution order. Frame existence, the Zak method, and the first-order equal-rate bound are credited as known. The strongest inspected exact-fiber precedents have no polynomial factor, and the strongest general window-class theorems establish existence or Zak zeros, not the extremum of the sum of two squared channels in this limit.

## value

PASS

A qualitative frame theorem misses the ill-conditioning of a narrow window at a fixed sampling density. This computes both the exponential and order-dependent polynomial deterioration, with a sharp prefactor for the specified natural normalization, and identifies the time region responsible for it. The precise relative formulation gives information at the scale of the optimal lower bound, unlike absolute closeness which becomes vacuous here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
