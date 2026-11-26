---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The graph is the intact 25-vertex Cartesian product, with sum of cyclic coordinate distances. A three-point set is forbidden exactly when its largest pair distance is the sum of the other two; the no-forbidden-triple property is hereditary. Increasing extensions exhaust every admissible set, and the absence of seven-vertex faces rules out all greater sizes. In X and Y the ordinary boundary columns delete one vertex over F_2; the relative basis consists of faces containing the discarded vertex, and deletion of that vertex gives zero in the quotient. The fresh exhaustive calculation gives f_X=(25,300,1400,2450,1360,50), f_Y=(24,276,1232,2058,1088,38), f_rel=(1,24,168,392,272,12), and positive-degree boundary ranks X=(24,276,1074,1290,50), Y=(23,253,935,1038,38), and relative=(1,23,139,241,12). Subtract adjacent ranks (and the degree-zero augmentation when reduced) to get all displayed Betti numbers and the other vanishing. To cross-check the natural-map ranks without choosing coordinate cycles, exactness gives b_rel(j)=b_X(j)-rank(i_j)+b_Y(j-1)-rank(i_(j-1)). Starting from degree zero gives 44,74,12 in degrees 2–4 and forces zero outside. This matches the independent direct quotient-of-cycle-span computation. The degree-three kernel and cokernel have dimensions 85-74=11 and 86-74=12. Translations of the intact graph give the identical result for any deleted landmark.

## originality

PASS

The contribution is the exact mod-two homology and actual induced map for the vertex-deletion pair in one fixed geodesic general-position complex. The maximum face size and general-position framework are not treated as new. The stronger-looking enumerative and ladder-homology sources examined do not supply the puncture ranks, and no exact matching homology table was located apart from the assigned record.

## value

PASS

The graph is a small nontrivial symmetric toroidal grid; retaining the ambient metric while removing one site is the natural induced vertex-deletion operation on the geodesic complex. The result quantifies an actual failure of homological persistence: a change from 85 to 86 in the middle Betti number hides eleven lost independent classes and twelve new ones. Knowing the complete inclusion and relative data is materially more informative for this example than an isolated Betti census or the already studied maximum face size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
