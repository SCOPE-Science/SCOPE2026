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

With nonempty neighboring-disjoint subsets, a cell cannot be invariant under any nontrivial 7-cycle rotation: all seven coordinates would have to agree. A fixed point would force just such an invariant open cell. The actual ordinary quotient therefore has one cell per free orbit; rotations induce the Koszul sign on the oriented product factors. I independently generated orbit representatives using a different canonical order, checked the full chain squares, and reduced the integral boundary by degree-descending sparse unimodular unit-pivot cancellation. The cell counts are (312,1452,2640,2340,1008,168); the different pivot order gives 3958 cancellations, leaving ranks (1,1,1,1,0,0) and the sole nonzero boundary [−14] in degree 2. This gives the claimed integral groups. The cover one-skeleton is connected by single-coordinate changes through all 2184 proper colorings. In the quotient, a spanning tree leaves 1141 generators, with actual triangle and square words having the correct exponent sums on all 2640 two-cells. A different tree and Tietze order gave 1140 single-occurrence eliminations and one generator, with 42 nonzero relators of length 14. With a single generator, a cyclically reduced length-14 relator is g^14 or g^(−14). The difference from 46 in the frozen transcript reflects the choice of reduction, not a difference in presented groups. The connected regular seven-fold cover gives kernel the unique index-seven subgroup C₂ of C₁₄. Replay: python /workspace/checks/hom.py (helper words.py; transcript /workspace/checks/hom.txt). No CW chain calculation was taken to determine higher homotopy or a manifold model.

## originality

PASS

Pass is for the exact fundamental groups of the cover and rotation quotient, with an explicit finite presentation rather than a calculation of its abelianization alone. The quotient homology itself follows from Kozlov's cited covering-space cohomology computation by standard covering spectral-sequence arguments; it is not an independently novel invariant here. The related pentagon result has a different source cycle and uses a different action, and the strongest inspected general sources do not show the requisite fundamental group of the seven-cycle cover.

## value

PASS

The passage from the pentagon benchmark to seven source vertices gives a natural next orbit-space case. Knowing that the actual group is cyclic, not just that the abelianization has order fourteen, determines the fundamental-group extension and the fundamental group of its natural covering space. This topology is not read off from cohomology and is useful in comparing combinatorial cycle-colouring spaces and their symmetry quotients. The homology replay is supporting context; the value does not rest on recomputing that already implied table or claiming a lens-space homotopy type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
