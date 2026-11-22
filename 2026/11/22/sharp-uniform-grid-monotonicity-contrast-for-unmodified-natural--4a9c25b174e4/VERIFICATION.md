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

# Reproducibility and checks

The analytic proof obtains the exact whole-line Green sequence, a piecewise polynomial formula for the derivative evaluation operator norm, and a finite-grid recurrence for alternating data. Those identities justify the arbitrary-knot-count conclusion; enumerating examples cannot do so.

The package contains `verify.py`. Run `python verify.py` with Python, SymPy and NumPy. It checks the Green recurrence, the signed and absolute coefficient identities, the two quadratic sign transitions and the exact extremal formula on 12 even-grid lengths, then independently solves randomly chosen natural spline systems and samples derivatives. The exact tests do not verify every length, and finite numerical tests cannot guarantee global monotonicity; that is supplied by the proof in RESULT.md.

The publication comparison covers the cited accessible original research and related published findings, not every historical textbook or inaccessible article. No independent mathematical audit has been performed.
