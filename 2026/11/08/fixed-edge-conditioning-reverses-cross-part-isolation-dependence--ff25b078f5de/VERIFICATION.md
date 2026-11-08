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

# Reproducibility

Execute `python verify.py` from the extracted package directory using Python 3 (standard library only). The script computes exact rational probabilities and independently enumerates complete binary-matrix sample spaces up to \(4\times4\), checks sign and factorization identities for \(2\le a,b\le12\), and compares with the independent-edge probability model. It additionally sanity-checks the sparse asymptotic covariance, variance and correlation constants on finite matrices. Expected observed output:

```
PASS: 17150 exact/sign/product/ensemble checks plus sparse-scale sanity checks
```

The derivation of the all-size sign and asymptotic limits is in RESULT.md, and is not replaced by enumeration or approximate numeric convergence. Earlier matrix-occupancy publications without accessible full text remain a historical-priority limitation.
