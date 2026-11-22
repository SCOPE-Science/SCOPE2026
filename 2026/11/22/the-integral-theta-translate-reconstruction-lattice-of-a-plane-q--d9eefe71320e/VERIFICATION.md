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

Run `python3 VERIFY.py` in the same directory. This reconstructs all 4,096 matrix entries from the six-coordinate quadratic form, checks all 4,096 Gram entries against the design identity, computes all 64 two-adic invariant-factor valuations by invertible modular row/column elimination, reconstructs the full Smith form from the exact determinant, and checks the claimed explicit integral inverse identity. No external packages are required.

The finite computation is exhaustive for the specified 64-element configuration and is used only to establish the exact 2-primary Smith multiplicities. The geometric identification and intersection-number/determinant formulas are proved symbolically in RESULT.md. No claim is made about computations in other genera or about a geometric divisor-class lattice. An independent mathematical audit has not been conducted.
