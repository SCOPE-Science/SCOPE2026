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
# Verification notes

The standalone script `verification/verify.py` uses only Python's standard library. Run `python3 verification/verify.py` from the package root. It reconstructs coefficient-polynomial multiplication and counts exact element orders by direct multiplication for selected prime fields, independently tests extension fields \(\mathbb F_4\) and \(\mathbb F_9\), counts classes of each exact order from all commuting pairs, and tests coefficient multiplication against the corresponding triangular matrices.

Expected final markers: `NULL_FILIFORM_ORDER_SPECTRA_VERIFIED`, `EXTENSION_FIELD_SPECTRA_VERIFIED`, `MATRIX_MODEL_VERIFIED`, and `JOINT_ORDER_CONJUGACY_VERIFIED`. These checks were executed on the package's exact script source. They validate the listed finite examples; the all-parameter proof is written in RESULT.md. The assumptions and prior-literature qualification are recorded there. Independent audit has not been performed.
