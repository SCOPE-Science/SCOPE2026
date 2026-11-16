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

# Verification of the primitive-word Walsh result

Run `python3 verify.py` in the same directory as this document. The script uses only the Python standard library and enumerates primitive indicators **directly** by proper-block repetition tests, rather than generating them from the claimed Möbius formula. A separate integer Walsh–Hadamard transform produces the actual full spectrum.

The checker tests every frequency for each \(2\le n\le16\), including squarefree values, prime powers, and mixed exponents. It compares direct transforms with the independent Möbius character expression, verifies the predicted rank, zero locations, congruence valuations, sharp positive multiplier, explicit witness and zero-frequency count. A separate exhaustive translation-stabilizer check runs through \(2\le n\le8\).

Observed replay output:

`PRIMITIVE_BINARY_WALSH_EXACT_PASS lengths=2..16; all frequencies and stabilizers<=8`

**Proof boundary:** The finite computation is not an all-length proof. The all-length argument uses pointwise Möbius inversion, group-character orthogonality, one term of minimal 2-adic order, and the explicit minimal-magnitude witness, as written in `RESULT.md`. There is no external independent audit or certification.
