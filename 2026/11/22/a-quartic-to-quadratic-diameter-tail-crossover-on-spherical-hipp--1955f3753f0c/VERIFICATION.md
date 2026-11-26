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

The sphere and cylinder give z²=2b(2−x), y²=4(1−b)+2bx−x² and force x=0 for an antipodal pair. For fixed 0<b<1 there are four ordered pairs. In signed x-coordinates the quadratic form is (x+y)²+K(x−y)² with K=b/[4(1−b)]>0. The ellipse area is 4πδ/√K per pair, and the product of arclength densities tends to 1+K, giving the stated C(b) after division by L_b². The period-4π parametrization covers both arcs once except for the zero-mass node, and its speed integrates to the asserted length with elliptic parameter b/2. In the moving window, compactness at b=1 restricts all events to the two ordered pole patches. In the exact sum of the two parametrized points, the y component first bounds u by O(√δ), since cos v stays away from zero; the x component then gives 1−cos v=O_κ(√δ). With the stated scaling, the squared sum divided by 8δ converges on the resulting common compact rectangle to U²+(V²−√2κ)². Its unit-level boundary has area zero. The combined Jacobian factor is 2·2·√2·8^{1/4}=2^{13/4}; product speed tends to 1 and L_1²=128E(1/2)². Dominated L¹ convergence and normalization prove the conditional total-variation statement, with the fair order mark by exchange of the sampled points. The V-slices show the stated connectivity threshold, including the strict inequality at equality. Substitution q=v²−√2κ yields the area asymptotic and the stated sequential matching; no uniformity for unbounded κ is inferred. Replay: differentiate the two local square roots in RESULT.md lines 46–58 and expand the exact vector at lines 64–80 before applying the two Jacobians.

## originality

PASS

Credit the classical family and the existing fixed Viviani coefficient. The independently compared addition is the fixed two-antipodal-pair coefficient and the resolved, marked merging-pair crossover. The inspected work does not give these; this is bounded comparison, not a historical-priority certificate.

## value

PASS

The example gives a concrete geometric degeneration in which two ordinary antipodal pairs merge. It quantifies the transition by an explicit family of normalized endpoint laws and a connectivity threshold, not just the already known isolated exponent. The exact coefficients also give a checkable benchmark for comparing arclength distance tails under coalescing maximizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
