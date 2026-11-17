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

Run `python checker.py` in an environment with the Python dependencies listed in `requirements.txt`.

The checker uses exact symbolic identities to reconstruct all four normalized add/subtract equations of the proof. It confirms that for \(r=16/5\), the scalar two-cycle is strictly positive and has exact second-iterate multiplier \(4/25\). It solves the two polynomial coupled period-two equations at \(c=d=10^{-4}\) for both sharpness orientations and verifies residuals below \(10^{-45}\), distinct positive coordinates inside \((0,1)^2\), and both multipliers strictly inside the unit circle.

The universal absence statement is proved by AM–HM inequalities and the nonsingular difference matrix; the numerical examples test only particular small positive couplings. The proof's sharpness uses the implicit-function theorem and does not depend on a finite grid. Full independent audit and exhaustive literature priority checks have not been performed.
