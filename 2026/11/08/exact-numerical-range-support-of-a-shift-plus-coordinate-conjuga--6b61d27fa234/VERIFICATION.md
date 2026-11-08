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

The analytical proof is in RESULT.md. The separate executable diagnostic `check_real_shift_conjugation.py` verifies that real-coordinate quadratic forms agree with the complex definition (320 random finite cases) and checks the sharp support against 35 finite-section symmetric matrices (70 assertions), totaling 390 finite assertions. Execute `python check_real_shift_conjugation.py` with NumPy installed.

For every \(a>0\), no finite matrix approximates a weakly null sequence by itself. The lower support bound uses growing modulated blocks, while nonattainment uses the strict uniqueness of the Fourier-symbol maximizer. Publication priority is not independently established.
