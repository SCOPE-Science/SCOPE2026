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

The dissection is supported by da Silva–Sellers arXiv:2606.17440v1 §4 Eq. (18) and their Jacobi identity (14): the former gives 2 f_2^3 f_3^3 modulo 4, and in the latter all weights (-1)^j(2j+1) are odd. The Jacobi indices must begin at zero, as stated in the frozen result: the following displays in the accessible preprint render lower limits 1, inconsistent already at the constant term 2. This issue does not affect the derivation from (18) and (14); the frozen citation label (4.2) is not the arXiv label and was not checked in the journal version. Completing squares gives m=2(2j+1)^2+3(2k+1)^2. The maximal order of Q(sqrt(-6)) has discriminant -24 and units ±1. Its Minkowski bound is below 4; norm-2 and norm-3 ramified ideals are nonprincipal (2 and 3 are not principal norms) and their product is (sqrt(-6)), so the class number is exactly 2. For the principal class each ideal of norm m yields two signed generators for x^2+6y^2=m. For the other class multiply by J=(2,sqrt(-6)), of norm 2 and self-inverse class: the generator is in J and is of the form 2x+y sqrt(-6), so its norm divided by 2 is 2x^2+3y^2. Conversely (2x+y sqrt(-6))J^(-1) is integral. This confirms the factor of two even at ramified divisors. Modulo 8 at m=5, the principal form never represents, and both coordinates in the other form must be odd; hence the positive-pair count R obeys 4R=2a(m) for the ideal count. Local ideal factors are 1 for a ramified prime, e+1 for split, and 1 or 0 for even or odd inert exponent. They yield the divisor sum and identify residue 2 with exactly one split exponent 1 mod 4, no other odd exponents except at 3, and the stated class 5 or 7 mod 24 as selected by m=5 mod 8. All other values are zero modulo 4 by the evenness already proved. For the asymptotic use Y=8X+5, and for h=0 sum primes <=Y/(3^a s^2) in one reduced class mod 24, with (s,6)=1. Removing p|s overcounts by O(sqrt(Y)) since s=pt gives the convergent weight sum of 3^(-a/2)p^(-3/2). The h>=1 count is also O(sqrt(Y)) by summing 3^(-a/2)p^(-(4h+1)/2). For 3^a s^2<=sqrt(Y), the prime-count upper bound gives summable majorant 1/(3^a s^2) after normalization by Y/log Y; the other range contributes at most Y times the reciprocal-weight tail, O(Y^(3/4)) by splitting the a-sum at 3^a=sqrt(Y) and bounding the s^-2 tails. The fixed-class prime number theorem therefore gives Y/(8 log Y) times (3/2)(1-1/4)(1-1/9)zeta(2)=Y zeta(2)/(8 log Y). This converts to the stated X scale. Replay: frozen RESULT.md lines 23–56 and the preprint's Eqs. (14),(18). An independent finite check using the Euler-product logarithmic derivative, with b*d(b)=sum_{j=1}^b d(b-j) sum_{k|j, k allowed} k, agreed with the character sum for 0<=n<=134. The supplied check.py was inspected, not executed; finite agreement does not establish the general congruence or asymptotic.

## originality

PASS

Da Silva–Sellers supply the same progression's theta dissection and explicit zero congruences, but the inspected preprint does not yet identify the full zero-versus-two fiber or count it. The supported novel content is the arithmetic classification via the -24 norm forms and the exceptional-index asymptotic, not the dissection, Jacobi identity, ideal–form method, or the use of a fixed-modulus prime number theorem. Distinct partition statistics with analogous square and prime-times-square conditions were compared directly.

## value

PASS

The exact zero/two test resolves the entire progression rather than giving more isolated sufficient zero congruences. It replaces counting partitions or representations by a factorization criterion and explains why most indices are zero modulo four, with a sharp rarity scale and leading constant. The two-class ideal argument handles cancellation and multiplicity beyond the known nonrepresentation obstruction; the counting law quantifies the resulting exceptional set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
