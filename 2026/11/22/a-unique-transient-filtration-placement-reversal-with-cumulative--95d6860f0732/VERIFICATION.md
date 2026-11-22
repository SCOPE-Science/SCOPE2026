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

# Reproduction

Install Python 3 and the packages listed in `requirements.txt`, then run `python verify.py` from the directory holding the extracted files. The script prints the exact symbolic determinant/Green-function identities and an independently evaluated matrix-exponential example. The analytic proof, including the all-parameter and infinite-time quantifiers, is in `RESULT.md`; finite checks do not constitute a substitute for its nonstandard reduction and the cited classical log-concavity theorem.

# Verified checks and limitations

The symbolic computations use integer/rational algebra and independently reconstruct the three-room matrices. The normalized illustration uses 70-digit arbitrary-precision arithmetic and confirms the crossing, the two signs and the exact total integrated difference. These are reproducibility checks, not interval-certified numerical proofs of the displayed decimal approximation or a certificate of novelty. No empirical calibration or independent audit has been performed.
