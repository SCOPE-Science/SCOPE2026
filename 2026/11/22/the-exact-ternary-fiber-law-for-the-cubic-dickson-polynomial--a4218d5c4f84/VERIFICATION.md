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

For x=3u, f(x)=9(3u³−u); the divided difference of 3u³−u is a unit, so the branch bijects after reducing precision by two, and the original fiber has three lifts. On x=±(1+3u), the factorization f(x)+2=(x−1)²(x+2) and oddness give the reflected outputs ±(−2+27u²(u+1)). At k≤3 each signed branch collapses to its corresponding target. For k≥4 the quotient has precision m=k−3, leaving nine lifts. Modulo three the u=1 and u=−1 balls give the two simple branches onto t=2 and 0 respectively. On u=3v the output quotient is 9v²(1+3v); the unique square root s(v)≡1 mod 3 has s(v)−s(w) divisible by 3(v−w), so v↦vs(v) preserves every congruence distance and thus permutes each residue ring. This yields three lifts per square root after reducing from precision m−1 to m−2, and literal collapse for m=1,2. Dividing a nonzero square target of valuation 2j by 3^(2j) gives two simple unit roots and 3^j lifts each; zero has 3^floor(r/2) roots. For even r=k−5 the unique square-root maximizer is zero; for odd r it is 3^(r−1), translating back to the two stated shifted targets. The image check follows because each signed branch has exactly the two simple target classes modulo three and the critical image adds none. Independently enumerated all 265,719 targets through k=11, comparing the direct polynomial histogram with the square-normal form and checking the displayed peak locations and counts at both parities.

## originality

PASS

The supported distinct result is the exceptional ternary, target-by-target one-step fiber law and its exact sharp maximizers. The thirteen-class image is established coverage, and the same map's depth census is a different invariant. An older primary Galois-ring paper remains a material unverified priority risk, not evidence of either equivalence or absence.

## value

PASS

The prime equals the degree and both nonzero classes are singular; image-size bounds and the simple branch do not control concentration. The formula gives exact local preimage counts at every precision, including peak sizes of order 3^(k/2) and the alternating locations of those peaks. This is a usable invariant for counting solutions of a natural exceptional congruence or analyzing the pushforward of uniform measure, beyond recomputing a known image size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
