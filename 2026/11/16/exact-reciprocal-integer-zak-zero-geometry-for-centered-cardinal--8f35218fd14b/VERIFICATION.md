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

The mathematical proof is the finite-convolution refinement factorization, followed by the classical unit-scale unique-zero theorem and elementary root-of-unity algebra. Finite tests are supporting checks only.

Reproduction: execute `python3 zak_refinement_checker.py` using the Python standard library. The expected output is `CHECK_OK exact_refinement_samples=126 integer_mask_cases=20`. The tests use exact `Fraction` arithmetic at 126 order/scale/position triples and check the Laurent-polynomial identity without rounding.

The tests neither exhaust all orders and scales nor establish global literature priority. The half-frequency exceptional intersection for even subdivisions is identified as a location but its local vanishing order is not claimed. Independent audit: not performed.
