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

Run the provided standard-library-only `CHECK.py` using a recent Python 3 interpreter. The program computes every self-STFT coefficient by exact integer cyclotomic residue histograms in five parameter configurations, separately checks exact squared magnitudes, and counts zero/nonzero tiers against the stated formulas. It covers odd prime orders \(3\), \(5\), horizontal dimensions \(1\), \(2\), and several nonzero quadratic coefficients.

The same checker independently sums the transform directly for two nonconstant complex profiles at prime orders \(3\) and \(5\), testing *every* translation-modulation pair against the arbitrary-profile factorization, with tolerance \(10^{-10}\). The exact integer tests and general-profile tests both passed when run on the complete supplied source. The terminal markers are `ALL_EXACT_STFT_CHECKS_PASSED` and `ALL_GENERAL_PROFILE_CHECKS_PASSED`.

These checks are finite and do not certify the unrestricted result for all prime powers or all dimensions. The analytic proof uses only the group law, finite-character orthogonality, a one-dimensional variable substitution, and an elementary quadratic-character sum; no external numerical certificates are assumed.
