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

For X=Ind_2(K4□K4) the induced-degree≤1 face predicate, exhaustively evaluated for all 2^16 subsets, gives cardinality face vector (1,16,120,384,528,144). Independent bitset elimination of the full mod-two simplicial boundaries gives ranks (15,105,279,144). Since characteristic-zero ranks are at least these and chain dimension/im(d^2=0) force upper bounds successively at exactly the same values, rational reduced homology is concentrated in degree three of dimension 105. The full graph automorphism group is (S4×S4)⋊C2 of order 1152. Independently enumerated its 1152 cell permutations, computed the exact signed Lefschetz trace over all invariant faces, and confirmed full-group trace sum zero. The packaged verifier independently computes invariant faces via orbit cycle unions, 20 conjugacy-class values, tensor Specht multiplicity matrix, ± diagonal extensions and row/diagonal invariant dimensions 3,5,3; the complete script and proof were read. A finite exhaustive calculation establishes only this fixed board, not a theorem for every rook graph.

## originality

PASS

Nonequivariant 105-sphere topology is acknowledged as prior. The new result gives a 20-class full automorphism action, explicit rational Specht and wreath-product decomposition, and subgroup quotient Betti numbers; these are not implied by adjacency spectral/critical groups or by the nonequivariant rank alone. Relevant primary higher-independence papers concern different graph families, and no exact rook dissociation equivariant table surfaced in searches.

## value

PASS

This natural sixteen-cell rook dissociation complex has large nontrivial symmetry; its full 1152-element rational action and 20-class character are not fixed by the known 105-sphere count. The explicit 105-dimensional module and surprising 0/3/5/3 subgroup invariant dimensions form an independently useful exact equivariant invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
