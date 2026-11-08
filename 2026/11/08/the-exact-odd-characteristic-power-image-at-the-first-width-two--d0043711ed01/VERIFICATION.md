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

The packaged `power_test.py` has no external dependencies and can be run as `python power_test.py`. `check_output.txt` is the recorded output of executing this exact program. It computes \(N^p\) from actual upper-triangular matrix entries, tests every possible target over the prime fields of orders three and five against an explicit construction, and independently enumerates all \(3^{12}\) effective source-coordinate assignments for \(p=3\). The final enumeration is exhaustive over the effective variables because only the first three superdiagonals of \(N\) contribute to \(N^p\) at dimension \(p+3\); its other entries contribute to no output coordinates. Over prime fields, modular integer operations implement exact finite-field arithmetic.

Observed markers: `ALL_TARGET_CONSTRUCTIONS_PASS p=3 q=3 images=585`; `ALL_TARGET_CONSTRUCTIONS_PASS p=5 q=5 images=13225`; `EXHAUSTIVE_POWER_IMAGE_PASS p=3 q=3 effective_sources=531441 images=585`; `ALL_FIRST_WIDTH_TWO_POWER_CHECKS_PASS`.

The code is a finite verification only. The arbitrary-prime and arbitrary-field conclusion relies on the constructive path proof in `RESULT.md`. No finite computation proves originality or mathematical generality by itself. Independent audit has not been carried out.
