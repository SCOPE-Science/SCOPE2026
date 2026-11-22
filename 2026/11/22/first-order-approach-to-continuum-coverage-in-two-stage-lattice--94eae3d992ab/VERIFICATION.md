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

# Verification evidence and limits

The first-placement recurrence was independently checked by enumerating feasible accepted-placement sequences with exact rational probabilities on short substrates. Additional exact rational recurrence identities were checked across several rod lengths. Deterministic high-accuracy numerical quadrature independently evaluated the integral representation for several two-stage parameters and compared the rescaled finite-length discrepancies with the predicted constant. Running `python checks.py` yielded `PASS 276 exact and numerical assertions`.

The proof of the asymptotic result is the integral and generating-function argument in `RESULT.md`; finite enumeration and quadrature alone cannot establish the infinite statement. Numerical constants are approximate and an independent mathematical review has not been performed.
