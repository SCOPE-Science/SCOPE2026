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

# Reproducibility and scope

Run `python check_null_xray.py` from the same directory as the six research text files. The script uses Python standard libraries and optionally NumPy for two direct normal-matrix diagonalizations.

On inspection, the script computes all projective null directions for sample odd finite fields and all Fourier normal multipliers, then checks the predicted multiplicities and a deterministic nonuniform direction-weighting inequality. It covers both quadratic-form types when the dimension is even and includes the extension field \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). For \(q=3\) and dimensions \(3,4\), it builds the actual point-to-affine-line incidence matrix and compares the complete eigenvalue spectrum of its normal operator against the formula.

Expected successful terminal line: `NULL_RAY_FOURIER_VERIFICATION_PASS`. The directly computed dimension-three kernel has dimension \(6\) when \(q=3\), and the nonsplit dimension-four case has normal multipliers \(3,12,30\) with multiplicities \(20,60,1\), respectively.

The finite computations do not prove infinite-field or dimension claims. Those follow from the provided quadratic Gauss-sum zero-count formulas, hyperplane sections, Fourier orthogonality, and group-averaging argument. No independent audit has been performed.
