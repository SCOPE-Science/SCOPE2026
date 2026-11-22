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

From the extracted directory, install the published `requirements.txt` in a suitable Python environment and execute `python3 verify.py`. The script constructs the sixteen-state transfer matrix directly from admissible five-bit windows and verifies its determinant factorization exactly with symbolic polynomial arithmetic. It independently enumerates all \(2^n\) labelled vertex subsets for each \(n=5,6,\ldots,16\), checking the original closed-neighborhood identifying-code definition directly. Each complete cardinality distribution is compared both with the cyclic binomial-gap expressions and with a dynamic-programming transfer trace, and every subset is also compared with the claimed local characterization.

Successful execution produced `DETERMINANT_IDENTITY_OK`, twelve lines beginning `EXHAUSTIVE_OK`, `BINOMIAL_AND_TRANSFER_OK`, and `VERIFY_OK`. The minimum sizes at lengths 5 through 16 were 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10, 11, with corresponding minimum-set counts 5, 9, 7, 32, 30, 50, 33, 45, 13, 98, 153, 384. The total numbers of identifying codes at the same lengths were 11, 16, 29, 65, 67, 96, 166, 220, 391, 645, 924, 1449.

# Mathematical limits

The infinite statement is derived analytically by a complete auxiliary-graph characterization, gap enumeration, and singularity calculation. The finite enumeration is not extrapolated to arbitrary \(n\), and the exact symbolic determinant is supplementary confirmation. No independent audit is asserted. The 2020 minimum-code publication remained inaccessible in full text, so originality is provisional rather than an independent priority certification.
