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

Independently derived the radius-two witness sets for the unit metric graph. On an open edge ab, integer endpoint distances give precisely N_1[a] union N_1[b], contained in each of N_2[a] and N_2[b], so vertex witnesses alone suffice here, though the underlying definition allows all points of an edge. Replayed with sets: generate edges from the three listed arms; square the closed-neighborhood relation, retain all nonempty subsets of each radius-two ball, and do exact GF(2) row elimination on incidence supports indexed by consecutive face sizes (combine rows by symmetric difference, pivoting on the least surviving column). All ten listed facets matched. For the full nerve the face vector was (10,45,114,134,74,20,2), ranks of boundaries from degree 1 upward (9,36,76,56,18,2), and reduced Betti vector (0,0,2,2,0,0,0). Repeating on each intrinsic cycle separately and unioning faces on common labels gave (10,36,66,55,14), ranks (9,27,39,14), and reduced Betti vector (0,0,0,2,0). The cycle-nerve intersection is exactly the simplex on {0,1,2,3}. Their union is contained in the theta nerve, both by finite subset testing and because any cycle witness persists when metric distances can only shorten after adding the other arm. The degree-two discrepancy proves that the natural inclusion is not a homotopy equivalence. It does not identify the map in degree three or determine integral or full homotopy types. Inspected the frozen verifier as text.

## originality

PASS

Best-of-knowledge pass for the concrete higher-homology mismatch and consequent failure of the inclusion, not for the even-scale neighborhood identity or cycle-nerve computation in isolation. The prior gluing work gives genuine Čech results and a related obstruction to one proof criterion, but not the homology mismatch asserted here.

## value

PASS

An exact ten-vertex example isolates where gluing the constituent Čech nerves can miss genuine homology: each piece and their union have no degree-two classes, while the glued metric graph has two. The common path is a natural overlap of two heptagons outside the short-overlap Rips guarantee. The calculation is small enough to serve as an exact test for candidate graph-gluing principles and algorithms. Its value is as a counterexample at this scale and with these centers and coefficients, not as a minimality, threshold or classification claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
