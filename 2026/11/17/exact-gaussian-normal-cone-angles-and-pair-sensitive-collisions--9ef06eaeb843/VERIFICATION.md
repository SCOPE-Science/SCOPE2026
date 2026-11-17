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

# Reproducible finite verification

Run `python check_angles.py` with Python 3 and its standard library. The verifier enumerates all \(n!\) coordinate orderings in seven independently specified admissible Johnson-independent forbidden families of sizes \(n=6,7,8\), then optimizes a unique-score linear objective by a brute-force scan of all allowed bases. The chosen superincreasing coordinate weights avoid ties between subset sums. Counts are compared as exact rational numbers with the asserted vertex angles and global collision probabilities.

The exact witness pair yields degree histograms \(\{1:18\}\) and \(\{0:4,1:10,2:4\}\), and collision fractions \(1/18\) and \(113/2025\), respectively. The checker prints `SPARSE_PAVING_GAUSSIAN_ANGLE_PASS cases=7 example=exact` after all assertions pass.

# Proof and limitations

The checker verifies particular finite instances, not the universal theorem. The mathematical proof uses the uniquely second-best subset, uniform conditional index orderings, exact Johnson common-neighbor counts and a matching upper bound. No external independent mathematical validation has been conducted.
