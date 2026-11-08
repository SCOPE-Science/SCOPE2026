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

# Reproducibility and limitations

Execute `python verify.py` with Python 3 and `sympy`. The program verifies first-step identities for mean and raw second moment at generic and exceptional states as symbolic polynomial identities for arbitrary odd \(n\ge3\); it also verifies the reduction from the quartic second-moment potential to the variance formula. An independent state-pair matrix computation over exact rational numbers at lengths 3, 5, 7 and 9 checks the indexing and rule normalization. Expected final line: `SYMBOLIC_ALL_ODD_N_OK`.

A finite enumeration is not used as an infinite proof; the proof is an all-parameter algebraic potential with a finite absorbing-chain uniqueness argument. No independent external scientific audit is claimed. The analysis excludes even orders, biased letters, other pairs, and full-state reset times.
