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

Reconstructed the geometric quotient model: barycentric vertices are nonempty independent sets and flag cardinalities strictly increase. An orbit identification within a closed flag simplex preserves each barycentric coordinate indexed by cardinality, so the simplex embeds in the quotient and its different codimension-one faces have distinct omitted cardinalities. Thus orbit deletions with sign (−1)^i give the integral cellular differential with no stabilizer weight, and a flag facet with a unique current codimension-one coface gives a legal free-face collapse. An independently implemented exact enumeration, without executing supplied scripts, reproduced the complete range: n=6–11 and 13–15 collapse to a point; n=12 has dimension two and one free H₂; n=16 has dimension three and one free H₃; n=17–19 have dimension three and two free H₃ classes with no torsion. At n=20 it reproduced initial counts (74,926,3717,6267,4662,1260), ∂²=0, 7,194 legal collapses to counts (36,297,851,962,372,0), unit ranks (35,262,589,371) and one further ∂₄ Smith factor 2. In the independent pivot order the last ∂₄ column had 96 nonzero coefficients of absolute value 2; gcd reduction by unimodular row operations, not modular rank alone, makes this a single Smith entry. The kernel of ∂₃ is saturated in C₃, so the nonzero Smith data in C₃ and in ker ∂₃ coincide. This yields H₃=ℤ⊕ℤ/2, H₄=0 and no other reduced homology at twenty. The independent triangular presentations reduced to the trivial group in all required noncontractible cases (262 eliminated generators at twenty). There is also a direct check of simple connectivity: the quotient of the original one-skeleton is a star, since all vertices lie in one orbit and every independent edge {i,j} is flipped by x↦i+j−x. Passing through the original higher skeleta attaches, for each simplex orbit, a cone on its boundary modulo its setwise stabilizer (radial contraction to the barycenter); for dimension at least two that boundary quotient is connected, so the attachment creates no π₁. Hurewicz and simply connected homological Whitehead give the stated sphere cases. At twenty, the collapsed three-skeleton is 2-connected and equivalent to a wedge of S³; its four-cell attaching maps are specified by their integer degrees, since π₃≅H₃. Basis changes of the sphere wedges implement Smith reduction up to homotopy. The degree-one cells cancel, the degree-two cell gives M(ℤ/2,3), and one free S³ remains. The frozen replay entry point is code/verify.py, with ranges 6 15, 16 19, 20 20, and mod20. This is an exact finite audit, not proof-assistant verification or a conclusion past twenty.

## originality

PASS

Best-of-knowledge pass for the bounded full-dihedral integral homotopy classification and the first Moore summand. This is not a new claim about the unquotiented homotopy recurrence, the rational Euler invariant, or total cut complexes.

## value

PASS

Full polygon symmetry and distance-three exclusion define a natural orbit-space family. The cutoff at n=20 exhausts the nondegenerate sizes of independence-complex dimension at most five, since the maximum independent-set cardinality is floor(n/3) by cyclic spacing and an attaining spaced set. Locating and identifying the first integral torsion by a Moore attachment distinguishes spaces with the same rational invariants. The exhaustive earlier sphere and contractibility classifications make the precise finite boundary a useful benchmark for later equivariant computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
