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

The minimal nonfaces are precisely the pairwise-intersecting triples of distinct two-subsets (stars or triangles). I independently used this characterization to enumerate all faces, and used coface-first matching rather than the frozen coreduction program. The three full oriented Hasse DAGs have respectively 232, 159, 72 faces; 720, 471, 168 covers; 111, 77, 33 matched pairs; and critical counts {0:1,3:9}, {0:1,3:4}, {0:1,2:5}. The acyclic-matching theorem therefore gives the asserted wedges: with one vertex and just one positive cell dimension, the attaching maps are constant. The S5 action on two-subsets transports the computation to every vertex. The relative chain complex of (K,D_v) is the augmented link chain complex shifted by one, by removing v from each surviving simplex (with v oriented first). Thus the pair sequence gives exactly 0 -> Z^4 -> Z^9 -> Z^5 -> 0 over Z; the free quotient makes the image primitive and gives a noncanonical splitting. The ranks describe the image and quotient, not recovery of four distinguished basis elements. Replay: python3 /workspace/reproductions/2.py; the original script and expected output were inspected, not executed.

## originality

PASS

The ambient rank nine is already known via the earlier exact total-cut record. The supported contribution is the complete local wedge profile and its integral inclusion consequence; neither duality applied just to the known ambient calculation nor an unrelated nine-sphere result computes the puncture. No equivalent or dominating statement for the local claim was located in the inspected evidence.

## value

PASS

Petersen is a canonical nonbipartite test for a graph complex studied on bipartite families. Knowing the ambient nine classes does not tell what survives a vertex failure; the exact local wedge types and primitive rank-four image distinguish local loss of five free classes from possible torsion or different local topology. The classification is uniform for every vertex and useful at its finite scale, without claims about multiple punctures, particular generators, or equivariant splittings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
