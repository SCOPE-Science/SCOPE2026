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

The analytical theorem uses an exact, closed covariance-square integral and the identity
\[
G_a''(t)+2aG_a'(t)=\frac{e^{-2at}-e^{-2a(1-t)}}a.
\]
Its sign changes only at the midpoint, while the gain derivative has exactly one zero after that midpoint. The argument proves global uniqueness for every positive rate and every positive observation-noise variance; a finite test grid alone would not imply this theorem.

Run `python verify.py` with Python 3, SymPy and SciPy. The script checks four symbolic identities and 60 independently evaluated covariance/optimization instances. All checks passed on the exact embedded source. The test does not establish literature uniqueness, does not substitute for independent validation, and does not assess other initializations or multiple observations.
