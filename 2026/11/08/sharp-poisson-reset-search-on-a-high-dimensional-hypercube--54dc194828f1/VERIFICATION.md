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

Run `python verify.py` with Python 3. No third-party packages are required. The program solves the exact killed Hamming-weight birth–death backward equations and independently integrates the product-chain transition density by Simpson quadrature, then compares 45 values. It also numerically minimizes the mean for fixed distances two, three, four and four increasing hypercube dimensions. These are finite sanity checks, not a certificate of an asymptotic theorem. The proof of the infinite result, including all boundary reset-rate regimes, is given in `RESULT.md`.

The exact normalization is one coordinate flip per coordinate per unit time, hence the total walk jump rate is the dimension. The reset rate is independent and returns to the initial non-target vertex. The limit holds with the starting Hamming distance fixed. Historical novelty has not been independently certified.
