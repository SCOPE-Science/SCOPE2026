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

Code a vertex outside a pointwise named base by its binary adjacency vector; every vector occurs infinitely often, and each vector class is an orbit for graph automorphisms fixing the base. On a finite tuple the allowed edge changes are s_i+s_j+c over F2. Finite switches are realized by composing conjugates of a singleton switch, and complementation is realized by a complementing permutation; homogeneity then takes the transformed tuple to the target, so the composite fixes the base. A named pair excludes a pure complement, while three named vertices exclude any nonzero complement bit by summing the triangle equations. With switching only, the base bits are constant, and switching the new vertex gives the all-ones translation. With both operations and two named vertices, c=s_1+s_2 gives every translation on the two outside-edge bits. These cases give the stated table including the empty base; all outside orbits are infinite, and the m named points are the only algebraic types. It is the prefix through size three, not the single size-three row, that separates the groups. The archived bounded enumeration is consistent with, but not a substitute for, this argument.

## originality

FAIL

A distinct indexed result gives the full named-base injective tuple spectrum. Its arity-one specialization reproduces all the frozen formulas, including the small-base exceptions; the sharp size-three prefix follows by comparing the first four rows. It also states stronger stabilizer-tail identities. This is coverage, not evidence that the distinct later-dated entry preceded or was independent of the frozen record.

## value

PASS

The sharp named-base prefix measures precisely what can and cannot be reconstructed from the simplest type statistics. The two permanent tail collisions show why large base sizes alone are insufficient. This is a meaningful limitation on a natural reduct invariant, apart from whether this record contributes it distinctly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
