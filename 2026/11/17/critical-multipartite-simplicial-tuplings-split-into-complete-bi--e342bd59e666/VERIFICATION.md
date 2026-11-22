---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For X the join of 2r nonempty discrete parts and D^r(X) defined by r-faces with disjoint union a face, a vertex support is an r-subset of the 2r color labels. Three vertices would use 3r>2r parts for r>=2 and cannot span a face. Two vertices form an edge exactly for complementary r-supports; all p_I=product_{i in I}a_i transversal vertices and p_Ic choices are adjacent, yielding one complete K_{p_I,p_Ic} per unordered complement pair. Hence c=binom(2r,r)/2 components, reduced H0 rank c-1 and H1 rank sum (p_I-1)(p_Ic-1)=c(1+prod_i a_i)-e_r(a), torsion-free. Zero-row/column-sum integral edge matrices establish canonically H1(component)=augmentation Z[U_I]^0 tensor augmentation Z[U_Ic]^0, with minus tensor swap for part permutations exchanging bipartition shores. For all a_i=2, the cross-polytope consequence follows. Independently calculated r=2 sizes (2,3,1,2) components K_(6,2), K_(2,6), K_(4,3), H1 rank 16 by both formulas; finite cases do not establish the all-r claim.

## originality

PASS

Lesh–Schreiner–Wahl define simplicial tupling and give general connectivity work; the published 2r+1-color character theorem yields a connected graph for ODD part count and a rational symmetry character but not the even 2r complement-pair split. The prior cross-polytope double result explicitly includes r=2, four-part 3 K_(4,4) components, which are excluded from the novelty comparison. The submitted full r>=2, arbitrary part-size even-part decomposition and integral augmentation lattice with shore-swap sign are not dominated by those specific prior results.

## value

PASS

It is a natural exact boundary classification at the critical 2r parts, immediately adjacent to connectedness at 2r+1. It gives the exact graph components, all integral homology, weighted elementary-symmetric rank, and natural equivariant integral lattice for arbitrarily many colors; future homotopy/representation work can use the precise boundary structure. The known r=2 special case is not the full family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
