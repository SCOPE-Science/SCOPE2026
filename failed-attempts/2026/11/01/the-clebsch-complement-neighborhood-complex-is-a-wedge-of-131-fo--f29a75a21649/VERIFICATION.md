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

The XOR graph has parameters (16,5,0,2); the open neighborhoods used for the main theorem are those of its ten-regular complement. Independent replay produced the sixteen distinct ten-vertex facets, 11,804 nonempty faces, 4,780 collapse pairs and 1,050 toggle pairs. All 65,680 covers sort acyclically; using the globally reversed arrow convention in the frozen verifier does not alter acyclicity. The critical cells are one vertex, six 3-cells and 137 4-cells. Integral signed Morse elimination reproduces the stated minor on columns 2,4,9,10,23,26 with determinant +1. The six corresponding 4-cells together with the 3-skeleton have a unimodular integral degree map and form an acyclic simply connected, hence contractible, CW subcomplex. The other 131 attaching maps to that subcomplex are null, giving the exact wedge of four-spheres. The dominance condition is that no closed C-neighborhood is wholly in a face; complementing shows D(C)^∨ = N(H). Combinatorial Alexander duality on 16 vertices gives degree 16−4−3=9 in D(C) and no other reduced integral homology. The argument does not infer its homotopy type from its homology.

## originality

FAIL

The archived dominance result 0b2c4cb32b46 explicitly proves the stronger dominance homotopy type for the identical graph. Combinatorial Alexander duality transfers the homology but not, by itself, the open-neighborhood homotopy type. However, the actual prior proof provides a complete acyclic face matching. Complementing its pairs yields a relative matching on the missing faces of N(H) in the full simplex, with only 131 critical 5-cells. This implies the necessary 3-connectivity and hence the four-sphere wedge. Thus the prior exact certificate, not merely its stated homology or an analogous graph, covers the main result by a direct inference.

## value

FAIL

The exact integral homotopy type of this canonical halved-cube complex would be valuable if it required a distinct calculation. Here the earlier exact dominance certificate already yields it by complementing the matching, and the dominance corollary is explicitly weaker than the earlier result. The separately verified integral minor is useful corroboration, but no new facet structure, equivariant invariant, or other independently motivated consequence is claimed. There is no distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
