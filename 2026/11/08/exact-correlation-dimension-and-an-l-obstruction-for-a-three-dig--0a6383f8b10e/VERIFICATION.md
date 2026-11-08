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

Run `python3 CHECK.py` with the standard Python interpreter. The program enumerates all 81 digit quadruples, constructs the integer carry matrix independently, obtains its first seven central powers, tests the exact second-order recurrence, and compares the results against separate brute-force additive-energy calculations at levels one through four.

The *infinite* assertions instead rest on the explicit carry-state completeness argument and the uniform factor-two comparison between truncated and full convolution grid energies. The strict \(L^2\) obstruction follows from \(4\lambda_+/81>1\) and the grid-interval Cauchy--Schwarz inequality. Numerical checks cannot establish singularity of the convolution or its \(L^p\) regularity for \(1\le p<2\); neither is asserted.

The scientific comparison checked the full accessible HTML versions of arXiv:2606.07143, arXiv:2602.08568, and arXiv:2201.01909. General finite-type overlap machinery remains potentially relevant; independent review of historical priority has not been performed.
