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

Writing A=S^s on a row, the companion matrix gives M^3-I=(A+I)C, with commuting polynomial entries and det C=A. Thus the kernel at time 3·2^j is exactly the joint kernel of A^(2^j)-I; no smaller kernel is hidden in C. In the cyclic group algebra z^n-1=(z-1)^n, reduction at z=1 gives the order-three two-dimensional matrix with no fixed nonzero vector for exponents not divisible by three. Invertibility lifts modulo the nilpotent ideal. Since A has order L, M^(3L)=I. These facts prove the pointwise first returns and all-time fixed counts. Taking consecutive differences of the paired coordinate-cycle counts gives the census, including the zero state, n=1, and s≡0; for L>1 the two largest fixed-space dimensions are 2n and n. I independently enumerated six F4 cases with n=1,2,4 including negative strides and nonzero multiples of n; at n=4,s=-3 the counts at 1,3,6,12 were 1,15,240,65280. This was an additive two-bit reproduction, not an execution of the frozen checker or an all-length certificate.

## originality

PASS

The checked results cover entropy, matrix representations, or complete orbit statistics for materially different update operators. None of the inspected statements gives or implies the directed monomial rule's pointwise joint spatial-to-temporal period law. This is a judgment on the specified claim, not priority certification.

## value

PASS

For the natural directed single-neighbor reversible update, knowing a global order alone does not identify which initial configurations run on each clock. The fixed-space identity gives a statewise criterion with a spatial interpretation, then determines the full finite ring census without simulating long orbits. This also explains the exact stride-independent maximal-period proportion for every nonidentity spatial stride. The value is this structural identification and resulting complete census, not the standard matrix encoding or merely dividing counts by period.

The dated certificate retains the supplied scientific assessment, sources and limitations.
