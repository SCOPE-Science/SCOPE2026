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

The coset parity agrees across the two bracketings. For outside parity, (l u)^(-1)(r u)=r^(-1)l, since outside elements are involutions; for even parity use l^(-1)r. Recomputing the bracketings with the four given rules produces the displayed table. For example, at 111 the base elements are k h^(-1)g and g h^(-1)k; taking their quotient in the outside-coset order gives k^(-1)h g^(-1)k h^(-1)g, equal to the stated h-conjugate. At 011 the even bracketings are k^(-1)h g and g k^(-1)h, giving [g,k^(-1)h]. Across the seven sectors the pair changes have one free variable and the 111 conjugation preserves fibers. The 000 contribution is concentrated at 1 and the total is 8m^3. For odd dihedral n, the three sectors of group pairs involving at least one reflection each hit any given rotation n times, since doubling the relevant label or label difference is invertible modulo n; rotation pairs contribute n^2 at 1 alone. The boxed values follow with m=2n. Read RESULT.md, VERIFICATION.md and verify_associators.py; the supplied finite enumerator was inspected, not executed, and is not used for the proof.

## originality

FAIL

A distinct indexed Resultary result proves the same all-target finite-group law, even sector by sector, using an equivalent associator convention. This is demonstrated statement-level coverage, not a claim that one record has historical priority over the other. The odd-dihedral values and inversion of the mixture are mechanical consequences of the covered general law; neither is a separate surviving original contribution.

## value

FAIL

An arbitrary-group associator/commutator distribution identity is mathematically natural, but the frozen statement contributes no separate useful invariant beyond the equivalent complete census. The inverse-and-reverse correspondence is a convention change, distribution recovery is algebraic inversion of the mixture, and the odd-dihedral evaluation uses only its substitution with elementary doubling modulo n. No valuable distinct remainder warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
