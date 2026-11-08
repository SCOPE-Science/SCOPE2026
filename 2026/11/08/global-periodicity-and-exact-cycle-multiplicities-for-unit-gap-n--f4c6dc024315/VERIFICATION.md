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

Run `python3 CHECK.py` with Python 3.8 or later (standard library only). Expected output is `EXACT_INTEGER_RETURN_AND_CYCLE_CHECK_OK 22160`.

The checker performs the integer recurrence directly and independently evaluates the claimed first-return formula for 8 parameter values and all coordinates of 19 full layers, tests distinctness and least-return counts, verifies the return-roof sums, and confirms primitive original-map periods on the first five layers. No floating-point arithmetic is used. These checks are finite and are not presented as an exhaustive proof for all integers. The complete mathematical argument is in `RESULT.md`.

The explicit finite checks were run successfully before packaging; the packaged source was rerun after extraction. Independent mathematical validation has not been performed.
