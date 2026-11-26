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

In T_n all nonadjacent pairs are at distance two, so the forbidden triples are induced three-vertex paths. Components of a selected induced cluster graph are pairwise intersecting edge families on mutually disjoint supports in K_n; one incident pair ab,ac shows the only non-star possibility is the whole triangle abc. Unused vertices contribute singleton blocks. The weights at support sizes 1, 2, 3 and k>=4 are 1, z, 3z^2+z^3 and kz^{k-1}, yielding the first EGF. Maximality excludes two unused vertices, two-edge stars, and any unused vertex when a selected star exists. Conversely, an edge crossing occupied components meets a selected edge in each, and those two old edges are disjoint; this supplies the general crossing case in line 48. An added leaf edge in a star of at least three edges or an edge from an unused vertex into a triangle also creates a forbidden triple. Thus the maximal modes are full coverage by allowed components, or a single unused vertex with only triangles, giving exactly the second EGF including the formal n=0,1 terms. For maximum size, each nontriangle support loses exactly one selected edge relative to its vertex count, giving the claimed residue cases. In the full-coverage maximal mode, twice the edge count minus n is additive: zero for a K2, 3 for a triangle, and k-2 for a k-vertex star (k>=4). This corrects the informal half-support arithmetic in line 58: a triangle and a five-vertex star each have excess 3/2 above half their support. For odd n, an odd component is necessary, the least doubled excess is 3, and equality is exactly one triangle or one five-vertex star plus disjoint pairs. The unused-vertex mode never ties the minima for n>=2. Counting labels gives both extremal formulas. Private replay /workspace/branches/replay/triangle.py and triangle.txt used actual shortest paths and all legal subset extensions, reproducing both complete arrays through n=7 and checking extremal coefficients by exact extraction through n=15. The proof, not these finite checks, covers all n.

## originality

FAIL

The first of the two central EGFs is explicitly the same as the earlier 2026/10/13 Resultary Finding after a variable rename, which also already gives its coefficient recurrence and the divisible-by-three maximum multiplicity. The nondivisible maximum formula extracts a coefficient from that earlier series at the known degree. The remaining maximal enumerator is not printed in the inspected earlier sources, but follows mechanically by the labelled set construction from the previously specified maximal component and coverage restrictions, with an elementary forbidden-triple converse. It is explicitly present in a later record under the equivalent maximal-cluster formulation; that later record alone does not establish earlier priority. The finding as frozen is not an original pair of enumerators and extremal counts.

## value

FAIL

Counting by cardinality is natural, but the complete all-set distribution was already available. The remaining maximal polynomial amounts to the elementary labelled-set count of the allowed components from the earlier maximality proof (with the direct single-edge obstruction for the converse). Its lower extremal coefficient reduces to matching counts and the two known tight support types. No mathematically substantive remainder beyond this routine translation and coefficient extraction was established, so no repaired claim is issued.

The dated certificate retains the supplied scientific assessment, sources and limitations.
