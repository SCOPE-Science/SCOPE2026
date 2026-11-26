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

The generator equations force rectangular domains and ranges; the induced maps on image and quotient factors are isomorphisms, so intersections and pullbacks preserve rectangularity under composition. A rectangle with q matrices is exactly a rank-one line. The source proof's assertion about uniqueness of a semigroup isomorphism of idempotent lines needs the qualifier F_q-linear (abstract multiplicative automorphisms can occur); linearity has already been proved for every element of this monoid, and suffices. For an idempotent or square-zero line, respectively use a projection or I plus one nilpotent Jordan block with the prescribed kernel and image to obtain its identity. Conjugation then gives the unique linear idempotent-line arrow and every nonzero scalar arrow for square-zero lines. Products match middle lines or restrict to {0}, so these are orthogonal Brandt ideals. Every nonzero map can be restricted to a line in its rectangular domain, proving exhaustiveness of the minimal ideals. Full-domain factors are conjugations, with scalar kernel, and a rank-two projection gives a q⁴ domain strictly between the line and full cases. The hyperplane counts give E_n and Z_n and the order formula. Separate enumeration verified 28 and 21 lines and 1225 line arrows for (q,n)=(2,3), hence order 1394; the (3,3) formula gives 24714.

## originality

FAIL

I did not find the exact n≥3 Brandt statement in the originating paper. But the earlier exact semilattice classification --c72f4e192073 for this same monoid gives every proper nonzero rectangle and its identity, and the two line types. The entire line sector is a direct consequence: apply domain and range idempotents, linearity, and ordinary rank-one conjugation. The two minimal ideals, scalar labels and polynomial counts then follow from line intersection and elementary hyperplane counts. This is prior implication, not a claim that the same formula is printed in the reference, nor an inference from the date of a same-day record.

## value

FAIL

The minimal ideals are naturally motivated by the vector-space problem, and the formula usefully spells out their size. But after the prior complete semilattice result, the remaining specialization is a routine application of linearity, rank-one conjugacy and hyperplane counts. The assembled submonoid excludes higher rectangular domains and does not resolve a further structural or enumerative gap beyond that direct consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
