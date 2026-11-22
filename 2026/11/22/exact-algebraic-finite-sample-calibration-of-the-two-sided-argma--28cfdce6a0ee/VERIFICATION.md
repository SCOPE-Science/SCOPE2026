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

# Exact checks and reproduction

Run `python3 verification_checks.py` from the directory holding `exact_ks_argmax.py` and `verification_checks.py` with Python 3, SymPy and NumPy installed. The script completed **120 assertions** with the output `PASS: 120 exact/sign/monotonicity/simulation assertions`.

The exact tests independently compare the algorithm with the hand-derived one-observation formula at six thresholds, compare closed radical expressions at sample sizes one to four, and use algebraic sign evaluations to certify that the exact three-observation \(95\%\) quantile belongs to \((2.2981,2.2982)\). The remaining exact checks establish positivity, boundedness by one, and monotonicity on a fixed rational grid for sample sizes one through six. Finally, a seeded direct-order-statistic simulation on 200,000 independent samples per size compares the original statistic against the exact CDF at three thresholds. These simulations are only diagnostics; they cannot prove general correctness.

The code uses rational arithmetic, symbolic polynomials and exact real-algebraic sign comparisons in the CDF calculation. It does not substitute numerical quadrature for proof. The finite terminating chamber decomposition and ordered-simplex bin recurrence are proved in RESULT.md. The program has no external file dependencies beyond its sibling script and Python's installed scientific packages and makes no network calls. The runtime and expression size can grow substantially as sample size increases.

Only the self-review described in REVIEW.md and AUDIT.json have been performed. No external or independent mathematical audit is represented by these results.
