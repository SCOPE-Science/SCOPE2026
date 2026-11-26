---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Bochvar representation identifies the canonical fibers with intervals below strictly descending supports S_i of the first finite Boolean algebra P([k]). In these coordinates the transition maps are restrictions: each p_0j kills the complement of S_j and is the stated interval isomorphism on S_j, and compatibility and surjectivity determine the later transition maps. The quotient intervals have sizes 2^{|S_i|}, and disjointness gives a binary expansion with no repeated powers. Nested initial segments with the indicated lengths satisfy the converse representation, including the trivial first fiber for N=1 and a terminal zero support when the final exponent is zero. Equal-length flags are conjugate by an atom permutation matching successive differences. A finite chain has no nontrivial order automorphism; every algebra automorphism fixes each support and is determined by its first-fiber permutation, since J₂ is injective on each fiber. The equivariant restriction maps and external operations give the converse. The stabilizer is the independent product of the layer permutation groups. Its factors are trivial exactly when the exponents are consecutive ending in 0 or 1, which gives the two stated sets of rigid sizes. The generating functions follow by choosing the lower bits freely. The bundled verify.py was inspected, not executed; it is a bounded flag, stabilizer and axiom check rather than a proof for all finite ranks.

## originality

FAIL

The binary formulas are correct but mechanically implied by the prior categorical classification of Bochvar algebras by Boolean algebras with a designated meet-subsemilattice. On the chain subclass that theorem already classifies the objects and isomorphisms as Boolean flags and flag-preserving atom permutations, with explicitly given quotient fibers. Taking the sizes of those quotients and the symmetric groups of the disjoint layers yields the exact formulas. No new restriction on the flags or their symmetries is needed. This does not assert that the earlier authors printed the formulas verbatim.

## value

PASS

As a mathematical description, this is a complete, usable normal form for a natural finite subclass. It constructs a representative, gives its full symmetry group, and recognizes rigidity directly from size. The scientific utility is in that classification, not in the routine generating functions or in any claim of novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
