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

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy installed. The script checks five symbolic identities including equality of traces/determinants and the exact signed contraction, then makes 45 exact-rational substitutions and 120 independent higher-dimensional exponential evaluations. The output from a successful execution is included verbatim in `verification_output.txt`.

These finite checks supplement the two-dimensional exact identity and strict hyperbolic monotonicity proof in `RESULT.md`. They do not certify historical priority, nor independently validate the mathematical proof. All checked code and output are packaged alongside this document.
