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

Re-audited the complete corrected RESULT.md under repairs/2/. The main theorem survives unchanged, but the frozen example's identification with the standard integral S4-lattice did not: at n=4 the signed partition lattice has coinvariants Z/2, because there is one orbit with a block-swapping stabilizer. The standard integral root lattice has zero coinvariants, since all e_i−e_j are conjugate and the relation (e_1−e_2)+(e_2−e_3)=e_1−e_3 kills their common class. The repair makes the standard-representation identification only after rationalization, and does not infer integral quotient homology from coinvariants. For the theorem, a full no-singleton partition is a maximal simplex so its oriented coefficient kills boundaries. The signed cross-polytope cycle obtained by replacing each block alternatively with a singleton has unit coefficient on its designated facet and none on the others. With Gottstein's exact integral rank and freeness, the coefficient map is an isomorphism. Independently, filter the augmented chains by the number of nonsingleton blocks: for fixed such blocks the associated graded is the augmented simplex on the unused labels up to shift and signs, hence acyclic unless all labels are used. On the latter summands the facet coefficient map induces the identity, proving that it is a quasi-isomorphism. Stabilizers permute repeated-size blocks with sign and act trivially within blocks. Subdivided orbit chains over Q are coinvariants; averaging is exact, and signed stabilizer lines contribute one invariant exactly for pairwise distinct sizes. Their least possible sum is j(j+3)/2; increasing just the largest realizes every greater sum. This verifies the stated series and first degree-two class at n=9.

## originality

PASS

For the repaired claim, Gottstein's same-complex nonequivariant homology and automorphism theorems are substantial known inputs, fully credited. They allow the refinement to be derived but do not themselves identify the homology action or the orbit-space ranks. The supported distinct contribution is the canonical oriented-facet description over Z, which avoids choosing an equivariant set of block representatives, and the full strict-partition rational orbit-space formula. The repaired example distinguishes rational representation from integral lattice rather than claiming a new rational character computation independently of the theorem.

## value

PASS

The full label action on a natural partial-partition complex is a meaningful invariant not specified by ordinary Betti numbers. The result gives integral stabilizer signs and thus identifies actual surviving rational orbit classes and the exact sharp dimension threshold, rather than just counting permutations of homology generators. The repaired example illustrates why rational character data cannot be used to identify an integral lattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
