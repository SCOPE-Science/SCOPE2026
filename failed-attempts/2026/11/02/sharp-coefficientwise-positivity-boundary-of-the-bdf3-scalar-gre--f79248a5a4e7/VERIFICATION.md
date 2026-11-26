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

The normalized impulse response has exactly the generating function and seeds stated. I independently expanded it through degree 7, reduced both denominator-cleared new characteristic polynomials modulo the original cubic (zero remainders), and verified the Bernstein table by substituting x=(a+bv)/(1+v), multiplying by (1+v)^deg, and comparing rational coefficients. These are exact checks: H(1/16)=−35/1024 and H(76/1215)=8464/4100625, and H' has strictly positive coefficients in that interval basis. The two nonnegative sparse recurrences cover [x*,256/3915] by induction on the nonnegative seeds. At x* the n and n+1 terms of the order-eight recurrence have strictly positive multipliers, and G₆ is the only zero seed, so no pair of consecutive seeds/later terms can force a second zero. For the large-x segment, d=D(r)/r³ decreases strictly since d'=-6E(r)/r⁴; Vieta and the simple-root residue formula give the stated amplitude identity. The Taylor expansion of T at 8/15 has positive coefficients (constant 344/5625, then 6772/375, 1026/25, 669/5, 126), proving the amplitude bound there. For d>16, r<1/2 and the nonreal pair has strictly larger modulus and nonzero residues. Each sign recurs by density, or in the rational-phase case by the mean-zero nonconstant values of the finite phase cycle. Root moduli are below one and evaluating the convergent generating function at one proves the exact gain identity. Reproduction of the exact algebra can use symbolic polynomial series/remainders and the stated rational substitution; the frozen script was inspected, not executed. This is not a maximum principle for arbitrary starting histories.

## originality

FAIL

Lóczi, arXiv:1609.07858v2, Theorems 1.6 and 2.3, section 3.5 and §3.5.3, already proves the exact all-coefficients threshold and unique zero at index six for the same sequence. Write γ for his step-size variable and m_n(γ) for his auxiliary sequence. Setting x=1/(6γ+11), his initial values and recurrence give m_n(γ)=6xG_n(γ) for every n. This is not an analogy with boundedness: for BDF3 the theorem's stability-interior condition is automatic, so it is literally equivalent to nonnegativity of these same sequence coefficients (the n=0 term is positive). The earlier polynomial is exactly (6γ+11)^4 H(1/(6γ+11)), and §3.5.3 explicitly proves strict positivity at the endpoint except at n=6. Qiu's later sufficient interval for the same sequence is therefore not the strongest prior coverage.

## value

FAIL

This is an important endpoint for distinguishing stability from positivity, but the exact endpoint, all-index positivity classification and endpoint zero are known. The submitted finite sign-range lead-in and gain condition are elementary consequences; the sparse recurrences give an alternate special-purpose validation without a demonstrated general or separately motivated mathematical contribution. The frozen submission cannot stand as a new sharp classification by adding that certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
