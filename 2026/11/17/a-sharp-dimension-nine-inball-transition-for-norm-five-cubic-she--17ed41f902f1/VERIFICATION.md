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
# Exact computational checks

Execute `python verify.py` with Python 3.10+ and SymPy. The recorded outcome was `PASS: 2916 exact rational / support / rank assertions`. The verifier enumerates polar-chamber vertices using exact `fractions.Fraction`, tests maxima and unique normal patterns in each dimension five through twenty, independently generates complete integer norm-five shells in dimensions five, six, eight and nine, checks the predicted facet supports against every shell vertex, and computes representative supporting-face ranks exactly using SymPy matrices.

The proof in RESULT.md covers every dimension \(d\ge5\) without relying on a computation deadline, omitted cases or finite extrapolation. The checker does not enumerate every facet and does not certify historical priority. No independent audit has been performed.
