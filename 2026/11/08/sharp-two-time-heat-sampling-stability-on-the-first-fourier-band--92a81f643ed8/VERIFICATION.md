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

# Reproducibility and limits

Install `numpy>=1.24` from `requirements.txt` and run `python CHECK.py` in the directory containing the embedded files. The program constructs orthonormal graph cosine/sine modes for cycles of orders 5 through 90 and the four raw measurements for every site separation and five damping ratios. It independently computes each Gram spectrum and compares all three eigenvalues to the analytic formula. It verifies the unique continuous root, evaluates the exact finite-grid bracketing rule, and tests representative short-time asymptotics. The saved checker reports `CYCLE_TWO_TIME_FRAME_CHECKS_PASSED 10968`.

The proof's critical infinite steps are the exact orthogonal Gram decomposition, an analytic strict-monotonicity certificate for the smaller block eigenvalue, and the unique crossing with a decreasing scalar eigenvalue. Numerical tests do not establish those steps for arbitrary parameters. No symbolic-computation package or external certification is required by the proof.
