---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PBW basis x^iy^j (0≤i,j≤2) gives dim A=9 and dim J=8. Multiplication coefficient λ^{jr} independently reconstructs w³=s[a²b x²y + ab² xy² + {t(a²e+b²c)+(1+λ)abd}x²y²], w⁴=su a²b² x²y², and w⁵=0 for arbitrary λ, where s=1+λ+λ², t=1−λ+λ², u=1+λ². Independently expanded these in symbolic characteristic-zero polynomial arithmetic, then reduced identities to all finite fields. For w²=0 the independent degree-two a²,b² terms force a=b=0 and the remaining nondegenerate d²/ce equation has exactly q² triples (c,d,e), giving C₂=q⁵. For w³=0, s=0 gives all q⁸, else ab=0 and the t-dependent condition gives C₃ as written; w⁴=0 either all or ab=0. Nested counts yield N1..N5 and establish index-four iff st≠0 and index-five iff su≠0. The t=0,s≠0 boundary has no index four yet q⁶(q−1)² index-five elements. No use of finite search for universal quantifiers.

## originality

PASS

Best-of-knowledge PASS for the complete parameter-dependent nilpotency-index census, particularly cyclotomic gaps for λ not restricted to primitive cube roots. Earlier closely matching quantum-cubic results classify the primitive-third-root s=0 specialization and the Jordan ranks of left multiplication, not the full λ-dependent counts of elementwise indices for all finite fields. The s=0 branch is explicitly prior-covered; no novelty claimed for that branch alone.

## value

PASS

The radical of the natural smallest two-generator cubic quantum complete intersection has elementwise nilpotency spectrum differing from the nilpotency class of J, and exhibits a nonconsecutive gap (index four absent, index five present). The full q- and λ-dependent count including characteristic two/three resonance is a motivated structural phase diagram with a reusable exact invariant, not a trivial root-of-unity substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
