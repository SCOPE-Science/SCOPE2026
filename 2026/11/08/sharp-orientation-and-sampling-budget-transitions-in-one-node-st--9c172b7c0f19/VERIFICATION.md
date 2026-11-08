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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 with only its standard library. The program enumerates all four equally likely sign vectors, and for probe budgets up to four explicitly enumerates each finite probe sequence. It compares their empirical finite-support means and MSEs against the independent analytic formula and tests both endpoint and minimizer predictions on parameter grids. It produces the recorded `verification_output.txt` of 80,540 checks. The output should state `PASS`.

The *proof* of all real-parameter extrema, equality cases and phase thresholds is the derivative and monotonicity argument in `RESULT.md`. Grid checks are regression tests and do not establish universal assertions. The exact integer-probe distribution assumes independent probes; all logarithm arguments are positive because \(a>b>0\). No external independent review or certification has been conducted. An unrelated numerical or source-discovery failure would not be evidence that a universal mathematical claim is impossible.
