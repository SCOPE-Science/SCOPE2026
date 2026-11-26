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

For F(t)=t²−t+1, any solution with equal coordinates or a coordinate equal to 1 is (1,1). For 2≤a<b, put r=F(a)/b, a positive integer strictly less than a. The identity rb≡1 (mod a) and F(b)≡0 (mod a) imply b(1−b)≡1 (mod a), so r≡1−b (mod a), and F(1−b)=F(b). Therefore (r,a) obeys both divisibilities and has smaller sum. It cannot have r=1 when a>1. This confirms the unrestricted descent, including the boundary case. Grouping the defining sum by gcd gives nH(n)=∑_{d|n}dφ(d), a multiplicative numerator whose prime-power factor is (p^(2e+1)+1)/(p+1) and is 1 modulo p. This excludes every prime power in particular p and p². For distinct p,q the numerator is F(p)F(q), so integrality would force exactly the forbidden two-cycle. Together with H(1)=1 this establishes the stated squarefree consequence and prime graph assertions.

## originality

FAIL

Mills's 1953 Theorem 3 treats the exact negative-linear-sign system, within a stronger chain classification. Even without trusting the corrupted equality in extracted text, §2 and the §8 chain list imply this case: change both input signs, then any two adjacent negative terms in a 1-chain must both be −1. The reciprocal-gcd factorization is known, and the semiprime implication is just its application to that classified pair. A separate same-day indexed record explicitly states both results with the same hypotheses; its date does not determine ordering.

## value

FAIL

The exclusion is a natural question in reciprocal-gcd integrality, but the core obstruction is an already classified Diophantine system. The application from the existing multiplicative identity is immediate and independently already stated in the distinct indexed record. There is no additional case or genuinely new obstruction left to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
