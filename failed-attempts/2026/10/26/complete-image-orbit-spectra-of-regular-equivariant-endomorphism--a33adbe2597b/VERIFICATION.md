---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For an equivariant map f, the relation fgf=f is equivalent to having an equivariant section on the image: restrict g to the image in one direction, and extend a section by identity on orbits outside the image in the other. On a transitive image orbit the section must be an isomorphism onto a source orbit, so an equal-stabilizer source orbit is necessary and sufficient. For an abelian group, the image of a chosen representative of G/H can be any of the w_K points in each admissible G/K (H contained in K). After choosing the target orbits, the selected targets of type H must all be hit by sources of type H. Excluding specified same-type targets removes w_H choices per target, while strict-supergroup choices stay available. This gives the displayed inclusion–exclusion factor independently for each source type and leaves no unselected orbit in the image. The empty set gives 1, the trivial group specializes to counting ordinary transformations by image size, and profiles with no available target for a nonempty source type give zero. For C_p, condition on the r fixed targets hit by fixed sources: all free targets have only free antecedents, so there are (r+pb)^b unrestricted choices within those r fixed targets and the b free targets. Dividing by the total and using b log((r+pb)/(a+pb)) -> (r-a)/p yields the claimed limit, including the stated example. The bundled checker was inspected, not executed; its recorded four cases (3,253 maps; 1,793 regular) are corroboration only. The proof independently establishes the claim.

## originality

FAIL

A distinct indexed record gives the exact census summand by stabilizer profile for arbitrary finite groups. The abelian product here is that summand with the abelian table of marks and a reversed inclusion–exclusion index. The indexed work also proves that each summand counts the fixed profile, so the use of separate formal variables here does not avoid coverage. The recorded dates do not establish historical priority or dependence. The C_p total and limit are an explicit specialization and an elementary limiting calculation; they do not make the frozen central enumeration a distinct result.

## value

PASS

The complete profile census is a meaningful invariant of equivariant monoids: it distinguishes regular strata with the same cardinality of the image but different stabilizer types, and yields both rank distributions and regularity proportions. That mathematical use is separate from whether the frozen version is distinct from the broader indexed census. The prime-cyclic example illustrates the distribution but does not rescue the overlapping central claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
