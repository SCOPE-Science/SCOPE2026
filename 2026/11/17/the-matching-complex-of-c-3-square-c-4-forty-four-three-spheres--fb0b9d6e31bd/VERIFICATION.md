---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The frozen graph is K3 Cartesian C4 with 12 vertices, 24 edges. An independent edge-mask matching enumeration counted 2764 faces including empty and f=(24,204,748,1149,588,50). Rebuilding the stated pivot matching gives 1358 pairs, one critical vertex, 45 critical three-cells and one critical four-cell. Independently constructed oriented Hasse graph is acyclic on all 2763 nonempty faces and 10488 incidences. Exact signed integer Morse projection gives seven distinct ±1 coefficients (-1,+1,-1,-1,-1,-1,+1) on masks 0x90102,0x94002,0x210500,0x404410,0x408401,0x40c010,0x480101; its primitive attaching map kills one of 45 S3 generators yielding wedge 44 S3. Independent GF2 chain ranks (23,181,567,538,50) match. Evaluating all 48 S3 x D4 edge permutations via signed invariant simplices reproduces every of 15 character classes and rational invariant dimensions 1 (full),4 (rotation subgroup). No equivariant wedge or integral quotient classification is inferred.

## originality

PASS

Best-of-knowledge PASS. The published 3x4 grid classification is P3 Cartesian P4, not C3 Cartesian C4; boundary wrap and triangle close both directions, changing edge count, homotopy ranks and the automorphism representation. Published dihedral character tables for rectangular matching grids, perfect matching complexes or total-cut complexes concern different graphs or functors. No verified stronger all-toroidal-grid result implying the full rational character found; Jonsson 2005 unpublished grid manuscript remains unread.

## value

PASS

A complete exact integral homotopy type plus full rational row-column character for the first naturally periodic three-by-four toroidal matching complex is a concrete natural object and invariant: it distinguishes periodic boundary conditions from rectangular grid results and resolves genuine quotient homology not derivable from Betti ranks alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
