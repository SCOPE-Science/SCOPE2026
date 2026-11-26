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

By the defining relations, a rotation image of a gives either a central map or a coset-type pair (u,v) with u odd. If the image of a is outside the rotation subgroup it has order four, so odd m is impossible; for 4|m the image of b would square to one and could not invert it. For m=2h with h odd there are exactly four choices of image of b for each outside image of a, generating Q8. For m≥3 automorphisms preserve the unique cyclic subgroup of order 2m. On coset maps the action sends v to rv+(1−u)s at fixed u. Translations reduce this to units acting modulo d=gcd(u−1,2m), giving the stated gcd labels and orbit sizes. On the quaternion-type fiber with a↦b, the stabilizer has s=0 or m according to r≡1 or 3 mod 4. For r≡3 the precomposition contributes the extra central factor a^m to the new image of b; this cancels the rotation swaps and exchanges the two coset choices. Thus two fixed choices and one pair yield sizes 2m,2m,4m. Central maps give the stated parity-dependent orbits. For m=2 a proper image is abelian and the domain abelianization has exponent two, ruling out order four; the three nonzero central characters are transitive and the 24 automorphisms give the five S4 classes. Interchanging the gcd-divisor sum with the sum over odd u gives the arithmetic total.

## originality

PASS

Inspected prior results establish adjacent counts, group/semigroup structure or restricted notions of maps, not the uniform image-order refinement of automorphism conjugacy on all endomorphisms. Credit the known unrefined quaternion counts; the contribution includes the non-cyclic-subgroup-preserving endomorphisms and their three orbits, not just the Q8 coefficient or the affine automorphism parametrization.

## value

PASS

The uniform classification distinguishes maps of the same image order even when image-subgroup data or raw endomorphism counts cannot. It gives a complete exact invariant on a standard nonabelian family and explains precisely where quaternion-image maps escaping the characteristic cyclic subgroup occur, how the orbits split, and why Q8 requires separate treatment. These are useful classification facts beyond a small-group enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
