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

The mathematical argument and all stated parameter bounds appear in `RESULT.md`.
Running `python CHECK.py` with the Python standard library produced:

`QARY_CAP_THREE_NEGATIVE_TYPE_PASS parameter_cases=784 direct_characters=701`

The program directly evaluates 701 nonconstant complex characters (at two exponents each), separately from the closed Krawtchouk formula, and also exercises the threshold and asymptotic formulas. Finite checks do not certify the infinite statement. The essential exact steps are the identity for the degree-two character sum, the inequality \(2<(3^p-1)/(3^p-2^p)<3\) for \(0<p<1\), and the strict derivative and endpoint comparisons proved in the paper.

Self-review was completed. Independent mathematical review was not performed.
