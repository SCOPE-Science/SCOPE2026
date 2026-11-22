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

# Reproduction of finite Fourier certificate

Run `python3 checker.py certificate.json` from the directory containing both files. The verifier uses only Python standard-library exact integers. At each order one through eight it reconstructs every restricted-growth word and independently computes the histogram by the position-wise block-opener product; then it compares all direct signed character sums against all integer-butterfly entries and the complete stored spectrum. It also checks the Bell totals and the stated zero masks and sharp nonzero magnitudes. The dimension-eight certificate has 128 reduced Walsh values, encoding all 256 full Fourier values by toggling the forced first opener.

The optimal endpoint projection at dimension five additionally follows from the two exact null frequencies and translation averaging, as proved in `RESULT.md`; it does not require a numerical optimization. No randomness or approximation is used. No theorem for larger dimensions is claimed, and no independent audit is represented.
