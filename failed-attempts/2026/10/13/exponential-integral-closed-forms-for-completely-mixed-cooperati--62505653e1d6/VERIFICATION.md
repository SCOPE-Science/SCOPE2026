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

The final mathematical claim is correct. Pires–Broom §4.2, equations (23)–(24), gives the stated signs, harmonic subtraction and scaling. Write n_M/M→Q with n_M integer (for example n_M=floor(MQ)); fixing Q and insisting on exactly integral MQ only works for rational Q, and the frozen result explicitly allows the rounded endpoint. For r_M=M log(1−1/M), use (e^{a x}−1)/x=∫_0^a e^{u x}du including x=0. This proves uniform convergence of the two integrands on any compact interval, since their signed exponent parameters tend to −1 and 1. The mesh-1/M sums with cutoff n_M−1 then give the claimed integrals. From the entire exponential integral these are Ein(Q) and −Ein(−Q), with the stated real-axis E₁/Ei formulas, zero limits, derivatives and large-Q asymptotics. They are auxiliary functions in the published weak-selection conditions, not the complete thresholds. The bundled series check was inspected, not executed. Its alternating double-precision Q=20 calculation is affected by cancellation: independent stable quadrature gives L₁(20)≈3.57294793855388, about 2.23×10⁻¹⁰ from the hard-coded value, exceeding its nominal ~7.15×10⁻¹¹ test tolerance. The reported rounded checks remain consistent, but the checker is not evidence for that nominal precision; the analytic proof does not depend on it.

## originality

PASS

Limited to explicit identification of the two named population limits with the complementary exponential integral. The integrals, conversions, derivatives and large-argument asymptotics are classical once the limits are written as integrals; no novelty is credited to those identities in isolation. The inspected source passages define the original limits and give examples and qualitative growth, not the identification itself.

## value

FAIL

The auxiliary quantities are motivated, and the conversion is convenient, but the claimed gain is exhausted by reading a fixed-endpoint Riemann sum as the defining integral of Ein. The derivatives and precise large-Q rates then follow directly from the classical definition and standard asymptotics. The source already describes the opposite growth behaviors and reports representative values. The frozen record does not use the conversion to establish a distinct quantitative property of a threshold, a new density range or error estimate, or another independently useful fact beyond that routine evaluation. This fails the value requirement for the actual contribution, not the correctness of the formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
