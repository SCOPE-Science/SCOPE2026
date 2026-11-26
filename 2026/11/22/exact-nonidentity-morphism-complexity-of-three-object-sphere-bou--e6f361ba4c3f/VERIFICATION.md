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

Positive H₂ forces a nondegenerate composable pair; acyclicity orders its three distinct objects and excludes all reverse arrows and higher nondegenerate simplices. Write a,b,c for the 01,12,02 hom-set sizes. Counting cells gives s=2−a−b−c+ab=(a−1)(b−1)−(c−1), so u=a−1 and v=b−1 are positive and c=uv−s+1≥1. Conversely use the anchor label h₀ on the first row and column and put each of the c−1 other labels on a different interior cell. With f₀,g₀ as the spanning tree, the corner triangle kills h₀ in the fundamental group, the other anchor triangles kill remaining fᵢ,gⱼ, and the remaining labels are killed by their assigned triangles. There are no associativity constraints from triples of nonidentities. The resulting simply connected 2-complex has free H₂ of rank s, and spherical representatives give a homotopy equivalence by Hurewicz and homological Whitehead. Thus the Euler bound is attained for every feasible pair. For fixed u the cost increases strictly with v, and u>s is dominated by (s,1); the stated finite minimization and scale bounds follow. In particular s=1,7,8,100 have costs 5,10,9,23.

## originality

PASS

The three-object formalism, thin-factor examples, and object minimum are prior. The exact minimum counting all nonidentity arrows, plus the arbitrary feasible-pair realization needed for sharpness, survive the bounded primary literature and Resultary comparisons. No chronological priority is inferred relative to the same-day records.

## value

PASS

After minimizing objects it is natural to ask how expensive the allowed categories are in arrows, including composites. The result optimizes this exact invariant for every sphere multiplicity and replaces the known linear size family with an optimal square-root scale; the formula determines concrete minima even when they are nonmonotone. The construction proves attainability rather than just an Euler obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
