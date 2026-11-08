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

# Reproduction and scope of finite checks

Run `python3 verify.py` using a standard Python 3 interpreter, without third-party packages. Expected output is three PASS lines with totals 1,365, 3,807, and 32.

The script exhaustively checks all positive three-/four-run compositions of lengths from 3 through 14 and confirms both exact closed forms and their maxima. It compares direct, set-based enumeration of distinct palindromic subsequences with an independently formulated interval dynamic program on 3,807 short binary words; for odd-run hosts it separately counts subsequence strings having the full host run count. It checks balanced paired-run examples for eight parameter values.

These checks establish only the specified finite instances. The theorem for arbitrarily long words follows from the run-count classification, the AM–GM argument, and the explicit achieving construction given in RESULT.md. No independent external audit has been performed.
