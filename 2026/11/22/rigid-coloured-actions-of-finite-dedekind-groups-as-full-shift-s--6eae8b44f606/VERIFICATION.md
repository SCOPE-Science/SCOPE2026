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

The equivariant profile preserves colours by evaluation at the identity, and every coloured G-automorphism fixes profiles. On Gx with stabilizer H, the right-period subgroup K of the profile contains H; normality of H makes right multiplication on G/H by b in K well-defined, giving a coloured orbit automorphism moving x if b is outside H. Thus rigidity forces H=K. Equal profiles on one orbit then come from the same point; across two orbits they give equal point stabilizers and a coloured orbit isomorphism, hence a forbidden swap. Conversely every invariant subset with evaluation colouring has identity profile. Its union-of-orbits description gives the product, unique full-shift maximum, complement symmetry, and n! labellings because all automorphisms are trivial. Words fixed by H are constant on the sets gH (left cosets in standard terminology; left and right cosets coincide here), so Möbius inversion gives the stated exact counts; all conjugates of H are H, so division by [G:H] counts orbits. The q=1 and empty-object cases also work. Direct bounded reproducers for the two order-four examples gave orbit multiplicities (2,1,3) and (2,3,2) at sizes 1,2,4. The non-Dedekind example is valid: S3 on three points has trivial centralizer, and its extra fixed point cannot be swapped with that orbit.

## originality

PASS

Credit the standard cofree construction, subgroup inversion and cyclic primitive-necklace rigidity. The checked predecessors cover those ingredients or the cyclic case, not the profile as a complete invariant for all rigid named-colour actions of each finite Dedekind group, with every invariant subset realized and a unique maximum. The subgroup count is not judged new on its own. The originality judgment is for the all-Dedekind equivalence and its resulting exact rigid census.

## value

PASS

The meaningful gain is a single canonical host classifying all rigid coloured actions of a fixed group, not a new orbit-counting identity. It supplies exact counts at every size and a sharp unique capacity; the two order-four examples show that the polynomial detects subgroup distinctions missed by the maximum alone, and the S3 example shows why the classification needs a group hypothesis. The cyclic cases and each individual counting tool are standard, but their Dedekind synthesis gives an explicit invariant for the broader natural class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
