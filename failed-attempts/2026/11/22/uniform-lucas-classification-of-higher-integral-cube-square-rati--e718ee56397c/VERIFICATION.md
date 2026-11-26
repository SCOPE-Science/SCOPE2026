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

Centering the terms at x=a+n−1 gives S=nx and C=nx(x²+n²−1), by the vanishing of odd centered powers and the centered second moment n(n²−1)/3. If the ratio is integral, x divides n²−1, so even n is impossible since x has the same parity as n. For odd n the integer quotient is odd. For k≥5, the ratio equation is x²−knx+n²=1, with x≥n. A second proof of the descent is to replace (n,x) by (kn−x,n): the smaller coordinate (n²−1)/x is a positive integer strictly below n for n≥2 and preserves the equation. The terminal pair is (1,k); the inverse move gives (U_j,U_(j+1)) for every j≥1 and proves exhaustion and uniqueness. Thus a=(k−1)U_j−U_(j−1)+1, positive, and it is odd iff U_(j−1) is even. For odd k the recurrence modulo two has period 0,1,1, so j≡1 mod 3. Excluding n=1 makes j=4 the first index, and strict increase plus substitution gives the stated minimum pair and its monotone length as k varies. Binet's formula gives the fixed-k count log(X)/(3 log(alpha))+O_k(1). The checked conclusion is for positive odd terms of step two, not arbitrary square-valued cube sums.

## originality

FAIL

Keskin and Güney's Theorem 12 (public arXiv v1, 25 April 2013) already classifies exactly the positive solutions of u²−(k²−4)n²=4 for all k>3 by the same Lucas sequences. The frozen arithmetic-progression theorem is a direct change of variables and elementary parity filtering of this stronger result, with mechanical first-term and growth consequences. This is verified prior implication, not a claim to have located identical arithmetic-progression wording or to have shown the theorem false.

## value

FAIL

The integrality question is natural and the literal first pair is a useful illustration. As a claimed new theorem the result is a routine specialization of an existing complete Lucas classification, followed by a three-state parity filter and an evaluation at the first retained index. The record does not put forward a distinct invariant or nonmechanical classification beyond this specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
