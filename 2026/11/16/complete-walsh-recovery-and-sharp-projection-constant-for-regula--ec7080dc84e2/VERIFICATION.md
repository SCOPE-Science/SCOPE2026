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

# Exact reproducibility

Execute `python3 verify_k7.py` using Python 3 and the standard library. The script uses a recursive construction by vertex outgoing choices and fifteen-bit parity reduction. It asserts exactly \(2640\) distinct regular tournaments, exact Parseval, the complete all-character absolute-value histogram after lifting by \(64\), the exact convolution rank and a second fifteen-bit Walsh pass giving the projection kernel norm. It prints `REGULAR_K7_QUOTIENT_PASS` only if every asserted count holds.

Independently execute `g++ -O3 -std=c++17 -o verify_k7_full verify_k7_full.cpp && ./verify_k7_full`. The compiled checker enumerates every one of the \(2^{21}\) labelled orientations and computes the complete integer Walsh transform and inverse projection-support Walsh transform. It asserts count, rank, zero frequency count, minimum and maximum nonzero multipliers, Parseval and endpoint kernel absolute sum and prints `REGULAR_K7_FULL_PASS`.

Both programs have been executed successfully with the exact source files in this package. Their enumerations use different search spaces and approaches. The finite checks are exact and exhaustive; proof of projection optimality is the translation-averaging argument in `RESULT.md`. The certificate `SPECTRUM_CERTIFICATE.json` records numerical assertions and a deterministic quotient-transform SHA-256 for further byte-for-byte comparison. No higher-order or independent-external claim is made.
