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

# Verification

Execute `python3 check_spectrum.py` from a directory containing the included checker and output file. The standalone checker independently forms products in the finite Rees semigroup and computes the \(mn\)-dimensional real mutual-zero-product matrix, then compares it to the singular-value prediction and selected matrix moments. Exhaustive cases include all 327 binary regular sandwich matrices with each dimension from 1 to 3. A fixed random seed supplies another 400 rectangular or square patterns with dimensions \((4,4),(4,5),(5,4),(6,6)\). The actual execution output is in `checker_output.txt`.

The matrix proof in RESULT.md is finite-dimensional but uniform in every \(m,n\), including repeated or missing singular values and zero patterns. Finite tests cannot establish an all-size identity, and the historical-priority comparison is not an independent audit.
