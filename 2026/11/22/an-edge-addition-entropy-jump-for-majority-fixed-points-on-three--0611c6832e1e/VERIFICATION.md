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

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` in the directory containing this document and the script. It exhaustively constructs the 64-state column-pair transfer matrix from the majority inequalities, checks its 110 nonzero entries and its exact integer characteristic polynomial, verifies the strict Schur reductions establishing the root modulus bounds, and compares traces against a separately implemented direct majority update for all labelled configurations of lengths three, four, five and six. Reported fixed counts are 8, 36, 78 and 146; the longer trace sequence is recorded in RESULT.md. The characteristic-polynomial computation and transfer bijection are finite and exact, and therefore establish the formula at every cylinder length; direct finite enumeration alone is not a proof for untested lengths.

The new calculation is specific to a three-row path cross-section and to deterministic tie retention. Historical priority against unindexed equivalents and external mathematical validation remain open.
