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

# Reproducible verification

Run `python3 verify.py` in a directory containing the standalone checker. It requires Python 3 and only its standard library. The completed run produced `VERIFY_OK 35662 rational and numerical checks`. The program independently implements the two-projection eigenvalue calculation and checks the algebraic optimum, work normalization, limiting price imbalance, and a closed-form rational example.

The verification code is finite and numerical/rational; it cannot prove a theorem for all positive prices and all positive-definite Hessians, and is not an independent audit. The general mathematical proof is in `RESULT.md`. Literature search is not a certificate of publication priority. The most material remaining risk is equivalent historical two-regressor E-optimal design with unequal observation costs, whose complete primary sources were not available for comparison.
