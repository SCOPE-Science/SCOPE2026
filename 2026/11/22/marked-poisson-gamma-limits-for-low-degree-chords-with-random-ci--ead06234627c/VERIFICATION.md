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

Checked the hypotheses and conclusion of Acan Theorem 4.1: with k=K+1 the minimum degree in the induced length-at-least-k diagram is at least k with high probability, so the original degree exclusion is valid. In the spacing proof, the uniform origin should be understood as the angle of a distinguished sampled endpoint, not a uniformly chosen external cut; this is consistent with the formula for the first endpoint. I independently checked the marked theorem without the spacing or core reduction. Conditional on any matching of the original unsorted iid angles, the n endpoint pairs are iid, so each pair's shorter-arc length A has density 2 on (0,1/2) and its midpoint is independent Haar. For r prescribed marked chords with scaled lengths y_i bounded by B, the set of midpoint arrays whose arcs intersect has Haar measure O_r(B/n). Off this set the r chords do not cross each other. Each remaining independent chord crosses i with probability 2(y_i/n)(1−y_i/n) and crosses both i and h with probability 2y_i y_h/n². The probability of any double contribution is O_r(B²/n); the single-category multinomial degree vector therefore tends to independent Poisson(2y_i) variables, uniformly on bounded lengths and separated arcs. In the mixed factorial integrals, (n)_r(2/n)^r tends to 2^r, giving precisely du multiplied by 2 exp(−2y)(2y)^j/j! dy in class j, with factorization across classes and tests. Moment determinacy and bounded higher factorial moments give the joint compact-window count laws. For full tightness, d conditional on A=a is Bin(n−1,2a(1−a)); integrating shows the expected mass of class j above scaled length B is at most 2∫_B^∞ (2y)^j exp(−y/2)/j! dy for n≥2(j+1). This establishes the finite-measure topology and, by a void probability, the maximum formula for positive t. At t=0 the event is zero total count, since all lengths are positive almost surely; its probability tends to e⁻¹. The supplied VERIFICATION.md and check_chords.py were inspected without execution. Their finite matching, beta-moment and seeded diagnostics are not evidence of the limit beyond the proof.

## originality

PASS

Credit Acan for the core and the independent Poisson count laws, and the indexed results for other chord fluctuations and spatial combinatorial marks. The supported distinct increment is the joint law for fixed crossing-degree classes in physical angle and physical short-arc length, with independent Gamma marks and control of the entire marked mass. This is not a claim to originality for the degree-count Poisson marginal, the Gamma integral by itself, or fixed-site localization in a different length regime.

## value

PASS

The result explains in physical coordinates where the rare low-degree chords occur and how long they are. It resolves the needed joint spatial independence despite shared potential crossing partners, distinguishes physical length from combinatorial distance, and controls extremes as well as bounded windows. Those conclusions are useful beyond the already-known class counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
