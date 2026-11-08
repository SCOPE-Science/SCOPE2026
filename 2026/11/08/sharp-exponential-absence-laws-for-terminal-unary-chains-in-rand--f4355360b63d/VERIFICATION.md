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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 (no third-party dependencies). Expected output:

`VERIFY_OK 100 comparisons including exhaustive recursive trees through 9 vertices`

The program independently enumerates every parent-choice vector for random recursive trees on \(1\) through \(9\) labelled vertices, tests absence of the fringe chain of \(r=2\) through \(6\) vertices, and compares the resulting integer counts against exact rational coefficients from the analytic generating-function recurrence. It also checks the special boundary cases, including the single forbidden path at \(n=r\).

The all-\(n\) probability and sharp asymptotic rely on the derivation in RESULT.md: (i) a root-SET construction, (ii) an exactly solved linear ODE, (iii) injectivity on the complex disk \(|z|<3/2\), and (iv) Cauchy coefficient estimates. Exhaustive finite tests cannot establish these infinite analytic claims. The proof gives no uniform varying-\(r\) error and has not undergone independent mathematical validation.
