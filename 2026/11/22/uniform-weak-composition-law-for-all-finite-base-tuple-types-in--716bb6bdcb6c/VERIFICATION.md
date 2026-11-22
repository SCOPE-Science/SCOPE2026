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

Execute `python3 verify_s3.py` in the directory holding the extracted package files; its last line must read `ALL_13_EXACT_DIAGRAM_TESTS_PASS` and its preceding output must equal `verification_output.txt` byte-for-byte. The program uses only the Python standard library (`fractions`, `itertools`, `math`).

All sampled coordinates are exact rational points in the circle, and the expected count is cross-checked against a set of independently generated ternary relation signatures (rather than against equivalent gap-order data). For each tested arity the finite sample has enough distinct projected positions inside every gap to realize all coordinate orders; combinations with two identical quotient projections are excluded because they would have displacement exactly one-third or two-thirds of a circle and lie outside the homogeneous domain. The computation verifies the finite test cases only. The all-arity mathematical proof and conditions are in `RESULT.md`.

The record documents self-review. An independent audit has not been performed.
