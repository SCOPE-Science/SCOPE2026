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

Frozen proof line 54 wrongly counts only n size-(n−1) faces for all n≥2. Direct trace enumeration of the identity and the transposition gives four singleton faces at n=2, consistent with the frozen polynomial and CHECK_OUTPUT.txt; the repair restricts the n-face count and top-class assertion to n≥3 and gives a separate size bound for VC dimension. The support criterion follows by respecting disjoint cycles under all positive answers, excluding identical opposite orientations, and negating one loop in a saturated support to strand its vertex. Conversely pair the negative-loop vertices, using one unqueried vertex if needed, and fix unused vertices; negative edges then have fixed endpoints. Orienting each chosen pair cancels the 2^e in unordered pair enumeration, and removing saturated loop cases gives the EGF. For Littlestone dimension a positive answer removes one or two vertices and the now forced coordinates cannot split any subsequent query; the base cases each contain one concept. Facets use n−1 vertices or are loop-free perfect matchings, with the stated cardinalities and counts. When n≥3 no perfect matching has n−1 cells; a size-(n−1) unsaturated face cannot have edges. The diagonal boundary therefore generates the integral top kernel (double omissions equate the signed coefficients) with no top boundaries. The disjoint-edge sampling product has log −2m(m−1)/n+O(m/n+m³/n²) in the critical range, where the chance of any diagonal is ≤m/n; the supercritical limit follows by monotone coupling. The frozen checker and captured output were read, not executed, and a separate bounded direct trace check at n=2 and n=3 corroborated the corrected boundary.

## originality

PASS

The correction changes no surviving large-order claim or closest-source comparison. The material distinction is the complete Boolean trace criterion for disjoint monomer and dimer queries with unrestricted involutions, including the saturated-loop obstruction, together with its quantitative and topological consequences. The nearest assignment-matrix and matching results use materially different hypothesis families.

## value

PASS

This is a natural all-order classification for query learning of symmetric permutation matrices. It identifies a precise effect of fixed points even after disjointness and symmetry have been accounted for. The same criterion determines all faces and facets, the top integral class and a sharp sampling threshold that differs measurably from the bipartite assignment model. The separate n=2 correction preserves these substantive consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
