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

Run `python3 verify_motzkin.py` using Python 3 with SymPy installed. The verifier computes exact integer coefficients of the six moment series for lengths through 250; independently generates every Motzkin word through length 12 and compares six moment sums at each length; expands the six algebraic generating functions around their unique dominant singularity by symbolic Laurent series; verifies all 18 amplitude/correction entries; and simplifies the covariance cancellations exactly to \(0\), \(-1\), and \(2\) as required. The observed run printed `passed: 1106 checks` and numerical diagnostics agreeing with the theorem.

These finite checks do not independently establish an asymptotic theorem: the mathematical justification is the first-return generating function identity, explicit derivatives, unique dominant singularity and gamma-ratio transfer expansion in `RESULT.md`. No independent external validation was performed, and the code does not assess scientific novelty.
