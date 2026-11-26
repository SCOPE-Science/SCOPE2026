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

Taking matrix powers and multiplying gives the stated linear relation in the three upper-right entries. The Laurent monomial substitution with s=lambda mu identifies the diagonal base with a split rank-two torus and has the stated inverse. Each rational fiber has Q^2 points unless its three coefficients vanish, when it has Q^3. A direct scheme check over any allowed base field writes the exceptional set as a product of primitive fourth roots, sixth roots other than ±1, and n-th roots other than 1: in the third factor use eta=(-mu^3)nu, so eta^n=1 and the excluded eta=1 corresponds exactly to the matching root ±1 of nu^n=-mu^3. These Kummer factors are finite étale, proving the geometric length 2*4*(n-1)=16m. The first two factors have 2 and 4 rational points simultaneously exactly for Q=1 mod 12; the third has gcd(n,Q-1)-1. Summation in the defining zeta series gives the displayed quotient, and rationality of the roots over the extension of degree ord_M(q) implies the stated finite Möbius product. Independently enumerating the polynomial roots and testing the diagonal relation for n=5 gave 0 exceptions over F_7, F_49, F_11 and F_13 and 32 over F_121; the degree-two fields used X^2-3 over F_7 and X^2-2 over F_11, respectively. The finite calculations corroborate rather than prove the formula.

## originality

PASS

Pass is restricted to the explicitly quantified good-characteristic finite-field formula as a statement. The geometric equations, fiber stratification, and exceptional-root description are already present in Liriano. No inspected primary theorem or distinct catalogue record states a finite-field or uniform arithmetic version that already contains the formula. The small amount of deduction needed from the known geometric description is evaluated separately under value.

## value

FAIL

Finite-field zeta is a natural invariant and the formula is correct, but here its determination is a routine cyclic-group recount of the exact coefficient and root equations already analyzed in Liriano's Lemma 7, not a substantive new arithmetic computation. The existing proof supplies not only the length but every exceptional condition: primitive fourth roots for lambda, sixth roots other than ±1 for mu, and roots of nu^n=-mu^3 excluding the unique sign root. Over the allowed fields the very same integral equations give 2 or 0, 4 or 0, and gcd(n,Q-1)-1 respectively, by elementary cyclicity. The split torus and rank jump are already explicit; substituting the standard sizes of affine spaces gives the entire point count, and its zeta expression and finite product then apply the defining exponential and standard Möbius inversion. No new arithmetic structure or exceptional phenomenon beyond this mechanical replacement of complex root counts is established. Failure is on scientific value, not falsehood or proven earlier publication of the finite-field formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
