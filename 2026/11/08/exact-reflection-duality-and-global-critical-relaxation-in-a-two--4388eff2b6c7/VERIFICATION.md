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

The global result is proved analytically by reducing the dynamics to an odd monotone inverse map, exploiting strict convexity of its positive branch, and summing reciprocal-square increments at the two neutral thresholds.

The self-contained standard-library checker `verify.py` was executed using `python3 verify.py`. It checked exact binomial coefficients for integers from 3 to 12 and 2,240 signed reflection pairs, then tested noninteger exponents, limiting amplitudes, multipliers, and two critical relaxation coefficients. Its final line was `VERIFY_OK all_exact_and_numerical_checks_passed`.

Numerical examples are finite evidence only. The proof covers every real exponent \(p>2\), every parameter \(0\leq\gamma\leq2\), and every starting difference \(d_0\in[-1,1]\). No computation establishes a theorem for untested real parameters independently of the analytic argument. No independent scientific audit or external certification has been performed.
