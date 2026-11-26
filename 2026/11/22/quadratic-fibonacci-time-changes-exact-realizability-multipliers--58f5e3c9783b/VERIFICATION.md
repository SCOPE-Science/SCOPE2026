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

For the integral Fibonacci matrix Q, reduction at p≠5 gives Q^p=Q in the split classes and Q^p=−Q⁻¹ in the inert classes (at 2 directly), with Q^(p²)=Q in both. Taking the upper-right entry, the Fibonacci–Lucas addition identity gives the inert defect −F_b L_(a+c), including when a−b+c is negative because Q is invertible over the integers. If b≥1 this is a fixed nonzero integer, so any fixed multiplier still fails the prime Dold condition at all but finitely many inert primes, a set of relative prime density 1/2 by the prime number theorem in arithmetic progressions. For b=0, the argument differences at mp^k and mp^(k−1) are multiples of p^(k−1)(p²−1) at p≠5. At 5, the period 20 modulo 5 lifts to a period 20·5^(k−1) modulo 5^k; the difference 24am²5^(2k−2) suffices except possibly at k=1, where 5|a works unscaled and multiplication by 5 always works. The nilpotent part of Q at the repeated root 3 gives F_(25a+c)−F_(a+c)≡−a·3^(a+c−1) modulo 5, so the multiplier 5 is forced if 5∤a. Grouping the Möbius sum in prime-power pairs establishes divisibility. Positivity follows separately: the proper-divisor terms are bounded by (n−1)F_(a⌊n/2⌋²+c), strictly less than F_(an²+c) by the addition formula for n≥3; the first two indices are positive directly. Thus the scaled transform actually counts cycles. The package checker was inspected, not run; the decision uses the all-index proof, not its finite expectations.

## originality

PASS

The already-covered monomial and positive input-translation cases and general monomial Dold sufficiency are not new here. The supported distinct result is the sharp joint classification for arbitrary nonnegative quadratic coefficients with a≥1, including the leading-coefficient test at the ramified prime and the factored defect for independent linear and constant coefficients.

## value

PASS

A quadratic time change is a natural next family after monomials and translated monomials. The classification precisely separates an obstruction at almost every inert prime caused by the linear term from a single ramified-prime obstruction for the even quadratic. The least multiplier and the positive orbit counts decide actual realizability, not merely a few congruences or the existence of some unspecified multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
