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

Cyclotomic irreducibility over Q(zeta_(2^r)) follows from the product cyclotomic degree for coprime conductors. Hence a zero determinant gives equal grouped coefficients. Reducing at a prime above two makes all dyadic phases and permutation signs equal to one; with six terms and odd p the common parity must be zero. In the normalized exponent lists {1+ts,s,t} and {s+t,ts,1}, neither s nor t occurs in the second list. If s differs from t, the remaining single exponent of the first list cannot give both even multiplicity. If s=t, remove the two copies of t; 1+t^2 differs from 2t, t^2 and 1. The argument includes p=3 and uses no principal selection assumption. Direct rank geometry gives a separate proof: for any row pair, the three componentwise ratios are distinct, since the quotient between two ratios has a nontrivial prime-order factor and a dyadic factor. Any linear combination with both coefficients nonzero can have unit modulus in at most two of those distinct ratios (intersection of a line with the unit circle), so a third unit-modulus row in the span would have to be proportional to one of the first two, which the same ratio test excludes.

## originality

FAIL

The broader Resultary rank-two coset theorem gives the entire claim as an immediate corollary, not only the previously classified C2 case. Every two distinct rows are nonproportional on these columns: the quotient of their entry ratios between two columns is the product of a dyadic root and a nontrivial p-th root. The dual argument prevents proportional columns. Both coset counts are therefore three, so the broader theorem forces rank three. The displayed date of that broader record is later; this is verified coverage, not a determination of earlier publication priority.

## value

FAIL

Nonprincipal Fourier rank is a meaningful structural problem, but the specific three-by-three assertion is now mechanically implied by the broader rank-two rigidity theorem; the dyadic hypothesis itself is stronger than the coprimality needed for the proportionality test. The proof technique supplies a correct alternate derivation, not a remaining new invariant or consequence worth repairing into a separate claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
