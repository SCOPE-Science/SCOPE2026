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

For two particles the simple graph meets the deleted-product subdivision conditions (paths between distinct essential vertices have at least one edge and essential cycles at least three). The discrete-model inclusion respects the particle swap, so passing to its free quotient gives the unordered model; within-part permutations also respect the inclusion. The product rule gives the stated oriented second boundary. There are 36 vertices, 182 one-cells and 198 squares, and no three-cells. Independently reconstructed matrices satisfy ∂1∂2=0 and have rank ∂2=129 over Q by exact row reduction. Enumeration by vertex subsets and cyclic permutations with least vertex first and reversed copies removed gives 4,395 cycles and 1,206 unordered disjoint pairs with the six stated counts. The 72 triangle pairs are also counted directly as 3·2·4·3 by first distinguishing the triangle through vertex 0. Independently oriented torus chains all have zero integral boundary. The exact determinant of the minor at the frozen JSON indices is +1, so the rational kernel of rank 69 projects injectively to its selected square coordinates and the selected 69 chains map onto their entire integral coordinate lattice. Hence they generate the whole integral H2; reconstruction with that minor also gives integral coefficients for all 1,206 pair tori. The three stored 36-term vectors are in the exact kernel, and project to the identity on the complementary triangle indices 64,70,71 (zero-based), so generate all integral relations. Recomputing the six signed triangle actions from triangle orientation and the sign of swapping circle factors reproduces all stored action matrices. The S2 and S3 generators are −I; S4 traces on 1, (12), (12)(34), (123), (1234) are 3,−1,−1,0,1, exactly those of the sign twist of its standard representation over Q.

## originality

PASS

The distinct contribution is the specific shortest-torus integral presentation at the unequal tripartite boundary and its actual relation action, not the cubical model, the general intersection framework, or merely the rank. Closely matching integral presentations apply to other graphs; the strongest general tripartite symmetry statement inspected excludes a shore of size two and concerns rational homology rather than this integral presentation.

## value

PASS

The part-size-two boundary is missing from the inspected three-factor theorem, and the other two shores allow a natural family of disjoint shortest cycles. Integral generation by those shortest cycles settles whether longer cycles or non-toric cycles are necessary for H2; the full signed kernel and symmetry then say how the geometric generating tori are redundant. This is a meaningful integral boundary case, not just a Betti number for an arbitrary nine-vertex graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
