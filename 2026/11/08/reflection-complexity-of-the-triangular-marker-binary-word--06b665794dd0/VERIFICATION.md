---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the exact one-sided word 1 0^1 1 0^2 1... the all-zero factor is unique and the one-one words occur in every placement. Two-one factors have unique form 0^a 1 0^j 1 0^b with 0<=a<=j-1 and 0<=b<=j+1. Factors with at least three ones are uniquely indexed by initial zero count and first increasing internal gap; no such factor has its reverse in the language. Nonpalindromic reversal pair series are z²/((1-z)(1-z²)) for one one and z⁵/((1-z)(1-z²)(1-z³)) for two ones. Subtracting from P(z)=1+z(2-z-z²+z³)/((1-z)^3(1+z)) yields the claimed R(z) with denominator (1-z)^3(1+z)(1+z+z²), noncancelled roots of orders 2,3 and least quasipolynomial period 6, coefficients c=(1,2,2,4,5,7). P(n)=floor((n+1)^2/4)+1 and R/P→2/3. Own direct factor check at n<=45 corroborates but does not establish the all-length classification.

## originality

PASS

Best-of-knowledge originality after comparing statements, direct implications and inspected primary source material.

## value

PASS

Reflection complexity is a natural extension of word-factor complexity to reversal classes. An exact full spectrum on the triangular-number indicator yields a nontrivial least-period-six quadratic quasipolynomial and a structural obstruction to reversible factors with >=3 ones, relevant to sparse nonrecurrent languages. It is neither a trivial sequence lookup nor a known-table coefficient extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
