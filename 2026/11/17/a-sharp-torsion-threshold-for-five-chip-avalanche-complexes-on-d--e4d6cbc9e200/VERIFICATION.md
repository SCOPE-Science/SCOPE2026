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

PASS: A binary state on the outdegree-one directed n-cycle shifts exactly to S+t under every parallel firing step, so avalanche faces are the downward closure of all n cyclic translates. Dihedral support orbit reduction is mathematically valid (reflection induces an abstract simplicial isomorphism even though it reverses directed arrows). Independently implemented all-support canonicalization across 3<=n<=15,1<=k<=min(5,n), free face/coface elementary collapse, integer simplicial boundary matrices and SymPy Smith normal forms. This separate full 747-dihedral-class computation completed and reproduced exactly 111 classes at n=15,k=5, 14 exceptional supports all there, all first-homology torsion (Z/2)^2 and none in other degrees. Four cases have (rank H1,rank H2)=(1,0), ten have (2,1), all other configurations torsion-free. Torsion of H_{j-1} equals torsion of coker d_j because im d_{j-1} is a free subgroup and the quotient extension splits. The claimed length fifteen and five-chip threshold is confined to the EXHAUSTED finite domain; no extrapolation for n>15.

## originality

PASS

PASS best of knowledge, with genuinely read exact-object comparators and explicitly bounded coverage risks. Selected consecutive/3-chip cyclic theorems and unrestricted directed-tree realization show neither a five-chip threshold nor the exact 14 binary directed-cycle supports. The 747-class integral Smith census supplies additional nonimplied data.

## value

PASS

PASS: Integral torsion is a topologically meaningful obstruction to wedge-of-spheres descriptions. Enumerating a natural finite sparse binary cyclic sandpile family exhaustively through the first 5-chip torsion boundary, identifying all 14 exceptional dihedral classes and exact free/torsion ranks, is a motivated independently useful finite classification, notwithstanding lack of an all-n theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
