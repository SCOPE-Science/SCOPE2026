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

# Reproduction and scope

Run `python CHECKER.py` after installing `requirements.txt`. It compares exact analytical singular values with those of a numerical real lifted measurement matrix assembled from independent sampled Gaussian-STFT intensities. It also tests the optimizer and the branch crossing across small, critical and large tone offsets. The checker has only finite scope; the unrestricted proof is in `RESULT.md`. The integral normalization is the average over one beat period, and the coefficient-space normalization is Hilbert--Schmidt.

No independent mathematical audit has been performed.
