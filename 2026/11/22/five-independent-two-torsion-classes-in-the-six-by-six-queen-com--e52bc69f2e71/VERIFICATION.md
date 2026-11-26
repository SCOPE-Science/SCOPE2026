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

In the barycentric subdivision a chain has at most one face of each cardinality. If two points in the same closed flag simplex are in the same group orbit, the action has to fix every vertex in their support, because its size identifies it uniquely within the closed simplex. The quotient cells thus have embedded closures and are oriented by size, with the signed deletion boundary. I checked the supplied proof and independently constructed the geometric quotient chain complex using injective columns on selected rows and descending flags modulo the stabilizer of the largest face. The run /workspace/branches/check4.py counted 337,3541,10110,11166,4620,360 cells and checked every chain-square identity. Direct integer unit-pivot cancellations, without importing the supplied collapse list/matrix, left ranks (1,0,5,6) with only the degree-three differential nonzero. The entries are all even, and the halved matrix has maximal minors (1,0,0,0,1,0), so the image is exactly twice the entire degree-two chain group. This proves reduced H2=(Z/2)^5, H3=Z, and zero otherwise. The unquotiented comparison is a count of independent torsion summands, not a claim about the image of the induced homology map.

## originality

PASS

The strongest same-board sources establish the unquotiented integral homotopy type, the rational homology character and fixed-space data, not this orbit-space integral calculation. Credit the free rational rank to that prior character. The strongest exact orbit-space analogue is on a different board. The pass concerns the complete integral result, especially the five degree-two 2-torsion classes, and not the previously determined rational part.

## value

PASS

The six-board queen complex already exhibits an integral torsion class, and the full symmetry quotient of this natural action is a motivated test of torsion under a nonfree quotient. The exact five summands reveal behavior unavailable from the rational character and distinguish the case from the smaller torsion-free quotient. The complete integral groups can be used for comparisons with fixed-space calculations or other coefficient systems without claiming a homotopy classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
