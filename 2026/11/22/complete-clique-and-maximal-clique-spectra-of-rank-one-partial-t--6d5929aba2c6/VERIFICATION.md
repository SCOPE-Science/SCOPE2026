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

For distinct rank-one constants A→a and B→b, two nonempty equal composites would force A=B and a=b. Thus commutation is exactly mutual zero products, b not in A and a not in B. For image set H and complement R, each image can carry one map whose domain contains that image, or a nonempty selection from the 2^|R|−1 nonempty domains contained in R; choices at distinct images are independent. This gives P_n. A maximal clique must saturate any external image, which then uses every point of R in its domains and prevents any new image. If there are no external images, the only extension risk is an unused point of R; its singleton identity can be added exactly when that point is absent from every domain. Each point in R must therefore assign itself to a nonempty subset of the self-domains. These two disjoint cases prove M_n, including R empty. For h<n the size is at most h(2^(n−h)−1), strictly below 2^(n−1)−1 if h>=2 by h<=2^(h−1). The h=n case has size n. At n>=4 this leaves exactly n one-image cliques of all external maps. The proof's one-image equality sentence at RESULT.md line 43 should be restricted to n>=3 (and h<n): at n=2 a singleton self-map ties the external size one, but the maximum is two and the finding does not claim its maximizer classification there. Independently reconstructed direct pointwise compositions and counted all cliques and extensions for n=1–4, confirming every coefficient, with P_4 total 1376, M_4 total 221, and four degree-7 terms counted with multiplicity. Small-case checks do not replace the uniform argument.

## originality

PASS

Credit the exact commutation rule and the extremal size and structure to the applicable 0-Rees matrix framework of Paulista. The separate contribution is the two complete labelled enumerators for the singleton-output induced graph. The strongest same-day Resultary record genuinely contains this graph as an induced subgraph, but its actual enumerators do not specialize to the two polynomials just by evaluating their variables; in particular the ambient maximality census excludes some induced maximal cliques. No precedence is inferred from the catalogue date.

## value

PASS

Rank one is a canonical stratum of the partial transformation monoid. The two labelled polynomials give fine information not determined by its already covered clique number: how idempotent and external-domain choices combine, and when every possible extension is blocked. The exact distinction between ambient and induced maximality is useful in comparing partial maps with relations and partial bijections. The coverage of extremal size alone does not reduce the two enumerators to a rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
