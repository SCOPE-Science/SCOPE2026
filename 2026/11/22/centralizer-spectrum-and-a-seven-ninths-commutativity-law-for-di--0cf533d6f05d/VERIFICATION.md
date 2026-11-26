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

The induction c a_W c=a_W c combines with a_i c a_i=a_i c to produce a_S or a_U c a_V with disjoint U,V. Sending all leaves but one to 1 preserves the relations. The five transformations 1,a,c,ac,ca check the two-letter quotient, and the resulting projection tuple is injective since it recovers the normal-form type and all leaf states (m≥1). The image is the union of the two full cubes {1,a}^m and {c,ac,ca}^m. On one coordinate the leaf–leaf block has four ordered commuting pairs, either mixed block has four, and the hub–hub block has seven (only c and ca fail to commute with each other). The row counts in these blocks produce the two centralizer sizes for each element and sum to 7^m+3·4^m. Only 1 and the full-leaf form followed by c use entirely universal rows in their respective blocks. Division by (2^m+3^m)^2 gives the equivalent (7/9)^m. The source checker and its stored finite m=1,…,5 outputs were inspected, not replayed; the proof is valid at arbitrary positive m.

## originality

PASS

The size, normal-form shape, and commutation test restricted to idempotents have prior coverage and are not credited as new. The supported distinct result is the element-wise centralizer spectrum and resulting all-element commuting law for the Hecke–Kiselman star. The strongest different record gives a nearly parallel formula for a star left regular band but different hub centralizers, while the closest same-monoid prior record analyzes only idempotent commutation for its endomorphism calculation. Deriving the full spectrum needs identifying the faithful coordinate model and evaluating the local non-idempotent commutation block, not substituting m into those results.

## value

PASS

For a canonical noncommutative graph family, the full centralizer invariant and asymptotic describe all elements rather than the idempotent subfamily. The two-cube representation accounts for the growth constant and explains why an equally large star dependence band has different commutation statistics. The exact count and spectrum are individually useful without extending to mixed orientations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
