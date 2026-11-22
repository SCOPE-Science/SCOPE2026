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

# Reproducibility

Run `python3 check.py` in the extracted directory. The program is deterministic, uses Python's standard library and exact integer arithmetic, and finishes with a `PASS` line after all assertions.

The test reconstructs each allowed word by checking for forbidden runs. It computes its complete Walsh spectrum with an integer butterfly and separately by a finite-state dynamic program for every frequency. All \(2^n\) characters are checked for each \(1\le n\le13\); at dimension \(13\) this is exactly \(8192\) coefficient-by-coefficient comparisons. It checks the zero multiplicities at each Walsh degree, the earliest cubic zero cutoff, and the four cubic masks. Additional finite checks for other forbidden-run lengths do not constitute proofs at untested parameters; the relevant infinite auxiliary congruence is proved algebraically in `RESULT.md`.

A computation's completion is not a publication-priority certificate; the mathematical statement remains subject to independent assessment.
