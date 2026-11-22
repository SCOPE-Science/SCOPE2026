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

# Verification

The analytic result follows by deriving the zero-current stationary density, forming the sign function \(A-H_q(y)\), comparing the logarithmic derivative of \(h_q\) against the explicitly increasing \(h_2\), and constructing a strict local decrease of \(H_q\) whenever \(q>2\). These steps prove all positive-parameter quantifiers without numerical enumeration.

The included standalone Python 3 standard-library command is `python3 check_peak_threshold.py`. It performs 2683 deterministic checks in the supplied package: independent finite-difference differentiation, exact integer inequality, stationary-gradient monotonicity samples and q>2 constructive sign conditions. Re-run from the extracted package directory using that exact command. Exact radical identity can also be checked by algebraic rationalization.

Finite numerical assertions are diagnostics; they do not certify the full continuum of ratios or parameters. The entire analytic argument is stated in RESULT.md. The result does not prove a full mode-count classification above the threshold and has not undergone independent assessment.
