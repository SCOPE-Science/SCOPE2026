---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The normalization computation is reconstructed: the exponent semigroup omits only the linear v monomial, hence R=C⊕Cu⊕(u,v)^2, B=C[u,v], and conductor (u,v^2). Every R automorphism extends uniquely to B, preserves the conductor radical (u,v), and its first coordinate has no linear v term. Conversely a polynomial plane automorphism fixing 0 with a lower-triangular invertible derivative preserves R and its inverse preserves R, proving the exact group rather than merely a subgroup. The differential map splits by linear automorphisms; conjugation by scalar dilation gives polynomial families to their first jets and the connected Borel supplies connectedness. The allowed u→u+v² shear moves any punctured v-axis point off the axis, proving two orbits. The pinned verify.py was inspected: it symbolically checks the presentation/monomials and concrete automorphisms, not the infinite automorphism theorem. Independently checked all semigroup exponents in 0..12 except (0,1); the unbounded classification follows from the above arguments, not this finite check.

## originality

PASS

Best-of-knowledge original full first-jet stabilizer classification for Selin's exact nonnormal toric surface. Selin 2026 supplies the explicit example and failure of generation by torus and roots but the accessible abstract does not state the complete stabilizer; the unaccessed complete paper leaves material priority risk. General normalization/toric automorphism papers may contain overlapping lemmas; standard conductor and two-orbit consequences are not claimed new.

## value

PASS

A complete full automorphism group of a natural explicit counterexample resolves the distinction between torus/root-generated transformations and all automorphisms; it supplies the entire infinite-dimensional group, split first-jet quotient, and an intrinsic lift criterion. This is motivated structural information, not only an orbit count or a coordinate renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
