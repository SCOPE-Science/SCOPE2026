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

For an interior unit jump, the only potentially nonzero coefficient at level k has magnitude 2^(−k/2) dist(2^k x,Z), giving the stated geometric weight r=2^(2s−1). For r<1 the Haar vector depends continuously on the jump location by the uniform geometric tail bound. Integrating jump vectors against Df proves the exact operator bound; equality requires a common signed direction of maximal vectors, and Haar completeness rules out distinct jumps on one line modulo constants. Parseval gives F_(1/2)=x(1−x), so the midpoint is uniquely optimal for r≤1/2. For r>1/2 the competitor 1/2−2^(−m) has a last positive contribution r^(m−1)/4, outgrowing the O(2^(−m)) first-term loss. On the left tent branch v−v∘T=3x²−x for v=x(1−x); direct expansion proves the square-defect identity, and reflection proves it on the right. Its discounted telescoping gives the 1/9 coefficient and +1/6 bound, while the 1/3 jump gives the lower bound or divergence for r≥1. The same defect bounds its occupation average by (1−r)/6; the discounted invariance relation on the circle makes every weak limit invariant and supported on the two exchanged points. This proves occupation selection, not convergence of initial locations. The additive bound is not claimed sharp.

## originality

PASS

Credit only the distinct sharp free-geometric-weight Haar/BV classification and its midpoint threshold. The fixed Takagi member and Hilbert reduction are not independent novelty claims. More importantly, the same-day dyadic-residual finding has an algebraically equivalent squared-defect identity and substantially overlaps the critical residue and period-two selection. That overlap does not establish priority either way and does not give the free-geometric-weight transition; the all-scale norm classification retains distinct content.

## value

PASS

Geometric Haar scale weights are a natural smoothness parameter. The result locates two different sharp boundaries: immediate loss of the ordinary L² midpoint extremizer at positive smoothness, then failure of boundedness at s=1/2 with a sharp blow-up coefficient on approach. This gives concrete extremal information beyond a levelwise bound or a single critical orbit calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
