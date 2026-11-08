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

The exact universal viability proof is algebraic. It treats all \(x,p\in[0,1]\), all \(0<\lambda<1\), all \(h>0\), and relevant boundary values, and proves the sharp bounds by explicit attainable/limiting witnesses. Uniqueness of the crossover follows from strict log-concavity and opposite monotonicity, not numerical root finding.

Execute `python3 verify.py` with Python 3 and its standard library. In the saved package the program must return `VERIFY_OK 44939 exact_or_sampled_checks transition ...` to confirm all 44,939 test instances. Its exact Fraction-based checks include a negative value of \(-21719/25000\); floating-point grid and golden-section evaluations test the separate overshoot branches. Numerical tests are supporting diagnostics rather than universal proofs.

This check is not an independent external audit and does not establish publication priority. The theorem concerns the written recurrence, not a particular implementation, and does not establish global population-level dynamics.
