---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A minimal induced restriction with nonzero reduced H_d in a flag complex has a vertex deletion with zero H_d at each vertex. The deletion/link sequence injects H_d into reduced H_(d-1) of the link. Inducting from a nonedge in degree zero gives at least 2d link vertices; there must also be a nonneighbor since otherwise the complex is a cone. Thus the bound is 2d+2, with equality forcing exactly one nonneighbor per vertex and the join of d+1 copies of S^0. In particular any ambient degree-two carrier of size six must be octahedral. The exact independent reproduction exhausts all 5005 six-edge subsets of Petersen; the incidence-conflict graph is a three-edge perfect matching on 110 of them, and the 120 symbol permutations give orbits of sizes 10,60,40 with omitted-vertex center adjacency types 3,1,0. Their oriented eight-triangle join cycles all have zero signed boundary. The faces in degrees 0 through 4 number 15,75,145,90,6. Connectivity gives rank B1=14, and the modular lower bound 61 for B2 attains the rational upper bound 75-14. The Smith form of B3 has 79 unit factors, so its image is saturated and H2 is free of rank 145-61-79=5. Adding one orbit representative to B3 gives 80 unit factors in each case; hence its class is nonzero, with torsion-free quotient, and symmetry proves primitivity for all 110. Adding all cycles from each orbit gives rank 84, with nonunit Smith factors [2], [], [] respectively. The map from these augmented cokernels to im B2 has free image of rank 61 and finite kernel H2/L; hence the torsion subgroup is exactly the desired quotient, giving indices 2,1,1. The independent replay command is python3 /workspace/branches/3a34fa10-728d-419e-a16f-4839d823c187/independent_check.py exact, using exact SymPy Smith forms. The log lines 12–25 record the decisive full run, not just the earlier probe. The supplied verifier was inspected but not executed.

## originality

FAIL

The distinct Resultary record d78821241a7c has exact statement-level coverage of the frozen focal result: the same Petersen matching complex, 110 minimum six-vertex octahedra carrying primitive classes, H2=Z^5, three S5 orbits of sizes 10,60,40, and the same integral quotients (Z/2,0,0). It proves these by the same lattice presentations and gives additional equivariant character results. This is exact coverage, not a title match or an identification of the frozen record with itself. The dates do not determine dependence or priority. The original orbit labels by adjacency at the omitted vertex are a descriptive refinement, not a distinct index theorem.

## value

FAIL

The primitive-but-index-two phenomenon is a meaningful invariant of a natural complex and would have scientific value as a distinct classification; it is not merely the known Betti number five. As a standalone contribution in the present comparison, though, the entire useful classification and saturation obstruction are already furnished by the matched result. The omitted-center adjacency counts give an intrinsic way to label the same three orbits, but the frozen proof uses the same finite orbit census and Smith calculations and derives no further spanning criterion from that label. That residual observation and independent reproduction do not constitute a separate valuable finding for acceptance here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
