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

# Reproduction and limits

Run `python verify_panhandle_loewner.py` with Python and NumPy. It uses explicit binary-base enumeration, reconstructs full covariance matrices rather than just evaluating the stated eigenvalue formulas, and checks spectral multiplicities, all-vertex quadratic contacts and asymptotic root scales. Replayed result: `PANHANDLE_LOEWNER_PASS configurations=39 asymptotic_tests=9`.

These checks are finite numerical corroboration. The exact all-parameter theorem requires the analytic proof in `RESULT.md`, including the trace–determinant global certificate; no external or independent audit is asserted.
