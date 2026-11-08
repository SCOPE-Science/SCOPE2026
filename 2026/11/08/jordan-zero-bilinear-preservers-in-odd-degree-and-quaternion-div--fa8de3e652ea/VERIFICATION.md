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

# Verification record

Executing `python3 checks/verify.py` from the extracted package produces the embedded exact output in `checks/verification_output.txt`:

```
QUATERNION_OK zero_span=8 jordan_rank=4 bilinear_space=8 obstruction_dim=4
SPLIT_OK field=F3 Jordan_zero_pairs=417 zero_span=12 obstruction_dim=0
VERIFY_OK
```

The rational Hamilton-quaternion test checks eight explicit anticommuting pairs, the rank of their tensor span, surjectivity of the Jordan multiplication, and independence of four obstructions modulo four factorable bilinear forms. The matrix-algebra test exhausts all ordered pairs over \(\mathbb F_3\), then checks that the zero-Jordan pair tensors fill the twelve-dimensional kernel. These are exact finite tests, not general proofs. The odd-degree assertion is established symbolically by reduced-norm parity; arbitrary-field quaternion and split assertions rest on the general proof and the identified literature theorem. No independent mathematical audit was performed.
