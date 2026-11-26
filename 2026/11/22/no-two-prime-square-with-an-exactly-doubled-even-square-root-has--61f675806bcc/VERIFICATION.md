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

Reconstructed the divisor argument, including repeated summands and the unit-divisor issue in descent. For any odd q the positive differences for 1<d<2q^b are from the three divisor classes q^j (1≤j≤b), 2q^j and 4q^j (0≤j<b); the upper bound in the last class uses 4/q<2. The only differences not divisible by q are B=2M−2 and C=M−4, M=q^(2b). The strictly largest difference is B. A single exceptional occurrence fails modulo q; if both B,C occur once the only possible placement is B=C+D, which fails since B−C=M+2 is not divisible by q. Two copies of C must sum to the other exceptional value (2C≡−8≠0 mod q), but B−2C=6; B cannot be a summand. Therefore all factors and complements in the triple are divisible by q and division gives the same relation scaled to 4q^(2b−2). If the least new divisor is 1, its difference is n'−1 and every summand at a divisor ≥2 is ≤n'/2−2, so even their sum is <n'−1. Otherwise descent contradicts minimal exponent (n'=4 at b=1 has no allowed divisor). This independently validates the proof's exceptional case and in fact gives a self-contained proof for all odd q. For q=2 the cited prime-power exclusion applies; alternatively all factors and complements are even, so iterating the same division by 2 gives an impossible unit case or an empty allowed divisor interval.

## originality

PASS

Credit only the missing infinite subfamily 4·3^(2b) for b≥2 and the resulting complete ray classification. The other primes and b=1 are already covered by the explicitly cited results; they are not original claims. Neither the dominating-prime criterion nor the later positive Pell family yields the exceptional negative classification.

## value

PASS

The missing case is the single odd prime outside dominance when the root contains exactly one factor of two. Filling it requires excluding an infinite ray, not checking small squares. The modular pair isolation and unit-safe descent explain why the natural dominance threshold need not hold in this boundary case and give a clean exclusion for future classification by prime support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
