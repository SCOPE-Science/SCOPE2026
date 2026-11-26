---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Banerjee–Ghosh Dastidar, arXiv:2610.20135v1 p. 3, Theorem 1.5 and eq. (1.4), really give the two valuation forms for positive odd weights and this strongly unimodal generating function. Modulo 3 forces 3∤m and the stated complementary mod-3 prime classes; the symbol restriction gives p≡5,7 (mod 8). Evenness of 3n−1 forces m even only for ε=1. Conversely the resulting products are even and 2 mod 3, hence give odd integral n. Prime valuations recover ε,p,k,m uniquely. Counts for k≥1 are O(√X) by summing √X·p^(−2k−1/2); omitted tuples with p|m at k=0 contribute O(√X) by summing √X·p^(−3/2). Replacing 3X−1 by 3X costs at most one term per relevant m. For m≤X^(1/6), the fixed-modulus PNT and Li expansion at aX/m² give the second factor 1−log a+2log m and uniform error O(X(1+log m)²/(m² log³X)). The tail and the tails of the reciprocal-square moments are negligible. The restricted Dirichlet series at s=2 are 2^(−s)(1−3^(−s))ζ(s) and (1−3^(−s))ζ(s), giving S₁=π²/27, S₂=4π²/27 and T₁/S₁−T₂/S₂=log 2 with T₂/S₂=−ζ′(2)/ζ(2)−log 3/8. Substitution of a=3,3/2 and prime density 1/4 gives the two coefficients and their sum exactly as stated, with absolute errors and leading ratio 1:2. A separate bit-plane coefficient computation and valuation comparison through X=2500 agreed at all 1250 odd indices, with branch counts 118 and 221 (python3 /workspace/branches/independent_checks.py). The frozen verifier and reported runs were inspected, not executed or treated as proof.

## originality

FAIL

The primary congruence theorem does not already state the frequency law, but the distinct indexed mod-8 refinement e435dd406b7e demonstrably covers it. Its four displayed expansions sum to the frozen total, and its proof gives the uniform type-resolved prime sums and square-weight moments from which both frozen family coefficients and error follow by regrouping. The indexed refinement is later-dated by path; this is a catalogue-coverage decision, not an inference about historical priority, derivation direction or authorship from dates.

## value

FAIL

A frequency law for this natural congruence support is mathematically meaningful, and the second-order split is more informative than the pointwise criterion or leading density alone. But the existing indexed quantitative comparison already yields the whole proposed exact invariant and additional mod-8 information. No distinct valuable coefficient, regime or consequence remains in the frozen Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
