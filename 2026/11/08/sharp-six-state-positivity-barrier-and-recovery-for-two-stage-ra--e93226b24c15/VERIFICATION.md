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

# Verification details

The bundled `verify.py` and `certificate.json` were executed as actual files using standard-library exact rational arithmetic. The verifier returned `VERIFY_OK` with 112 counted assertions. It checks polynomial identities for the full first column of the two-stage Radau IIA transition matrix on directed cycles of sizes \(2\) through \(6\); the first column determines all entries by circulant symmetry. It also checks denominator and numerator coefficient signs, the exceptional six-cycle diagonal polynomial and root interval, the scalar fifth Taylor coefficient, and independent rational matrix inversions for the eight-cycle at three specified steps.

Run `python3 verify.py` in the extracted file directory to reproduce `verification_output.txt`. No network, downloaded data, source paper, or additional package is required. For arbitrary cycle sizes, the proof uses the analytic negative fifth coefficient and Fourier limit, not finite verification. Computational checks do not prove absence of unexamined literature overlap. External independent validation is not included.
