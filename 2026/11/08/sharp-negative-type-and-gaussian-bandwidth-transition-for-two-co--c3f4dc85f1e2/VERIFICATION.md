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

# Verification report

The companion `check_rank_kernel.py` was executed with Python 3 and only the standard library. It exhaustively enumerated all rank-one and rank-two elements and all additive Fourier frequencies for \(M_{2,2}(\mathbb F_2)\), \(M_{2,2}(\mathbb F_3)\), \(M_{3,2}(\mathbb F_2)\) and \(M_{2,2}(\mathbb F_4)\), with sizes 16, 81, 64 and 256. All 417 exact rank-sphere character comparisons passed, including genuine characteristic-two extension-field trace characters. The critical projective-line identity was also verified exhaustively over \(\mathbb F_4\). Further real-power frequency and threshold evaluations passed, including \(\alpha=1\) for six field sizes. Final output: `ALL_TWO_COLUMN_RANK_KERNEL_CHECKS_OK`.

The finite enumerations do not establish the claimed uniform theorem for every prime power and row dimension. The proof of the infinite statement uses the exact outer-product character sum and strict convexity, both shown in RESULT.md. At the phase boundary, zero eigenvalues occur only on full-rank frequency matrices, and their exact number is \((q^m-1)(q^m-q)\). No independent mathematical audit has been performed.
