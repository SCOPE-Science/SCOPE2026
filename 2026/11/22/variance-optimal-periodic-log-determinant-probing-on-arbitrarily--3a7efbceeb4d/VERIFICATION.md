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

From a directory containing the supplied standalone code files, run `python verify.py` using only the Python standard library. It constructs 14 heterogeneous rational killed-path matrices with sizes 2 through 8; computes three-shift exact resolvent mixtures; checks positivity of every strict interval coefficient, its telescoping representation, and the global minimum and unique equality case among all unlabeled partitions for every allowed color budget; then checks the homogeneous logarithm Fourier identity. Expected output: `PASS 21587 exact/Fourier assertions in 14 rational path cases, n=2..8`.

With NumPy and SciPy installed, run `python verify_log_numeric.py`. It constructs the corresponding symmetric matrix logarithms by eigendecomposition; checks direct variances over all unlabeled partitions; and compares finite homogeneous-path variances to the proved large-size formula. Expected output: `PASS 21184 log-matrix floating-point comparisons, n<=8 and homogeneous limits`.

These are genuine executed tests. The rational resolvent calculations are exact; the Fourier and matrix-logarithm comparisons are floating point. Finite enumeration and numerical approximation cannot establish the universal theorem; its proof is in `RESULT.md`. No independent mathematical audit has been performed.
