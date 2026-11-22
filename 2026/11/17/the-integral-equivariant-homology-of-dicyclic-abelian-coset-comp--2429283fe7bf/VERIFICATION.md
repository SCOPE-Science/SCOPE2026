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

Classify all maximal abelian subgroups as A=<x> and n order-four B_i=<x^iy> meeting at the center Z=<x^n>. Their left coset cover has two A-coset apices and n² small cosets; every nonempty intersection of principal downsets has its terminal intersection coset fixed by stabilizer, so the equivariant nerve lemma applies. The nerve is a union of row and column simplices, and the explicit second-largest-barycentric-coordinate contraction fixes shared vertices, yielding a G-equivariant K_{2,n²}. Orient U/V-to-e edges: cycles are exactly sum-zero integer e-coefficients with sign reversal when G swaps U,V. Stabilizers fix n² small cosets on Z, none on A\Z, and n off A; traces follow, and edge-pair orbits collapse the quotient graph to a tree. Independent group-law/coset/stabilizer enumeration for n=2,3,4,5 reproduced these cardinalities and character cases; proof, not finite extrapolation, handles n>=2.

## originality

PASS

Antolín-Camarena et al. 2023 Theorem 5.1 previously establish the underlying n²−1-circle wedge and enumerate maximal coset graph geometry; no integral left-translation module, complete character or ordinary quotient theorem was identified in its inspected full relevant proof. The sign-twisted module is additional data, though closely prompted by that graph.

## value

PASS

The integral symmetry action on a natural family of commutativity coset complexes, its character and its nonfree ordinary orbit quotient are motivated topological invariants not specified by the known wedge rank. Gives a uniform structural G-lattice formula and action-sensitive information across all n>=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
