---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof uses two exact identities and a standard integral lifting argument. The reciprocal eta-quotient is identified with the weight-one series whose coefficient formula in terms of representations as sums of two squares is Theorem 1.1 of Kassel--Reutenauer (2017). Its coefficients in exponents congruent to \(3\pmod4\) therefore vanish identically. The congruence \(H(q)^{2^t}\equiv H(q^2)^{2^{t-1}}\pmod{2^t}\) holds for every integral formal series by repeated squaring; two applications imply the needed support collapse modulo \(2^{\nu_2(k+1)-1}\). Finally, the explicit index-three coefficient attains that exact valuation for each odd \(k\).

Run `python3 verify_congruence.py`. Its expected success output is `DESIGNATED_ODD_K_DYADIC_OK inverse_gap_tests 40 coefficient_divisibility_tests 2600 sharpness_tests 65 independent_inverse_coefficients 81`. The finite diagnostics test odd \(k\le129\) and indices \(4n+3\le159\); the source theorem and algebraic argument, not finite evidence, establish all-index validity. No independent proof review has been performed.
